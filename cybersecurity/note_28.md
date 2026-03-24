# 🐧 Linux Fundamentals — Commands, Find, Grep & Operators

> **Source:** TryHackMe — Linux Fundamentals Module
> **Purpose:** Core Linux CLI skills for cybersecurity
> **Covers:** Where Linux is used, flavours, basic commands, find,
> grep, wc, operators (&, &&, >, >>), output redirection

---

## 🧒 Feynman Explanation — Linux Is Everywhere

You think you've never used Linux? You use it every day.
Every website you visit, every time you tap your card at a
checkout, every traffic light you pass — Linux is running
underneath. It's the invisible engine of the internet.

Learning Linux = learning to talk to the majority of the
world's computers in their native language.

---

## 🔷 1. Where Is Linux Used?

```
Linux powers:
  🌐 Websites you visit          (Apache/Nginx run on Linux)
  🚗 Car entertainment systems   (Android = Linux kernel)
  🏪 Point of Sale systems       (checkout tills, registers)
  🏭 Critical infrastructure     (traffic lights, industrial sensors)
  ☁️ Cloud computing             (AWS, GCP, Azure all run Linux)
  📱 Android phones              (Linux kernel underneath)
  🔬 Supercomputers              (100% of top 500 run Linux)
  🔒 Security tools              (Kali, Parrot — all Linux)

Fun fact: Ubuntu Server runs on as little as 512MB of RAM!
That's why it dominates servers — lightweight and powerful.
```

---

## 🔷 2. Flavours of Linux (Distributions)

```
"Linux" is actually an UMBRELLA TERM for many OS versions
called DISTRIBUTIONS (distros). They all share the same
Linux kernel but differ in packaging, GUI, and purpose.

┌─────────────────────────────────────────────────────────┐
│                    Linux Kernel                         │
│         (the core — manages hardware)                   │
├─────────┬──────────┬─────────┬──────────┬──────────────┤
│ Ubuntu  │ Debian   │  Kali   │  Arch    │   CentOS     │
│ Desktop │ Server   │Security │ Advanced │  Enterprise  │
│ & Server│ Stable   │ Testing │  Users   │  Servers     │
└─────────┴──────────┴─────────┴──────────┴──────────────┘

For this learning path: Ubuntu (most beginner-friendly,
massive community, runs well as both desktop and server)

Linux is open-source:
  Anyone can read the code
  Anyone can modify it
  Anyone can distribute their own version
  → This is why there are 600+ distros!
```

---

## 🔷 3. Basic Linux Commands — The Foundation

### First Commands

| Command  | Full Name               | What It Does                    |
| -------- | ----------------------- | ------------------------------- |
| `echo`   | echo                    | Output any text you provide     |
| `whoami` | who am I                | Show current logged-in username |
| `ls`     | listing                 | List files in current directory |
| `cd`     | change directory        | Navigate between folders        |
| `cat`    | concatenate             | Print file contents to terminal |
| `pwd`    | print working directory | Show your current location      |

### 💻 All Basic Commands in Action

```bash
# echo — print text to terminal
echo Hello World
# Output: Hello World

echo "I am learning Linux"
# Output: I am learning Linux

# whoami — who are you?
whoami
# Output: tryhackme

# pwd — where are you?
pwd
# Output: /home/tryhackme

# ls — what's here?
ls
# Output: Desktop  Documents  Pictures  folder1

# cd — move around
cd Documents
cd ..              # go back one level
cd ~               # go to home directory
cd /               # go to root

# cat — read a file
cat todo.txt
cat /etc/os-release
cat /etc/passwd    # interesting for security recon!
```

---

## 🔷 4. `find` — Search the Entire Filesystem

### 🧒 Feynman Explanation

`find` is like a search dog. You give it a scent (filename or
pattern) and it sniffs through every folder until it finds
every matching item — returning the exact location of each.

No more manually `cd`-ing into every folder looking for a file.

### Basic `find` Usage

```bash
# Find a specific file by exact name
find -name passwords.txt
# Output: ./folder1/passwords.txt

# Find from a specific starting directory
find /home -name passwords.txt

# Find from root (search ENTIRE system)
find / -name passwords.txt 2>/dev/null
```

### Using Wildcards with `find`

```bash
# Find ALL .txt files (wildcard *)
find -name *.txt
# Output:
# ./folder1/passwords.txt
# ./Documents/todo.txt

# Find all .log files
find / -name *.log 2>/dev/null

# Find all .config files (goldmine!)
find / -name *.config 2>/dev/null

# Find all .sh scripts
find / -name *.sh 2>/dev/null
```

### Advanced `find` (Security-Focused)

```bash
# Find SUID binaries (privilege escalation!)
find / -perm -4000 2>/dev/null

# Find world-writable files (misconfiguration!)
find / -perm -o+w -type f 2>/dev/null

# Find files owned by root
find / -user root -type f 2>/dev/null

# Find files modified in last 24 hours (incident response!)
find / -mtime -1 2>/dev/null

# Find files larger than 100MB
find / -size +100M 2>/dev/null

# Find by type
find / -type f -name "*.bak"   # files only
find / -type d -name "logs"    # directories only

# Find AND execute on results (very powerful!)
find /tmp -name "*.sh" -exec cat {} \;

# Suppress "Permission denied" errors
find / -name "secret*" 2>/dev/null
#                        ↑ redirect errors to /dev/null
```

---

## 🔷 5. `grep` — Search INSIDE Files

### 🧒 Feynman Explanation

`cat` shows you the whole book. `grep` is the index at the back —
you tell it what word you're looking for and it shows you
exactly which pages contain it. For a 244-page book (log file),
you don't read every page. You use the index.

### Basic `grep` Usage

```bash
# Search for a specific string inside a file
grep "81.143.211.90" access.log
# Output: 81.143.211.90 - - [25/Mar/2021:11:17 +0000]
#         "GET / HTTP/1.1" 200 417 "-" "Mozilla/5.0..."

# The file has 244 lines — grep finds your result instantly
# First check how many lines: wc -l
wc -l access.log
# Output: 244 access.log
```

### `grep` Flags

```bash
# Case insensitive search
grep -i "error" system.log

# Show line numbers
grep -n "failed" auth.log

# Invert match (show lines NOT containing word)
grep -v "INFO" app.log

# Count matching lines
grep -c "Failed password" auth.log

# Show context (2 lines before and after match)
grep -C 2 "error" logfile.log

# Search multiple files
grep "password" *.txt

# Recursive search through directories
grep -R "PRETTY_NAME" /etc/
# Output:
# grep: /etc/sudoers: Permission denied
# /etc/os-release:PRETTY_NAME="Ubuntu"
# Shows file path + matching line

# Recursive + case insensitive
grep -Ri "password" /var/www/html/
# Searches all web files for exposed passwords!
```

### 💻 Combining `find` + `grep` (Power Move)

```bash
# Find all .txt files then search inside each
find / -name "*.txt" 2>/dev/null -exec grep -l "password" {} \;

# Search ALL log files for failed logins
grep -R "Failed password" /var/log/ 2>/dev/null

# Search ALL config files for credentials
grep -Ri "password" /etc/ 2>/dev/null

# Find exposed API keys in web files
grep -Ri "api_key\|api_secret\|secret_key" /var/www/ 2>/dev/null

# SOC workflow: monitor live log for specific IP
tail -f /var/log/auth.log | grep "192.168.1.100"
```

---

## 🔷 6. Linux Operators — Powering Up the CLI

### Overview

| Operator | Name                 | What It Does                              |
| -------- | -------------------- | ----------------------------------------- |
| `&`      | Background           | Run command in background                 |
| `&&`     | AND                  | Run second command only if first succeeds |
| `>`      | Redirect (overwrite) | Send output to file (overwrites!)         |
| `>>`     | Redirect (append)    | Add output to end of file (safe)          |

---

### Operator `&` — Run in Background

```bash
# Without &: terminal is LOCKED until command finishes
cp huge_file.iso /backup/huge_file.iso
# (terminal frozen for 10 minutes)

# With &: terminal is FREE immediately
cp huge_file.iso /backup/huge_file.iso &
# [1] 12345   ← job number and PID
# Terminal immediately ready for next command!

# Other background examples
nmap -sV -p- 192.168.1.1 &   # run scan in background
python3 server.py &            # run server in background

# Check background jobs
jobs

# Bring background job to foreground
fg %1
```

---

### Operator `&&` — Chain Commands (Conditional)

```bash
# Run command2 ONLY IF command1 succeeds
command1 && command2

# Examples:
mkdir new_project && cd new_project
# Creates folder AND navigates into it
# If mkdir fails → cd is NEVER run

apt update && apt upgrade -y
# Updates package lists THEN upgrades
# If update fails → upgrade NEVER runs (prevents broken state)

git add . && git commit -m "update" && git push
# Stage → commit → push, ONLY if each step succeeds

# Contrast with single &:
# command1 & command2  → both run simultaneously
# command1 && command2 → command2 waits for command1 to succeed
```

---

### Operator `>` — Redirect Output (OVERWRITES)

```bash
# Send command output TO a file instead of terminal
echo hey > welcome
cat welcome
# Output: hey

# OVERWRITE example — BE CAREFUL!
echo hey > welcome    # welcome contains: hey
echo hello > welcome  # welcome now contains ONLY: hello
                      # "hey" is GONE!

# Practical uses:
# Save command output to file
ls -la > directory_listing.txt
systeminfo > system_info.txt
nmap 192.168.1.0/24 > scan_results.txt

# Create a file with content
echo "#!/bin/bash" > script.sh
echo "whoami" > quick_check.txt

# Save errors separately
command 2> errors.txt        # stderr to file
command > output.txt 2>&1    # BOTH stdout and stderr to file
```

---

### Operator `>>` — Redirect Output (APPENDS)

```bash
# Add output to END of file (does NOT overwrite!)
echo hey > welcome        # welcome: "hey"
echo hello >> welcome     # welcome: "hey" then "hello"

cat welcome
# Output:
# hey
# hello

# Practical uses:

# Build a file line by line
echo "Username: admin" >> credentials.txt
echo "Password: password123" >> credentials.txt
echo "Server: 192.168.1.1" >> credentials.txt

# Append scan results (run multiple scans, combine results)
nmap -p 80 192.168.1.0/24 >> all_scans.txt
nmap -p 443 192.168.1.0/24 >> all_scans.txt

# Logging
echo "[$(date)] System check completed" >> audit.log
```

---

## 🔷 7. `wc` — Word/Line Counter

```bash
# Count lines in a file
wc -l access.log
# Output: 244 access.log

# Count words
wc -w file.txt

# Count characters
wc -c file.txt

# Count all (lines, words, chars)
wc file.txt

# Combine with grep (count matching lines)
grep "Failed password" auth.log | wc -l
# → How many failed SSH attempts?

grep "error" app.log | wc -l
# → How many errors in the log?
```

---

## 🔷 8. Complete Reference — All Commands

```bash
# ── BASIC OUTPUT ──────────────────────────────────────────────────
echo "text"               # print text
echo $VARIABLE            # print variable value
whoami                    # current user

# ── NAVIGATION ────────────────────────────────────────────────────
pwd                       # where am I?
ls                        # what's here?
ls -al                    # all files + details
cd folder                 # move into folder
cd ..                     # go up one level
cd ~                      # go home

# ── READING FILES ─────────────────────────────────────────────────
cat file.txt              # print file
head -20 file.txt         # first 20 lines
tail -20 file.txt         # last 20 lines
tail -f file.txt          # live monitoring
wc -l file.txt            # count lines

# ── SEARCHING ─────────────────────────────────────────────────────
find -name "*.txt"                    # find by name
find / -perm -4000 2>/dev/null        # find SUID
grep "keyword" file.txt               # search in file
grep -R "keyword" /directory/         # recursive search
grep -Ri "password" /etc/ 2>/dev/null # case-insensitive recursive

# ── OPERATORS ─────────────────────────────────────────────────────
command &                 # run in background
cmd1 && cmd2              # run cmd2 only if cmd1 succeeds
echo "text" > file        # write to file (overwrites)
echo "text" >> file       # append to file (safe)
cmd > output.txt          # save output to file
cmd 2>/dev/null           # suppress error messages
cmd1 | cmd2               # pipe: send output of cmd1 to cmd2
```

---

## 🔗 Security Use Cases — Real Analyst Workflows

```bash
# ── SOC ANALYST ───────────────────────────────────────────────────

# Find all failed SSH logins
grep "Failed password" /var/log/auth.log

# Count brute force attempts per IP
grep "Failed password" /var/log/auth.log | \
  awk '{print $11}' | sort | uniq -c | sort -rn | head -20

# Live monitor for specific attacker IP
tail -f /var/log/auth.log | grep "192.168.1.100"

# Find suspicious files created today
find / -mtime 0 -type f 2>/dev/null

# Save scan output for report
nmap -sV target.com > nmap_results.txt 2>/dev/null

# ── PENTESTER ─────────────────────────────────────────────────────

# Find password files
find / -name "*password*" 2>/dev/null
find / -name "*.txt" 2>/dev/null | xargs grep -l "password"

# Find SUID for privilege escalation
find / -perm -4000 2>/dev/null

# Search config files for credentials
grep -Ri "password\|passwd\|secret\|key" /etc/ 2>/dev/null

# Find world-writable files
find / -perm -o+w -type f 2>/dev/null

# ── FORENSICS ─────────────────────────────────────────────────────

# Files modified in last hour (during incident)
find / -mmin -60 2>/dev/null

# Save all investigation output to report
find / -mmin -60 2>/dev/null > incident_files.txt
grep "Failed" /var/log/auth.log >> incident_report.txt
```

---

## ⚡ Enriched Insights (Beyond the Source Material)

### The Pipe `|` — The Ultimate Power Tool

```bash
# Pipe sends output of one command INTO another command
command1 | command2

# Examples:
ls -la | grep ".txt"           # list files, filter for .txt only
cat access.log | grep "POST"   # find all POST requests
ps aux | grep "apache"         # find apache processes
history | grep "ssh"           # find SSH commands in history

# Chain multiple pipes
cat auth.log | grep "Failed" | awk '{print $11}' | sort | uniq -c
# Read log → filter failures → extract IP → sort → count unique

# This one-liner finds top brute force IPs attacking SSH!
```

### Output Redirection Summary

```
>   overwrite    echo "new" > file      (file wiped, new content)
>>  append       echo "add" >> file     (new content at bottom)
2>  stderr       command 2> errors      (only errors saved)
2>&1 both        command > out 2>&1     (stdout AND stderr)
|   pipe         cmd1 | cmd2            (output flows to next cmd)
/dev/null        command 2>/dev/null    (discard errors)
```

---

_Notes compiled from TryHackMe — Linux Fundamentals Module_
_Enriched with security use cases, SOC workflows, and penetration testing context_
