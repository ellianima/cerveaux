Here’s a **clean, structured, high-impact reviewer** you can paste directly into your markdown file 👇

---

# 🔐 CIA TRIAD & SECURITY MINDSET — REVIEWER

---

# 🧠 PART 1 — THE CIA TRIAD (CORE OF CYBERSECURITY)

## 📌 Definition

The **CIA Triad** is the **foundation of information security**, consisting of:

- **Confidentiality** → Protect data from unauthorized access
- **Integrity** → Ensure data is accurate and not altered
- **Availability** → Ensure systems and data are accessible when needed

> Think of it as:
>
> - Confidentiality = **Secrets stay secret**
> - Integrity = **Data stays correct**
> - Availability = **Systems stay usable**

---

# 🔒 1. CONFIDENTIALITY

## 📌 Definition

Ensures that **only authorized users can access sensitive information**

## 🧠 Intuition (Feynman Style)

Imagine your messages — only YOU and the intended receiver should read them.

If others can read it → confidentiality is broken.

## ⚙️ Mechanisms (How it's implemented)

- Encryption (AES, RSA)
- Authentication (passwords, biometrics)
- Authorization (RBAC — Role-Based Access Control)
- VPNs
- Data masking

## 💥 Attacks That Break It

- Packet sniffing (Wireshark 👀)
- Man-in-the-Middle (MITM)
- Phishing
- Credential stuffing

## 🏢 Real-World Example

- Banking systems encrypt transactions so hackers can't read them

## 🧰 Tools Used

- `Wireshark` → sniffing detection
- `OpenSSL` → encryption
- `Hashcat` → password cracking (attack perspective)

---

# 🧬 2. INTEGRITY

## 📌 Definition

Ensures data is **accurate, consistent, and not tampered with**

## 🧠 Intuition

If you send ₱1000 but it becomes ₱10,000 → integrity is broken.

## ⚙️ Mechanisms

- Hashing (SHA-256, MD5)
- Checksums
- Digital Signatures
- File Integrity Monitoring (FIM)

## 💥 Attacks That Break It

- Data tampering
- SQL Injection
- Malware modifying files

## 🏢 Real-World Example

- Software downloads use hashes to verify files aren’t modified

## 🧰 Tools Used

- `sha256sum` → verify file integrity
- `Tripwire` → integrity monitoring
- `Snort` → detect tampering attempts

---

# ⚡ 3. AVAILABILITY

## 📌 Definition

Ensures systems and data are **accessible when needed**

## 🧠 Intuition

If a website is DOWN → availability is broken.

## ⚙️ Mechanisms

- Load balancing
- Redundancy (backup servers)
- Failover systems
- Regular backups

## 💥 Attacks That Break It

- DDoS (Distributed Denial of Service)
- Hardware failure
- Ransomware

## 🏢 Real-World Example

- Cloud providers ensure 99.99% uptime

## 🧰 Tools Used

- `Nmap` → check open services
- `Nagios` → monitoring
- `Cloudflare` → DDoS protection

---

# ⚖️ CIA TRIAD TRADE-OFFS (IMPORTANT ⚠️)

You **CANNOT maximize all three perfectly**.

| Scenario          | Trade-off                    |
| ----------------- | ---------------------------- |
| Strong encryption | ↓ Performance (Availability) |
| Open systems      | ↓ Confidentiality            |
| Strict validation | ↓ Speed                      |

> 🔥 Real skill = balancing the triad depending on the system

---

# 🧠 PART 2 — THE SECURITY MINDSET

---

# 🧠 What is a Security Mindset?

## 📌 Definition

A way of thinking where you:

- **Assume systems can fail**
- **Think like an attacker**
- **Continuously question trust**

---

# 🧠 CORE PRINCIPLES

## 1. 🔍 Think Like an Attacker

Ask:

- “How can I break this?”
- “What’s the weakest point?”

### Example:

You see a login page → attacker sees:

- No rate limiting?
- Weak password policy?
- SQL injection?

---

## 2. ❌ Trust Nothing (Zero Trust)

> “Never trust, always verify”

- Don’t trust users
- Don’t trust devices
- Don’t trust internal networks

---

## 3. 🔓 Assume Breach

Even if system is secure:

- Act as if attacker is already inside

### Result:

- Monitor logs
- Detect anomalies
- Limit damage (segmentation)

---

## 4. 🔗 Attack Surface Awareness

## 📌 Definition

All possible entry points an attacker can exploit

### Examples:

- Open ports
- APIs
- Login forms
- Misconfigured servers

> 🔥 Reduce attack surface = reduce risk

---

## 5. 🧩 Defense in Depth

Layered security approach:

- Firewall
- IDS/IPS
- Antivirus
- Authentication
- Logging

> If one fails → others still protect

---

## 6. 🧠 Paranoia (Healthy, Not Irrational)

Always ask:

- “What if this fails?”
- “What if attacker is smarter than me?”

---

# 🧠 HOW PROFESSIONALS THINK (REAL INDUSTRY)

## SOC Analyst

- Monitors logs for anomalies
- Detects breaches early

## Pentester

- Simulates attacks
- Finds weaknesses BEFORE hackers

## Network Admin

- Secures infrastructure
- Maintains availability

---

# 🔄 MENTAL MODEL SUMMARY

| Concept          | Question You Should Ask  |
| ---------------- | ------------------------ |
| Confidentiality  | Who should NOT see this? |
| Integrity        | Can this be altered?     |
| Availability     | Can this be taken down?  |
| Security Mindset | How can this fail?       |

---

# 🧪 PRACTICE (TRAIN YOUR BRAIN)

## 🟢 Beginner

1. Identify CIA Triad in:
   - Login system
   - ATM machine

2. Ask:
   - What protects confidentiality here?

---

## 🟡 Intermediate

Analyze your own network:

- Run:

```bash
nmap -sn 192.168.1.0/24
```

Ask:

- Which devices expose risk?
- Which affect availability?

---

## 🔴 Advanced (Real Pentester Thinking)

Pick a website and ask:

- How would I:
  - Steal data? (Confidentiality)
  - Modify data? (Integrity)
  - Take it down? (Availability)

---

# 🧠 FINAL INSIGHT

> 🔥 “Cybersecurity is not about tools. It is about thinking.”

Tools:

- Nmap
- Wireshark
- Kali Linux

…but mindset is what makes you dangerous (in a good way 😈)

---
