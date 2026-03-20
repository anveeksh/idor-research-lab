# 🔐 IDOR Research Lab

> **Research Question:** How effective are automated scanners vs. manual testing in detecting IDOR vulnerabilities in REST APIs?

## 📌 Overview
A controlled testbed for studying Insecure Direct Object Reference (IDOR) vulnerabilities — one of the most critical access control flaws per OWASP API Security Top 10 (API1:2023).

## 🧪 What's Inside
- **Vulnerable Flask API** — 4 intentionally flawed endpoint groups
- **Custom Python Fuzzer** — sequential ID enumeration across all endpoints
- **Research Dataset** — 45 test cases, 27 confirmed IDOR findings (60% hit rate)
- **Findings Report** — auto-generated PDF via ReportLab

## 🗂️ IDOR Types Covered
| Type | Endpoint | Description |
|---|---|---|
| Horizontal Privilege Escalation | `/api/users/<id>` | User A reads User B's profile + SSN |
| Order Enumeration | `/api/orders/<id>` | Sequential ID exposes all orders |
| Document Access | `/api/docs/<id>` | File access without ownership check |
| Mass Assignment | `/api/profiles/<id>` | Parameter tampering escalates role |

## 📊 Fuzzer Results
| Endpoint | Tested | IDOR Found | Detection Rate |
|---|---|---|---|
| User Profiles | 15 | 9 | 100% |
| Orders | 15 | 9 | 100% |
| Documents | 15 | 9 | 100% |
| **Total** | **45** | **27** | **100%** |

## 🚀 Quick Start
```bash
git clone https://github.com/anveeksh/idor-research-lab.git
cd idor-research-lab
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cd vulnerable_app && python3 seed_data.py && python3 app.py
# New terminal:
cd fuzzer && python3 fuzzer.py
```

## ⚠️ Disclaimer
For educational and research purposes only. Run in isolated local environments.

## 👤 Author
**Anveeksh Rao** | MS Cybersecurity, Northeastern University
[anveekshmrao.com](https://anveekshmrao.com) · [GitHub](https://github.com/anveeksh)
Vulnerability Researcher @ CACTi Lab, Khoury College
