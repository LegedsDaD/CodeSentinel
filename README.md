## 🔱 CodeSentinel

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![Security](https://img.shields.io/badge/Security-Sandboxed-critical)
![Static Analysis](https://img.shields.io/badge/Analysis-AST--Based-orange)
![Safe Execution](https://img.shields.io/badge/Execution-Restricted-important)
![AI Ready](https://img.shields.io/badge/AI-Code%20Inspection-purple)
![Offline](https://img.shields.io/badge/Offline-100%25-success)
![No API](https://img.shields.io/badge/External%20APIs-None-blue)
![Multiprocessing](https://img.shields.io/badge/Isolation-Multiprocessing-yellow)
![Timeout Protected](https://img.shields.io/badge/Timeout-Enforced-red)
![Windows Safe](https://img.shields.io/badge/Windows-Freeze%20Safe-0078D6?logo=windows)
![Single File](https://img.shields.io/badge/Architecture-Single%20File-blueviolet)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-success)
![CLI Tool](https://img.shields.io/badge/Interface-CLI-lightgrey)



CodeSentinel is a single-file, production-ready secure Python code analyzer and sandbox executor designed to safely inspect and execute untrusted or AI-generated Python code without risking system integrity.

It performs static AST analysis, assigns a risk score, applies heuristic AI probability checks, and runs code inside a time-limited, restricted sandbox before allowing optional full-access execution.

## 🚀 Features
> 🔍 Static Security Analysis

AST-based inspection (no execution required)

Detects:

Dangerous module imports (os, subprocess, socket, etc.)

Unsafe built-ins (eval, exec, compile, open)

High-risk attribute calls (os.system, os.remove, etc.)

Line-accurate reporting with code snippets

> 🧮 Risk Scoring System

Severity-weighted scoring model

Normalized 0–10 risk score

Automatically flags high-risk files

> 🤖 AI Heuristic Probability

Lightweight heuristic to estimate AI-generated code likelihood

Zero external APIs

Fully offline and deterministic

> 🧪 Secure Sandbox Execution

Runs code in a separate process

Enforced execution timeout

Restricted built-ins and blocked filesystem access

Dangerous imports disabled at runtime

Optional manual override for unrestricted execution

> 🪟 Windows-Safe by Design

Uses multiprocessing.freeze_support()

Compatible with Windows executables and frozen builds

## 📦 Installation

No dependencies required.

git clone https://github.com/yourusername/codesentinel.git
cd codesentinel


Python 3.8+ is required.

## 🛠 Usage
## 🔎 Scan a Python file (no execution)
>python codesentinel.py scan example.py


Output includes:

Detected issues

Severity levels

Line numbers and code snippets

Risk score

AI probability estimate

 ## ▶️ Run code safely (restricted sandbox)
>python codesentinel.py run example.py


By default:

Filesystem access is blocked

Dangerous modules are disabled

Execution is time-limited

🚨 Run with full system access (dangerous)

If high-risk issues are detected, CodeSentinel requires explicit confirmation:

Type EXACTLY 'I UNDERSTAND' to run UNSAFE mode:


This prevents accidental execution of malicious code.

📊 Example Output
[HIGH] Line 12: Import of dangerous module 'os'
  > import os

[HIGH] Line 25: Dangerous call 'os.remove()'
  > os.remove("important.txt")

🧮 Risk Score: 3/10
🤖 AI-generated probability: 0%

## 🔐 Security Model
Layer	Protection
Static Analysis	AST inspection
Runtime Sandbox	Isolated process
Built-ins	Whitelisted only
Imports	Blocked by policy
Timeout	Forced termination
Unsafe Mode	Manual confirmation

## ⚠️ Important:
No Python sandbox is perfectly secure. CodeSentinel is designed for risk reduction, not absolute isolation.


## 🧠 Use Cases

Reviewing AI-generated Python code

Executing code from untrusted sources

Teaching Python security concepts

Secure local code testing

Building higher-level AI agents or coding tools

## 📄 License

MIT License
You are free to use, modify, and distribute this software.

## ⭐ Future Enhancements (Planned)

JSON / SARIF report export

Custom security policies

Memory & CPU usage limits

Plugin-based analyzers

GUI and editor integrations

## 👤 Author

LegedsDaD

Independent Developer
