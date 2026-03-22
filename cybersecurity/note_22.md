# 🔐 OS Security — Authentication, File Permissions & Malware

> **Source:** TryHackMe — Pre-Security / OS Security Module
> **Purpose:** Core security concepts through hands-on Linux practice
> **Covers:** CIA triad attacks, weak passwords, SSH, Linux commands,
> file permissions, malicious programs, ransomware

---

## 🧒 Feynman Explanation — Security as a House

Your computer is a house. Security is about three things:

- **Confidentiality** = only YOU can read your diary (no snooping)
- **Integrity** = nobody can change what's in your diary
- **Availability** = you can always access your diary when you need it

Three main ways attackers break into your house:

1. **Weak passwords** = you left a key under the doormat with a label saying "key"
2. **Weak file permissions** = you put your diary in a public library
3. **Malicious programs** = you let a wolf in dressed as a sheep

---

## 🔷 1. The CIA Triad — What Security Protects

```
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ CONFIDENTIALITY │  │    INTEGRITY    │  │  AVAILABILITY   │
├─────────────────┤  ├─────────────────┤  ├─────────────────┤
│ Only authorized │  │ Data is not     │  │ Systems/data    │
│ users can read  │  │ tampered with   │  │ accessible when │
│ the data        │  │ or modified     │  │ needed          │
├─────────────────┤  ├─────────────────┤  ├─────────────────┤
│ Attack:         │  │ Attack:         │  │ Attack:         │
│ Data theft,     │  │ File tampering, │  │ Ransomware,     │
│ credential      │  │ log deletion,   │  │ DDoS,           │
│ stealing        │  │ data corruption │  │ disk wipe       │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

---

## 🔷 2. Authentication & Weak Passwords

### Three Ways to Prove Identity

| Method                 | What It Is       | Example                       | Weakness                       |
| ---------------------- | ---------------- | ----------------------------- | ------------------------------ |
| **Something you KNOW** | Knowledge-based  | Password, PIN                 | Can be guessed, stolen, reused |
| **Something you ARE**  | Biometric        | Fingerprint, Face ID          | Can't be changed if stolen     |
| **Something you HAVE** | Possession-based | Phone (SMS OTP), hardware key | Can be lost, SIM swapped       |

### Why Passwords Are the Most Attacked

```
Passwords are the most common auth method → most attacked

Top 20 most common passwords (NCSC list):
  123456      password    123456789   12345678
  12345       1234567     password1   1234567890
  123123      000000      iloveyou    1234567891
  password2   1234567892  superman    123456789!
  qwerty123   dragon      monkey      letmein

"dragon" is #20 on the list!
→ In the task example, sammie used "dragon" as her password
→ Found on a STICKY NOTE at her desk
→ This is a real-world attack scenario

Attackers know:
  ✅ People use pet names, birthdates, favourite teams
  ✅ People reuse passwords across sites
  ✅ People use simple substitutions (p@ssw0rd)
  ✅ The 100,000 most common passwords are publicly known
  ✅ Most people never change default passwords
```

### 💻 Practical: SSH Login Attack

```bash
# What the attacker does:
# 1. Finds username (sammie — on sticky note)
# 2. Tries common passwords from the NCSC list
# 3. Gains access

# Step 1: Connect via SSH
ssh sammie@10.48.188.49

# Step 2: System asks for authenticity confirmation (first time only)
# "Are you sure you want to continue connecting (yes/no)?"
# Answer: yes

# Step 3: Enter password when prompted
# NOTE: You WON'T see anything typed — no stars, no dots
# The system still receives every character you type
sammie@10.48.188.49's password: [type dragon, nothing appears]

# Step 4: Successful login output
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-100-generic x86_64)
...
Last login: Tue Mar  1 09:46:11 2022

# Step 5: Confirm identity
sammie@beginner-os-security:~$ whoami
sammie

# Step 6: Look around
sammie@beginner-os-security:~$ ls
country.txt  draft.md  icon.png  password.txt  profile.jpg

# Step 7: Read files
sammie@beginner-os-security:~$ cat password.txt
# Reveals passwords!

sammie@beginner-os-security:~$ cat draft.md
# Operating System Security
# Reusing passwords means your password for other sites
# becomes exposed if one service is hacked.
# (ironic — she IS reusing passwords!)

# Step 8: Check command history (gold mine for attackers!)
sammie@beginner-os-security:~$ history
# Shows every command the user has run before
# May reveal other servers, passwords typed in commands, etc.
```

### Switching Users Without Logging Out

```bash
# If already logged in, switch to another user
su - johnny
# Enter johnny's password when prompted

# Try common passwords:
su - johnny
Password: password     # try 1
su - johnny
Password: 123456       # try 2
su - johnny
Password: johnny       # try 3 (username as password!)
su - johnny
Password: dragon       # try 4 (same as sammie?)

# Why attackers try the same password:
# Password REUSE is extremely common
# If sammie uses "dragon", maybe others do too
```

---

## 🔷 3. Weak File Permissions

### Principle of Least Privilege

```
Definition: Every user, process, and system should have
the MINIMUM permissions needed to do their job — nothing more.

Real example:
  A cashier at a store can:
    ✅ Scan items
    ✅ Accept payment
    ❌ Access the safe
    ❌ View employee salary records
    ❌ Change product prices

On a computer:
  A web server process should:
    ✅ Read web files in /var/www/html
    ❌ Read /etc/shadow (password hashes)
    ❌ Write to system files
    ❌ Execute programs as root
```

### How Weak Permissions Attack CIA

```
CONFIDENTIALITY ATTACK:
  File should be: readable only by owner
  File is actually: readable by everyone (world-readable)

  Result: Attacker reads your private files

  Example:
    chmod 777 salary.txt    → ANYONE can read salary data!
    -rw------- salary.txt   → CORRECT: only owner reads it

INTEGRITY ATTACK:
  File should be: writable only by owner
  File is actually: writable by everyone (world-writable)

  Result: Attacker modifies your files

  Example:
    chmod 777 /etc/passwd   → ANYONE can add root accounts!
    -rw-r--r-- /etc/passwd  → CORRECT: only root writes it
```

### 💻 File Permission Commands

```bash
# See file permissions
ls -la

# Permission string breakdown:
# -rw-r--r-- 1 sammie sammie 100 Mar 1 2022 salary.txt
#  │││└┬┘└┬┘
#  │││ │  └── Other: r-- = read only
#  │││ └───── Group: r-- = read only
#  ││└──────── Owner: rw- = read + write
#  │└───────── File type: - = regular file
#  └────────── (implicit: d = directory)

# Change permissions
chmod 600 private.txt    # only owner can read/write (private!)
chmod 644 public.txt     # owner r/w, others read only
chmod 755 script.sh      # owner all, others can execute

# DANGEROUS permissions to look for:
find / -perm -o+w -type f 2>/dev/null   # world-writable files
find / -perm -o+r /etc/shadow 2>/dev/null  # readable shadow!

# Real attack — if /etc/passwd is world-writable:
echo "hacker:x:0:0:root:/root:/bin/bash" >> /etc/passwd
# This adds a ROOT user → full system compromise!
```

### Key Sensitive Files and Their Correct Permissions

```bash
# These MUST be protected
/etc/shadow        -rw-r----- root shadow   # password hashes
/etc/sudoers       -r--r----- root root     # sudo config
~/.ssh/id_rsa      -rw------- user user     # private SSH key
~/.bash_history    -rw------- user user     # command history

# Check if shadow is too permissive:
ls -la /etc/shadow
# Should show: -rw-r----- (only root + shadow group)
# BAD:          -rw-r--r-- (world-readable = GAME OVER)

# If world-readable:
cat /etc/shadow
# Returns ALL users' password hashes → crack offline with hashcat!
```

---

## 🔷 4. Malicious Programs

### Types of Malware and Which CIA Attribute They Attack

| Malware Type     | CIA Attack                  | What It Does                                    | Example                      |
| ---------------- | --------------------------- | ----------------------------------------------- | ---------------------------- |
| **Trojan Horse** | Confidentiality + Integrity | Looks legitimate, gives attacker remote access  | RAT (Remote Access Trojan)   |
| **Ransomware**   | Availability                | Encrypts all your files, demands payment        | WannaCry, REvil, LockBit     |
| **Spyware**      | Confidentiality             | Secretly monitors and sends your data           | Keyloggers, screen recorders |
| **Rootkit**      | All three                   | Hides itself in the OS, gives persistent access | LoJax (UEFI rootkit)         |
| **Worm**         | Availability                | Spreads through networks, consumes resources    | Morris Worm, Blaster         |
| **Adware**       | Confidentiality             | Tracks browsing, serves targeted ads            | Browser hijackers            |
| **Cryptominer**  | Availability                | Uses your CPU/GPU to mine cryptocurrency        | XMRig (installed covertly)   |

### How Each Attack Works

```
TROJAN HORSE:
  User downloads "free_game_cracked.exe"
  → Actually installs a RAT (Remote Access Trojan)
  → Attacker now has remote shell into the machine
  → Can read files (confidentiality) AND modify them (integrity)
  → Looks like a normal game to the user

RANSOMWARE (Attacks AVAILABILITY):
  Malware runs on system
  → Scans all drives for documents, images, databases
  → Encrypts every file with attacker's key
  → README_DECRYPT.txt appears: "Pay 1 BTC to restore files"
  → Without decryption key → files are unreadable gibberish
  → Availability DESTROYED — you can't use your own data
  → Pay ransom → maybe get key, maybe don't

Real impact:
  WannaCry (2017) → hit 230,000 systems in 150 countries
  UK NHS hospitals shut down, operations cancelled
  Cost: ~$4 billion globally

HOW TO PROTECT AGAINST RANSOMWARE:
  ✅ Regular offline backups (3-2-1 rule)
  ✅ Keep OS and apps patched
  ✅ Don't open suspicious email attachments
  ✅ Use EDR/antivirus
  ✅ Principle of least privilege (limits spread)
  ✅ Network segmentation (limits lateral movement)
```

---

## 🔷 5. The Full Linux Recon Workflow

### Commands from This Module

```bash
# ── AUTHENTICATION CHECK ──────────────────────────────────────────

# Who am I?
whoami
# sammie

# Detailed identity (groups reveal privilege escalation paths!)
id
# uid=1001(sammie) gid=1001(sammie) groups=1001(sammie)

# ── REMOTE ACCESS ─────────────────────────────────────────────────

# Connect to remote system via SSH
ssh username@IP_ADDRESS
ssh sammie@10.48.188.49

# Switch to another user locally
su - johnny
su - linda

# ── FILE EXPLORATION ──────────────────────────────────────────────

# What files are here?
ls
# country.txt  draft.md  icon.png  password.txt  profile.jpg

# Read a file
cat password.txt
cat draft.md
cat country.txt

# Read sensitive system files (if permissions allow!)
cat /etc/passwd      # user accounts
cat /etc/shadow      # password hashes (root only normally)
cat /etc/hosts       # local DNS

# ── HISTORY MINING ────────────────────────────────────────────────

# What has this user been doing?
history
# Shows all previous commands
# May reveal:
#   - SSH connections to other servers (and their IPs!)
#   - Passwords typed accidentally in commands
#   - Scripts they've run
#   - Files they've edited

# Clear history (attackers do this to cover tracks)
history -c           # clear current session history
cat /dev/null > ~/.bash_history  # wipe history file
```

### The Attack Kill Chain (This Module)

```
STEP 1: RECONNAISSANCE
  Attacker visits office → sees sticky note: "sammie / dragon"
  Social engineering discovery of credentials

STEP 2: INITIAL ACCESS
  ssh sammie@10.48.188.49
  Password: dragon (from sticky note)
  → LOGGED IN as sammie

STEP 3: DISCOVERY
  whoami     → confirm access as sammie
  ls         → see what files exist
  history    → see what commands sammie has run
  cat *.txt  → read files (confidentiality breach!)

STEP 4: PRIVILEGE ESCALATION
  su - johnny → try common passwords for next user
  su - linda  → try common passwords for next user

  If any account has sudo:
  sudo -l    → what can this user run as root?
  sudo /bin/bash → become root!

STEP 5: IMPACT
  As root: full system access
  Read /etc/shadow → crack all passwords
  Modify /etc/passwd → add backdoor root account
  Install malware → persistence
  Encrypt files → ransomware
```

---

## 🔷 6. Key Security Lessons — What This Room Teaches

### Authentication Best Practices

```
❌ BAD habits (what sammie, johnny, linda do):
  - Using common passwords (dragon, password, 123456)
  - Writing passwords on sticky notes
  - Reusing the same password across accounts
  - Using personal info (birthdate, pet name)

✅ GOOD habits:
  - Use a password manager (Bitwarden, KeePass)
  - Unique password per account (auto-generated)
  - 16+ character random passwords
  - Enable MFA (Multi-Factor Authentication)
  - Never write passwords physically

Password strength rule of thumb:
  "dragon"          → cracked in < 1 second
  "dr@g0n"          → cracked in < 1 minute (substitutions known)
  "correct-horse-battery-staple" → centuries (passphrase!)
  "Kx9#mP2$vL8@nQ5!" → practically uncrackable (random 16 chars)
```

### File Permission Best Practices

```
Always ask: "Who ACTUALLY needs access to this?"
  Public website files  → world-readable is OK
  Config with passwords → owner-only (600)
  SSH private keys      → owner-only (600) MANDATORY
  Scripts               → owner executable (700 or 755)
  /etc/shadow           → root + shadow group only (640)

Audit permissions regularly:
  find / -perm -o+w 2>/dev/null   # world-writable (BAD!)
  find / -perm -4000 2>/dev/null  # SUID (check each one!)
  ls -la ~                         # check your own files
```

### Malware Prevention

```
Defense in depth — multiple layers:
  Layer 1: Don't click suspicious links/attachments
  Layer 2: Keep OS and apps patched (patch Tuesday!)
  Layer 3: Use antivirus/EDR
  Layer 4: Regular offline backups (3-2-1 rule)
  Layer 5: Least privilege (limits blast radius)
  Layer 6: Network segmentation (limits spread)
  Layer 7: MFA (even if password stolen, can't login)

3-2-1 Backup Rule:
  3 copies of data
  2 different storage media
  1 copy offsite (not connected to main network)
  → Ransomware can only encrypt what it can REACH
```

---

## 🔗 Security Attack Map

| Weakness             | Attack Type                      | CIA Impacted    | Prevention                      |
| -------------------- | -------------------------------- | --------------- | ------------------------------- |
| Weak password        | Brute force, credential stuffing | Confidentiality | Strong unique passwords + MFA   |
| Password reuse       | Credential stuffing              | Confidentiality | Unique password per account     |
| Sticky note password | Physical snooping                | Confidentiality | Use password manager            |
| World-readable files | Unauthorized access              | Confidentiality | chmod 600/640 sensitive files   |
| World-writable files | Data tampering                   | Integrity       | chmod 644/755 at most           |
| Trojan horse         | Remote access, data theft        | C + I           | Don't run untrusted executables |
| Ransomware           | File encryption                  | Availability    | Offline backups + patching      |
| Command history      | Credential discovery             | Confidentiality | `HISTCONTROL=ignorespace`       |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### SSH — Why It's Critical for Security

```bash
# SSH = Secure Shell
# Encrypted remote terminal access (replaced Telnet)
# Port 22 by default

# SSH is used for:
  ✅ Remote server administration
  ✅ Secure file transfer (SFTP/SCP)
  ✅ Tunneling other protocols
  ✅ Automated scripts and deployments

# SSH authentication methods:
  1. Password (vulnerable to brute force)
  2. SSH key pair (MUCH stronger — recommended!)
     Public key on server
     Private key on client
     No password needed, cryptographically secure

# Generate SSH key pair:
ssh-keygen -t ed25519 -C "your@email.com"
# Creates: ~/.ssh/id_ed25519 (PRIVATE — never share!)
#          ~/.ssh/id_ed25519.pub (public — put on servers)

# Copy public key to server:
ssh-copy-id user@server

# Now login without password!
ssh user@server  # uses key automatically
```

### The `history` Command — Attacker's Gold Mine

```bash
# History file location
cat ~/.bash_history

# Common finds in history files:
ssh admin@192.168.1.50 -p 2222          # other servers!
mysql -u root -p'SuperSecret123'         # DB password in command!
scp backup.tar.gz admin@10.0.0.1:/data  # internal IP + creds
curl -u admin:password123 https://api    # API credentials
git clone https://user:token@github.com  # Git tokens

# Protect your history:
# Prevent a command from being saved (prepend space)
 ssh user@sensitive-server    # space at start = not saved
# Or: export HISTCONTROL=ignorespace

# Clear history (attacker covers tracks this way):
history -c && cat /dev/null > ~/.bash_history
```

---

_Notes compiled from TryHackMe — OS Security Module_
_Enriched with attack kill chains, prevention strategies, and real-world examples_
