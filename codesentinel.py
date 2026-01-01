#!/usr/bin/env python3
"""
CodeSentinel
Single-file secure Python code analyzer & sandbox
Windows-safe
"""

import ast
import sys
import os
import multiprocessing as mp
import builtins

# ======================================================
# SECURITY CONFIGURATION
# ======================================================

DANGEROUS_MODULES = {
    "os": 9,
    "sys": 6,
    "subprocess": 10,
    "shutil": 9,
    "socket": 9,
    "requests": 8,
    "urllib": 8,
    "ctypes": 10,
}

DANGEROUS_FUNCTIONS = {
    "eval": 10,
    "exec": 10,
    "compile": 7,
    "open": 6,
}

DANGEROUS_ATTRIBUTES = {
    ("os", "system"): 10,
    ("os", "remove"): 9,
    ("os", "rmdir"): 9,
    ("subprocess", "Popen"): 10,
    ("subprocess", "run"): 9,
}

SANDBOX_TIMEOUT = 10  # seconds

# ======================================================
# AST ANALYZER
# ======================================================

class SentinelAnalyzer(ast.NodeVisitor):
    def __init__(self, source_lines):
        self.issues = []
        self.score = 0
        self.source_lines = source_lines

    def add(self, severity, message, lineno):
        self.issues.append((severity, message, lineno))
        self.score += severity

    def get_code_snippet(self, lineno):
        if 0 < lineno <= len(self.source_lines):
            return self.source_lines[lineno - 1].strip()
        return "Unable to retrieve code snippet"

    def visit_Import(self, node):
        for n in node.names:
            root = n.name.split(".")[0]
            if root in DANGEROUS_MODULES:
                self.add(
                    DANGEROUS_MODULES[root],
                    f"Import of dangerous module '{root}'",
                    node.lineno
                )

    def visit_ImportFrom(self, node):
        if node.module:
            root = node.module.split(".")[0]
            if root in DANGEROUS_MODULES:
                self.add(
                    DANGEROUS_MODULES[root],
                    f"Import from dangerous module '{root}'",
                    node.lineno
                )

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id in DANGEROUS_FUNCTIONS:
                self.add(
                    DANGEROUS_FUNCTIONS[node.func.id],
                    f"Use of dangerous function '{node.func.id}()'",
                    node.lineno
                )

        if isinstance(node.func, ast.Attribute):
            mod = getattr(node.func.value, "id", None)
            if (mod, node.func.attr) in DANGEROUS_ATTRIBUTES:
                self.add(
                    DANGEROUS_ATTRIBUTES[(mod, node.func.attr)],
                    f"Dangerous call '{mod}.{node.func.attr}()'",
                    node.lineno
                )

        self.generic_visit(node)

# ======================================================
# AI HEURISTIC (SIMPLE)
# ======================================================

def ai_probability(code: str) -> int:
    score = 0
    for line in code.splitlines():
        if len(line.strip()) > 120:
            score += 2
    return min(100, score * 5)

# ======================================================
# SANDBOX EXECUTION
# ======================================================

def sandbox_exec_restricted(code: str):
    def blocked_open(*args, **kwargs):
        raise PermissionError("Filesystem access is blocked by CodeSentinel")

    real_import = __import__

    def safe_import(name, globals=None, locals=None, fromlist=(), level=0):
        root = name.split(".")[0]
        if root in DANGEROUS_MODULES:
            raise ImportError(f"Import of '{root}' is blocked by CodeSentinel")
        return real_import(name, globals, locals, fromlist, level)

    SAFE_BUILTINS = {
        "print": print,
        "input": input,
        "range": range,
        "len": len,
        "int": int,
        "float": float,
        "str": str,
        "bool": bool,
        "enumerate": enumerate,
        "abs": abs,
        "__import__": safe_import,
        "open": blocked_open,
    }

    try:
        exec(code, {"__builtins__": SAFE_BUILTINS}, {})
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"\n[!] SANDBOX ERROR: {type(e).__name__}: {e}\n")
        sys.exit(1)

def sandbox_exec_unrestricted(code: str):
    try:
        exec(code, {"__builtins__": builtins}, {})
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"\n[!] RUNTIME ERROR: {type(e).__name__}: {e}\n")
        sys.exit(1)

def run_sandbox(code: str, restricted=True):
    target = sandbox_exec_restricted if restricted else sandbox_exec_unrestricted
    p = mp.Process(target=target, args=(code,))
    p.start()
    p.join(SANDBOX_TIMEOUT)

    if p.is_alive():
        p.terminate()
        print("❌ Code exceeded time limit and was terminated")
        return False

    return p.exitcode == 0

# ======================================================
# ANALYSIS & REPORT
# ======================================================

def analyze_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    source_lines = code.splitlines()

    try:
        tree = ast.parse(code)
    except SyntaxError:
        print("❌ File contains syntax errors and cannot be analyzed.")
        return None, False

    analyzer = SentinelAnalyzer(source_lines)
    analyzer.visit(tree)

    risk = min(10, analyzer.score // 5)
    ai_score = ai_probability(code)

    print("\n🔱 CodeSentinel — REPORT\n")

    analyzer.issues.sort(key=lambda x: x[2])

    for sev, msg, lineno in analyzer.issues:
        level = "HIGH" if sev >= 8 else "MEDIUM" if sev >= 5 else "LOW"
        snippet = analyzer.get_code_snippet(lineno)
        print(f"[{level}] Line {lineno}: {msg}")
        print(f"  > {snippet}\n")

    print(f"🧮 Risk Score: {risk}/10")
    print(f"🤖 AI-generated probability: {ai_score}%")

    return code, risk > 0

# ======================================================
# CLI
# ======================================================

def main():
    if len(sys.argv) != 3:
        print("Usage: python codesentinel.py [scan|run] <file.py>")
        sys.exit(1)

    command, file = sys.argv[1], sys.argv[2]

    if not os.path.exists(file):
        print("❌ File not found")
        sys.exit(1)

    code, has_issues = analyze_file(file)
    if code is None:
        return

    if command == "scan":
        print("\n✅ Scan finished.")
        return

    if command == "run":
        print("-------------------------------------------------")
        print("⚠️  Restricted execution mode enabled by default")
        print("-------------------------------------------------\n")

        ok = run_sandbox(code, restricted=True)

        if ok:
            print("\n✅ Restricted execution completed safely")
        else:
            print("\n❌ Restricted execution blocked or failed")

        if has_issues:
            print("\n❗ HIGH-RISK CODE DETECTED")
            print("❗ Running with FULL ACCESS can harm your system")
            confirm = input("Type EXACTLY 'I UNDERSTAND' to run UNSAFE mode: ")

            if confirm == "I UNDERSTAND":
                print("\n🚨 RUNNING WITH FULL SYSTEM ACCESS 🚨\n")
                ok = run_sandbox(code, restricted=False)
                print("✅ Execution completed" if ok else "❌ Execution failed")
            else:
                print("Full access execution cancelled.")

if __name__ == "__main__":
    mp.freeze_support()
    main()
