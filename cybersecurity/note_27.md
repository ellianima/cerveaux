This is the master summary for the Information Gathering & OSINT (Open Source Intelligence) phase of your journey. You can copy and paste this directly into your Markdown file to complete your "Hacker’s Encyclopedia."

---

## 🔍 OSINT & Information Gathering: The "Digital Private Eye"

OSINT is the art of collecting and analyzing data from publicly available sources to find vulnerabilities, map out targets, and verify the truth. In hacking, this is the "Passive Reconnaissance" phase where the target never knows you are watching.

---

## 🕵️ 1. The Core Philosophy: The "BS Detector"

Before you can hack, you must verify. Information on the internet is often biased, outdated, or intentionally fake (a "honeypot" for hackers).

- The 4 Pillars of Evaluation:
  - Source: Who wrote this? Are they reputable researchers or anonymous trolls?
  - Evidence: Does the claim show raw code/data, or just "scary" words?
  - Bias: Is the author trying to sell a product or push an agenda?
  - Corroboration: The "Rule of Three." If a major bug isn't reported by at least three independent sources, be skeptical.

---

## 🚀 2. The "Hacker's Search Engines"

Beyond Google, there are specialized engines that index the Physical World and the Deep Web.

| Tool         | Purpose                         | The "Loot"                                                          |
| ------------ | ------------------------------- | ------------------------------------------------------------------- |
| Shodan       | The "Search Engine for Things." | Finds webcams, routers, and power plants by their "Banners."        |
| Censys       | The "Infrastructure Map."       | Finds SSL certificates and "hidden" subdomains for large companies. |
| VirusTotal   | The "Malware Judge."            | Uses 70+ AV engines to check if a file's Hash is malicious.         |
| Google Dorks | "Advanced Search Operators."    | Finds leaked PDFs, Excel sheets with passwords, and open folders.   |

---

## 📑 3. The "Global Dictionaries" (Vulnerabilities & Exploits)

How do we turn a "Version Number" into a "Break-In"? We use these global databases:

- CVE (Common Vulnerabilities & Exposures): A unique ID number (e.g., `CVE-2014-0160`) for every known software flaw.
- Exploit-DB: The "Hardware Store" where you download the actual scripts (exploits) to take advantage of a CVE.
- GitHub: The "Public Library" where researchers post Proof-of-Concept (PoC) code for the latest bugs.

---

## 👥 4. Social Media & Human Recon

Humans are the "Weakest Link." A hacker uses social media to bypass technical firewalls.

- The "Secret Question" Trap: Posts about elementary schools, pet names, or first cars provide the answers to password-reset questions.
- The "Sock Puppet": Using a "Burner" identity and a disposable email to explore a target's network without linking it to your real identity.
- Username Scraping (`Sherlock`): Finding every platform a target uses by searching for their common handle across 300+ sites.

---

## 📖 5. The "Manuals" (Help Yourself)

A professional hacker doesn't memorize everything; they know how to find the Official Source of Truth.

- Linux `man` Pages: The built-in "Brain" of Kali. Every tool's instruction manual is just one command away (e.g., `man nmap`).
- Microsoft/Apache Docs: The gold standard for understanding how a system is _supposed_ to work—and finding where it fails.

---

## 🛠️ 6. Practical "OSINT" Tooling (Kali/Linux)

- `whois [domain]`: Finding the owner and "Age" of a website to verify its reputation.
- `dig [domain]`: Directly asking the DNS system for a server's "Real Address" to avoid phishing traps.
- `sha256sum [file]`: Creating a unique "Fingerprint" for a file to check it against VirusTotal.
- `searchsploit [service]`: Searching your local, offline copy of the Exploit-DB for known holes.

---

## ⚖️ 7. The Ethical Boundary: "Passive" vs. "Active"

- Passive Recon: Browsing Google, Shodan, and Social Media. You are silent and 100% legal.
- Active Recon: Running an Nmap scan or trying a login. You are "knocking on the door" and must have permission (Scope).

---
