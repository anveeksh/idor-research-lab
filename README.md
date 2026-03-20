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

## 🧑‍💻 Author & Credits
**Developed by:**
**👨‍💻 Anveeksh Mahesh Rao**
**Cybersecurity Engineer | Founder of Cyber Tech Associates | Researcher | Educator**
### Who is Anveeksh Mahesh Rao
Anveeksh Mahesh Rao is a passionate Cybersecurity Professional, Cyber Crime Investigator, and Entrepreneur with expertise spanning digital forensics, vulnerability assessment, penetration testing, and cybersecurity education.

He is the Founder and Managing Director of Cyber Tech Associates, a firm providing end-to-end cybersecurity consulting, training, and digital investigation services. Under his leadership, Cyber Tech Associates has trained and empowered over 10,000 students, professionals, and institutions across India through workshops, seminars, and awareness programs on Cyber Crime Investigation and Cyber Forensics.

Anveeksh holds a B.Tech in Cyber Security and Cyber Forensics from Srinivas University and professional certifications including CISCO CCST. His career reflects a balance between technical expertise and strategic leadership, making him a driving force in cybersecurity innovation and education.

He has served as Guest Faculty and Keynote Speaker at numerous universities and organizations, inspiring the next generation of cybersecurity professionals through real-world insights and practical skill development.

Beyond technology, Anveeksh is also a motivational speaker and mentor, using his platform to share stories of career growth, entrepreneurship, and digital safety awareness.

📍 LinkedIn: www.linkedin.com/in/anveekshmrao

📧 Email: raoanveeksh@gmail.com

🌐 Website: www.anveekshmrao.com

## 🏁 License
This project is released under the MIT License — free for research, academic, and authorized commercial use.
```bash
MIT License © 2025 Anveeksh Mahesh Rao
Permission is granted to use, copy, modify, and distribute this software for lawful, authorized purposes only.
```

## ⚠️ Disclaimer
Use as decision support; always validate mappings with a qualified ISO 27001 auditor/lead implementer.

