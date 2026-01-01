<img width="1024" height="1024" alt="ChatGPT Image Jan 1, 2026, 06_17_28 PM" src="https://github.com/user-attachments/assets/3e35289c-a26a-422f-8afe-48532c69f6ca" />

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

## 🔱 CodeSentinel

CodeSentinel is a single-file, production-ready secure Python code analyzer and sandbox executor designed to safely inspect and execute untrusted or AI-generated Python code without risking system integrity.

It performs static AST analysis, assigns a risk score, applies heuristic AI probability checks, and runs code inside a time-limited, restricted sandbox before allowing optional full-access execution.

## 👀Demo
<img width="598" height="289" alt="image" src="https://github.com/user-attachments/assets/d4e9a584-480c-4100-b7d3-aeb9c9f5fbe3" />
<img width="683" height="553" alt="image" src="https://github.com/user-attachments/assets/1766dc29-a36f-4a72-94ea-deaf61d87614" />



## Glance Tables
> Feature Comparison

| Capability | Supported | Notes |
|-----------|----------|-------|
| AST-based static analysis | ✅ | No code execution required |
| Dangerous import detection | ✅ | os, subprocess, socket, etc. |
| Unsafe built-in detection | ✅ | eval, exec, compile, open |
| Attribute call detection | ✅ | os.system, os.remove, etc. |
| Risk scoring (0–10) | ✅ | Severity-weighted |
| AI heuristic probability | ✅ | Offline, no APIs |
| Restricted sandbox execution | ✅ | Isolated process |
| Execution timeout | ✅ | Prevents infinite loops |
| Full-access execution | ⚠️ | Requires manual confirmation |
| Internet access | ❌ | Fully offline by design |

> Security Layer Breakdown

| Layer | Protection Applied | Purpose |
|------|------------------|--------|
| Static Analysis | AST inspection | Detect risky code early |
| Runtime Isolation | Separate process | Prevent host contamination |
| Built-ins | Whitelisted only | Block file/system access |
| Imports | Policy-based blocking | Disable dangerous modules |
| Timeout | Forced termination | Stop infinite or hanging code |
| Unsafe Mode | Manual consent | Prevent accidental harm |

> Risk Severity mapping

| Severity Score | Level | Meaning |
|---------------|-------|--------|
| 0–2 | 🟢 LOW | Minimal or no risk |
| 3–4 | 🟡 MEDIUM | Potentially unsafe |
| 5–7 | 🟠 HIGH | Dangerous patterns detected |
| 8–10 | 🔴 CRITICAL | Immediate system risk |

> CLI Command Reference

| Command | Description | Executes Code |
|-------|-------------|---------------|
| scan <file.py> | Analyze code only | ❌ No |
| run <file.py> | Run in restricted sandbox | ✅ Yes (safe) |
| Unsafe override | Full access execution | ⚠️ Yes (dangerous) |

> Sandbox mode Comparison

| Feature | Restricted Mode | Unsafe Mode |
|-------|----------------|------------|
| Filesystem access | ❌ Blocked | ✅ Allowed |
| Dangerous imports | ❌ Blocked | ✅ Allowed |
| Built-ins | Whitelisted | Full Python |
| Timeout enforced | ✅ Yes | ❌ No |
| User confirmation | ❌ No | ✅ Required |
| System risk | 🟢 Low | 🔴 High |
> Ideal user profiles.

| User | How CodeSentinel Helps |
|----|-----------------------|
| AI Developers | Inspect AI-generated scripts |
| Security Researchers | Test unsafe code safely |
| Students | Learn Python security |
| Educators | Demonstrate sandboxing |
| Offline Users | Secure execution without internet |

> Roadmap Status

| Feature | Status |
|------|--------|
| Core analyzer | ✅ Complete |
| Restricted sandbox | ✅ Complete |
| Risk scoring | ✅ Complete |
| JSON report export | ⏳ Planned |
| Custom policies | ⏳ Planned |
| GUI interface | ⏳ Planned |
| PyPI package | ⏳ Planned |

> Community Engagement

| Action | Impact |
|-----|-------|
| ⭐ Star the repo | Helps visibility |
| 🐛 Report issues | Improves security |
| 🔧 Submit PRs | Grows the project |
| 📢 Share | Helps safe coding |


## 🚀 Features
> 🔍 Static Security Analysis

AST-based inspection (no execution required)

Detects:

1)Dangerous module imports (os, subprocess, socket, etc.)
2)Unsafe built-ins (eval, exec, compile, open)
3)High-risk attribute calls (os.system, os.remove, etc.)
4)Line-accurate reporting with code snippets

> 🧮 Risk Scoring System

1)Severity-weighted scoring model
2)Normalized 0–10 risk score
3.Automatically flags high-risk files

> 🤖 AI Heuristic Probability

1)Lightweight heuristic to estimate AI-generated code likelihood
2)Zero external APIs
3)Fully offline and deterministic

> 🧪 Secure Sandbox Execution

1)Runs code in a separate process
2)Enforced execution timeout
3)Restricted built-ins and blocked filesystem access
4)Dangerous imports disabled at runtime
5)Optional manual override for unrestricted execution

> 🪟 Windows-Safe by Design

1)Uses multiprocessing.freeze_support()
2)Compatible with Windows executables and frozen builds

## 📦 Installation

No dependencies required.

git clone https://github.com/LegedsDaD/codesentinel.git
cd codesentinel


Python 3.8+ is required.

## 🔎 Scan a Python file (no execution)
>python codesentinel.py scan example.py


Output includes:

>Detected issues
>Severity levels
>Line numbers and code snippets
>Risk score
>AI probability estimate

 ## ▶️ Run code safely (restricted sandbox)
>python codesentinel.py run example.py


By default:

>Filesystem access is blocked
>Dangerous modules are disabled
>Execution is time-limited

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
>Layer	Protection
>Static Analysis	AST inspection
>Runtime Sandbox	Isolated process
>Built-ins	Whitelisted only
>Imports	Blocked by policy
>Timeout	Forced termination
>Unsafe Mode	Manual confirmation

## ⚠️ Important:
No Python sandbox is perfectly secure. CodeSentinel is designed for risk reduction, not absolute isolation.


## 🧠 Use Cases

1)Reviewing AI-generated Python code
2)Executing code from untrusted sources
3)Teaching Python security concepts
4)Secure local code testing
5)Building higher-level AI agents or coding tools

## 📄 License

MIT License
You are free to use, modify, and distribute this software.

## ⏭ Future Enhancements (Planned)

1.JSON / SARIF report export
2.Custom security policies
3.Memory & CPU usage limits
4.Plugin-based analyzers
5.GUI and editor integrations

## ⭐ Star

If you find CodeSentinel useful don't forget to leave a star behind. Thank You

## 👤 Author

LegedsDaD
Independent Developer
