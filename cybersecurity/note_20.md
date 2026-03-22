# 🐧 Linux CLI Fundamentals — Navigation, Files & System Info

> **Source:** TryHackMe — Pre-Security / Linux Fundamentals Module
> **Purpose:** Linux terminal mastery for cybersecurity
> **Covers:** pwd, ls, cd, find, cat, whoami, uname, df, /etc files,
> hidden files, filesystem navigation, system recon commands

---

## 🧒 Feynman Explanation — The Terminal as a Map

Imagine you wake up in an unknown city with no visual GPS —
only a radio. You can ask questions and get answers:

- "Where am I?" → `pwd`
- "What's around me?" → `ls`
- "Walk to the next street" → `cd Documents`
- "Go back" → `cd ..`
- "Find a specific building" → `find ~ -name mission_brief.txt`
- "Read the sign on the door" → `cat mission_brief.txt`

The terminal gives you COMPLETE control of the system through
text. Every click in a GUI is just a command running underneath.
Learning the CLI means learning the actual language of the OS.

---

## 🔷 1. Step 1 — "Where Am I?" → `pwd`

```bash
ubuntu@tryhackme:~$ pwd
/home/ubuntu
```

**`pwd` = Print Working Directory**

```
Tells you the FULL path of where you currently are
in the filesystem.

Reading a path:
  /home/ubuntu
  │     └── folder named "ubuntu" (your home folder)
  └── folder named "home" (where all user homes live)

  / = root of the entire filesystem (the very top)

Think of it like your GPS coordinates on the map.
Without pwd, you're navigating blind.
```

---

## 🔷 2. Step 2 — "What's Around Me?" → `ls`

### Basic `ls`

```bash
ubuntu@tryhackme:~$ ls
Desktop    Downloads  Pictures  Templates  logs
Documents  Music      Public    Videos     projects
```

Lists all visible files and folders in the current directory.

### `ls -l` — Detailed View

```bash
ubuntu@tryhackme:~$ ls -l
total 44
drwxr-xr-x 2 ubuntu ubuntu 4096 Feb 27  2022 Desktop
drwxr-xr-x 6 ubuntu ubuntu 4096 Dec 11 12:45 Documents
drwxr-xr-x 2 ubuntu ubuntu 4096 Feb 16  2024 Downloads
drwxr-xr-x 4 ubuntu ubuntu 4096 Dec 11 12:29 logs
drwxr-xr-x 5 ubuntu ubuntu 4096 Dec 11 12:29 projects
drwx------ 3 ubuntu ubuntu 4096 Sep 12  2024 snap
```

### Reading `ls -l` Output

```
drwxr-xr-x  2  ubuntu  ubuntu  4096  Dec 11  12:45  Documents
│            │  │       │       │     │               └── name
│            │  │       │       │     └── last modified
│            │  │       │       └── size in bytes
│            │  │       └── group owner
│            │  └── user owner
│            └── number of hard links
└── permissions (d=directory, -=file, l=symlink)
    rwxr-xr-x = owner:rwx  group:r-x  others:r-x
```

### `ls -al` — Show Hidden Files Too

```bash
ubuntu@tryhackme:~$ ls -al
total 144
drwxr-xr-x 24 ubuntu ubuntu 4096 Feb 10 10:48 .
drwxr-xr-x  3 root   root   4096 Feb 10 10:36 ..
-rw-------  1 ubuntu ubuntu  439 Feb 10 06:47 .Xauthority
-rw-rw-r--  1 ubuntu ubuntu    0 Sep 12  2024 .Xresources
-rw-r--r--  1 ubuntu ubuntu  111 Oct  3  2024 .apport-ignore.xml
```

**Hidden files in Linux start with a dot `.`**

```
.Xauthority    ← starts with dot = hidden
.Xresources    ← starts with dot = hidden
.bash_history  ← another classic hidden file!
.ssh/          ← hidden folder with SSH keys!

Why this matters for security:
  Malware LOVES hiding in dotfiles and dotfolders.
  A backdoor in ~/.bash_profile runs every time you login.
  SSH keys in ~/.ssh/ can give attackers persistent access.
  Always use ls -al during forensics and incident response!
```

### `ls` Flags Cheat Sheet

```bash
ls          # basic list
ls -l       # long format (permissions, owner, size, date)
ls -a       # show hidden files (dot files)
ls -al      # long format + hidden files (MOST USEFUL)
ls -lh      # human-readable file sizes (KB, MB, GB)
ls -lt      # sort by modification time (newest first)
ls -lS      # sort by file size (largest first)
ls -R       # recursive — show all subdirectories too
ls -la /etc # list a specific path without navigating there
```

---

## 🔷 3. Step 3 — "Move Around" → `cd`

```bash
# Go INTO a directory
ubuntu@tryhackme:~$ cd Documents
ubuntu@tryhackme:~/Documents$ pwd
/home/ubuntu/Documents

# Go BACK one level
ubuntu@tryhackme:~/Documents$ cd ..
ubuntu@tryhackme:~$ pwd
/home/ubuntu

# Go to root
cd /

# Go home (wherever you are)
cd ~
cd         # same as cd ~

# Go to an absolute path
cd /var/log

# Go to a relative path
cd ../Pictures    # one level up, then into Pictures

# Go to previous directory (toggle)
cd -
```

### Understanding Absolute vs Relative Paths

```
ABSOLUTE path (starts with /):
  cd /home/ubuntu/Documents    ← works from ANYWHERE
  cd /var/log/apache2          ← always the same destination

RELATIVE path (no leading /):
  cd Documents                 ← only works if Documents exists HERE
  cd ../Downloads              ← relative to current location

Pro tip: Use TAB to autocomplete paths!
  cd Doc[TAB] → cd Documents/
```

---

## 🔷 4. Step 4 — "Find a File" → `find`

```bash
# Basic syntax
find <starting_point> -name <filename>

# Find a file starting from home directory
ubuntu@tryhackme:~$ find ~ -name mission_brief.txt
/<REDACTED-PATH>/mission_brief.txt

# The command checks EVERY folder inside your home directory
# and returns the FULL PATH when found
```

### `find` — The Most Powerful Search Tool

```bash
# Find by name (exact)
find / -name "passwords.txt" 2>/dev/null

# Find by name (case insensitive)
find / -iname "*.log" 2>/dev/null

# Find by extension
find /home -name "*.sh"      # all shell scripts
find /tmp -name "*.exe"      # suspicious! .exe in /tmp?

# Find by type
find / -type f -name "*.conf"  # files only
find / -type d -name "logs"    # directories only

# Find by owner
find / -user root -type f 2>/dev/null

# Find by permissions (SUID — pentesting essential!)
find / -perm -4000 2>/dev/null       # SUID files
find / -perm -o+w -type f 2>/dev/null # world-writable files

# Find recently modified files (last 7 days)
find / -mtime -7 2>/dev/null

# Find large files (>100MB)
find / -size +100M 2>/dev/null

# Find AND execute command on results
find /tmp -name "*.sh" -exec cat {} \;

# Suppress permission denied errors
find / -name "secret*" 2>/dev/null
#                       ↑ redirect stderr to /dev/null
```

> ⚠️ **Pentesting power:** `find / -perm -4000 2>/dev/null`
> finds SUID binaries. Run results through GTFObins to find
> privilege escalation paths. This is one of the first commands
> run during a Linux privilege escalation attempt.

---

## 🔷 5. Step 5 — "Read a File" → `cat`

```bash
ubuntu@tryhackme:~/<REDACTED-PATH>$ cat mission_brief.txt
Great job finding your way around the terminal.

Your next assignment is to collect a small system report:
- Who you're logged in as
- The kernel version
- Total disk space
- The name of this Linux distribution

FLAG:<REDACTED>
```

### File Reading Commands Compared

```bash
# cat — print entire file to terminal
cat file.txt
cat /etc/os-release

# less — scroll through large files (q to quit)
less /var/log/syslog

# more — paginate (space = next page, q = quit)
more /var/log/auth.log

# head — first N lines (default 10)
head file.txt
head -20 file.txt      # first 20 lines

# tail — last N lines (default 10)
tail file.txt
tail -20 file.txt      # last 20 lines
tail -f /var/log/auth.log  # LIVE MONITORING (SOC essential!)
#      ↑ follow — updates in real time as file grows

# grep — search inside file
grep "password" file.txt
grep -i "error" /var/log/syslog     # case insensitive
grep -r "secret" /home/             # search recursively
grep -n "failed" auth.log           # show line numbers
grep -v "INFO" log.txt              # EXCLUDE lines with INFO
```

> 💡 **SOC analyst daily workflow:**
> `tail -f /var/log/auth.log | grep "Failed"` — live monitoring
> of failed SSH login attempts in real time.

---

## 🔷 6. System Recon Commands

### `whoami` — Who Are You?

```bash
ubuntu@tryhackme:~$ whoami
ubuntu
```

```bash
# More detailed identity info
id
# uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),
# 24(cdrom),27(sudo),30(dip),46(plugdev),116(lxd)

# Breakdown:
# uid=1000   → user ID (0 = root, 1-999 = system, 1000+ = regular users)
# gid=1000   → primary group ID
# groups=... → all groups this user belongs to
# sudo       → THIS USER CAN RUN SUDO COMMANDS!
# lxd        → this user can manage containers (potential privesc!)
```

> ⚠️ **Pentesting:** After getting a shell, immediately run
> `id` to see group memberships. Being in `sudo`, `docker`,
> `lxd`, or `disk` groups can all lead to root escalation.

### `uname -a` — System Information

```bash
ubuntu@tryhackme:~$ uname -a
Linux tryhackme <KERNEL-VERSION>-aws #17-Ubuntu SMP Mon Sep 2
13:48:07 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
```

**Breakdown of `uname -a` output:**

```
Linux        → kernel name (this is a Linux system)
tryhackme    → hostname (computer's name on the network)
<VERSION>    → kernel version (search CVEs for this!)
-aws         → compiled for AWS environment
#17-Ubuntu   → build number
SMP          → Symmetric Multi-Processing (multi-core)
Mon Sep 2    → kernel compilation date
UTC 2024     → timezone and year
x86_64       → CPU architecture (64-bit Intel/AMD)
GNU/Linux    → OS type (GNU tools + Linux kernel)
```

```bash
# Individual uname flags
uname        # just "Linux"
uname -s     # kernel name
uname -n     # hostname
uname -r     # kernel release (USE THIS FOR CVE SEARCHES!)
uname -m     # machine hardware (x86_64, aarch64)
uname -a     # ALL of the above
```

> ⚠️ **Pentest note:** `uname -r` gives the kernel version.
> Search `searchsploit linux kernel <version>` for local
> privilege escalation exploits. DirtyCow, DirtyPipe, and
> other kernel exploits are found this way.

### `df -h` — Disk Space

```bash
ubuntu@tryhackme:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        --G   12G   --G  17% /
tmpfs           1.9G     0  1.9G   0% /dev/shm
tmpfs           774M  1.2M  773M   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
```

**Reading `df -h` output:**

```
Filesystem    → the storage device or virtual filesystem
Size          → total capacity
Used          → space consumed
Avail         → free space remaining
Use%          → percentage full
Mounted on    → where it lives in the directory tree

Key filesystems:
  /dev/root or /dev/sda1 → your actual hard drive
  tmpfs                  → temporary storage in RAM (fast, volatile)
  /dev/shm               → shared memory (inter-process communication)

-h flag = "human readable" = shows KB/MB/GB instead of raw bytes
```

```bash
# More disk commands
df -h              # all filesystems, human readable
df -h /            # just the root filesystem
du -sh /home       # disk USAGE of a specific directory
du -sh /*          # size of each top-level directory
du -sh /var/log/*  # find which log files are largest
lsblk              # show block devices (physical disks)
```

---

## 🔷 7. Reading System Files in `/etc`

### The `/etc` Directory

```
/etc = "etcetera" = configuration files for the entire system

Contents:
  os-release   → Linux distribution information
  passwd       → user account information (no passwords!)
  shadow       → password hashes (root only!)
  hosts        → local DNS overrides
  hostname     → this machine's hostname
  resolv.conf  → DNS server configuration
  fstab        → filesystem mount configuration
  crontab      → system-wide scheduled tasks
  sudoers      → who can run sudo and what commands
  ssh/         → SSH server configuration
  network/     → network interface configuration
  nginx/       → nginx web server config (if installed)
  apache2/     → apache web server config (if installed)
```

### `/etc/os-release` — Linux Distro Info

```bash
ubuntu@tryhackme:/etc$ cat os-release
PRETTY_NAME="Ubuntu 24.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.1 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
```

### Critical `/etc` Files for Security

```bash
# User accounts (no passwords stored here)
cat /etc/passwd
# Format: username:x:uid:gid:comment:home:shell
# root:x:0:0:root:/root:/bin/bash
# ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash

# Password hashes (root access needed!)
sudo cat /etc/shadow
# Format: username:$hash_type$salt$hash:...
# $6$ = SHA-512 (modern, strong)
# $1$ = MD5 (old, weak, crackable!)

# Find users with login shells (potential accounts to target)
grep "/bin/bash\|/bin/sh" /etc/passwd

# Local DNS overrides (hosts file attacks!)
cat /etc/hosts

# DNS server config
cat /etc/resolv.conf

# Who can use sudo?
cat /etc/sudoers
sudo -l          # what can CURRENT USER run as sudo?

# SSH config
cat /etc/ssh/sshd_config
# PermitRootLogin yes → VERY BAD — root can login via SSH!
# PasswordAuthentication yes → brute force possible!
```

---

## 🔷 8. Complete Linux CLI Cheat Sheet

```bash
# ── WHERE AM I & WHAT'S HERE ──────────────────────────────────────
pwd                    # current directory
ls                     # list visible files
ls -al                 # list ALL files including hidden
ls -lh                 # list with human-readable sizes
ls -lt                 # list sorted by time (newest first)

# ── NAVIGATION ────────────────────────────────────────────────────
cd Documents           # go into Documents
cd ..                  # go up one level
cd ~                   # go to home directory
cd /var/log            # go to absolute path
cd -                   # go to previous directory

# ── READING FILES ─────────────────────────────────────────────────
cat file.txt           # print entire file
head -20 file.txt      # first 20 lines
tail -20 file.txt      # last 20 lines
tail -f logfile.log    # live monitor (real-time)
less bigfile.txt       # scroll through large file
grep "keyword" file    # search inside file
grep -r "keyword" /    # search recursively

# ── FINDING FILES ─────────────────────────────────────────────────
find ~ -name "*.txt"           # find by name in home
find / -name "config" 2>/dev/null  # find system-wide
find / -perm -4000 2>/dev/null     # find SUID binaries

# ── SYSTEM INFO ───────────────────────────────────────────────────
whoami                 # current username
id                     # user ID, group memberships
uname -a               # full system info
uname -r               # kernel version only
hostname               # machine name
uptime                 # how long system has been running
df -h                  # disk space usage
free -h                # RAM usage
top / htop             # live process monitor

# ── NETWORK ───────────────────────────────────────────────────────
ip a                   # network interfaces and IPs
ss -tulnp              # open ports and listening services
netstat -tulnp         # same (older command)
ping 8.8.8.8           # test internet connectivity
curl -I https://site.com  # HTTP headers

# ── KEY SYSTEM FILES ──────────────────────────────────────────────
cat /etc/os-release    # distro name and version
cat /etc/passwd        # user accounts
cat /etc/hosts         # local DNS entries
cat /etc/resolv.conf   # DNS server
uname -r               # kernel version
```

---

## 🔗 Security Use Cases — Every Command Above

| Command                     | Security Scenario                                                    |
| --------------------------- | -------------------------------------------------------------------- |
| `ls -al`                    | Find hidden malware files (dotfiles), SSH keys, suspicious scripts   |
| `find / -perm -4000`        | Locate SUID binaries for privilege escalation                        |
| `find / -mtime -1`          | Find files modified in last 24hrs (incident response)                |
| `cat /etc/passwd`           | Enumerate all user accounts                                          |
| `cat /etc/shadow`           | Extract password hashes for offline cracking                         |
| `tail -f /var/log/auth.log` | Live monitor SSH brute force attempts                                |
| `grep -r "password" /var`   | Search logs for exposed credentials                                  |
| `id`                        | Check if current user is in sudo/docker/lxd groups                   |
| `uname -r`                  | Get kernel version → search for local privilege escalation exploits  |
| `df -h`                     | Check if disk is full (could indicate log tampering or crypto miner) |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### The Terminal Prompt — Reading It

```
ubuntu@tryhackme:~$
│       │         │└── $ = regular user, # = root (!)
│       │         └── ~ = current directory (~ = home)
│       └── hostname (machine name)
└── username

ubuntu@tryhackme:/etc$    → you're in /etc
root@victim:/tmp#          → you're ROOT in /tmp (attacker's dream!)
```

### The Most Important Directories for Security Work

```
/etc/          → all system configs (passwords, network, services)
/var/log/      → all system logs (auth.log, syslog, kern.log)
/tmp/          → temp files — world-writable, malware often drops here
/home/         → user data — documents, SSH keys, history
/root/         → root's home — most sensitive
/proc/         → live process information (check /proc/<PID>/cmdline)
/dev/          → device files (/dev/mem, /dev/sda)
/usr/bin/      → user executables
/usr/local/bin → custom installed tools
```

### One-Liner System Recon Script

```bash
#!/bin/bash
# Quick system recon — run when you first access a Linux machine
echo "=== IDENTITY ==="
id; whoami

echo "=== SYSTEM INFO ==="
uname -a
cat /etc/os-release | grep PRETTY

echo "=== DISK USAGE ==="
df -h | grep -v tmpfs

echo "=== NETWORK ==="
ip a | grep "inet "
ss -tulnp

echo "=== LOGGED IN USERS ==="
who; w

echo "=== RECENT LOGINS ==="
last -10

echo "=== SUDO ACCESS ==="
sudo -l 2>/dev/null

echo "=== SUID BINARIES ==="
find / -perm -4000 2>/dev/null

echo "=== CRON JOBS ==="
crontab -l 2>/dev/null
cat /etc/crontab
```

---

_Notes compiled from TryHackMe — Linux Fundamentals Module_
_Enriched with security use cases, pentesting commands, and practical workflows_
