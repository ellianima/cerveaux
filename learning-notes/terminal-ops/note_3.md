# Session 1 — Terminal, Git, GitHub & Kali Linux
**Date:** March 18, 2026  
**Environment:** Kali Linux (Virtual Machine)

---

## 1. The Terminal

The terminal is a text-based interface to your operating system.
Instead of clicking icons, you type commands directly.

### Reading the Prompt
```
┌──(kali㉿kali)-[~]
└─$
```
- Left of ㉿ = **username** (kali)
- Right of ㉿ = **machine name** (kali)
- `~` = current directory (home directory shortcut for `/home/kali`)
- `$` = regular user awaiting input
- `#` = superuser (root) — more powerful, more dangerous

---

## 2. Core Navigation Commands

| Command | What it does |
|---|---|
| `whoami` | Prints your current username |
| `pwd` | Print Working Directory — shows where you are |
| `ls` | Lists files in current directory |
| `ls -la` | Lists ALL files (including hidden) with full details |
| `cd foldername` | Move into a folder |
| `cd ..` | Move up one level (parent directory) |
| `cd ~` | Go straight home from anywhere |

### Hidden Files
Files starting with `.` (like `.bashrc`, `.ssh`) are hidden.
`ls` won't show them. `ls -la` will.

---

## 3. File Operations

| Command | What it does |
|---|---|
| `echo "text" > file.txt` | Create file with content (overwrites) |
| `echo "text" >> file.txt` | Append to existing file |
| `cat file.txt` | Print file contents to screen |
| `mv oldname newname` | Move or rename a file |
| `mkdir foldername` | Create a directory |
| `mkdir -p parent/child` | Create nested directories in one shot |
| `rm filename` | Delete a file |
| `rm -rf foldername` | Delete a folder and everything inside it (no undo!) |
| `nano filename` | Open file in text editor (Ctrl+X, Y, Enter to save) |

### Terminal Shortcuts
- **Arrow up/down** — cycle through command history
- **Tab** — autocomplete filenames and commands

---

## 4. What is Git?

Git is a **Version Control System** — it takes labeled snapshots
of your project over time so you can:
- Never lose work
- Experiment freely and undo mistakes
- See exactly what changed, when, and why

### The Three States of Git
```
Working Directory → Staging Area → Repository
  (you edit here)   (git add here)  (git commit here)
```

- **Working Directory** — your desk. Files you're creating/editing.
- **Staging Area** — the outbox. You select what goes into the next snapshot.
- **Repository** — the locked filing cabinet. Permanent snapshot history.

### Git Setup (one time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
```

---

## 5. The Core Git Workflow
```bash
git init                        # Start tracking a folder
git status                      # Check state (run this constantly)
git add filename                # Stage a specific file
git add .                       # Stage everything
git commit -m "Your message"    # Take the snapshot
git log --oneline               # See commit history
```

### Commit Message Habit
Every message should complete: "If applied, this commit will ___"

Good: `"Add session 1 notes markdown file"`  
Bad: `"stuff"` or `"My message!!!!"`

---

## 6. What is GitHub?

GitHub is a cloud hosting service for Git repositories.
It is NOT the same as Git.

- Git = the tool (local)
- GitHub = the cloud + collaboration platform (remote)

GitHub is also your **public portfolio** — recruiters look at it.
Active repos and clean commit history signal you're the real deal.

---

## 7. SSH Authentication

SSH (Secure Shell) = a secure protocol for machine-to-machine communication.

A **key pair** is generated — two mathematically linked keys:
- **Private key** — lives on your machine. Never share this.
- **Public key** — given to GitHub. Safe to share.

GitHub sends a challenge → your private key solves it →
your public key verifies it → identity proven, no password needed.

### Setup (one time per machine)
```bash
ssh-keygen -t ed25519 -C "you@email.com"
cat ~/.ssh/id_ed25519.pub        # Copy this output
# Paste into GitHub → Settings → SSH Keys → New SSH Key

ssh -T git@github.com            # Test the connection
# Should say: "Hi username! You've successfully authenticated."
```

### Key Terms
- **SHA256 fingerprint** — a hash of your public key. Short unique ID.
- **Randomart image** — visual representation of your key. Human-friendly only.
- **ed25519** — the algorithm used to generate the key pair. Modern and secure.

---

## 8. Connecting Local Repo to GitHub
```bash
git remote add origin git@github.com:username/repo.git
git remote -v                    # Verify connection (fetch + push)
git push -u origin main          # First push (sets upstream)
git push                         # All future pushes
```

### What these mean
- `origin` — the name Git gives to your remote (GitHub)
- `main` — the branch you're pushing to
- `-u` — sets upstream, so future pushes only need `git push`

---

## 9. Syncing with GitHub
```bash
git pull origin main             # Download + merge remote changes
git push origin --delete branch  # Delete a remote branch
```

### Behind / Ahead
- **Behind** = GitHub has commits you don't have locally yet → `git pull`
- **Ahead** = You have commits GitHub doesn't have yet → `git push`

---

## 10. Branches

A branch is a parallel version of your project.

- `main` — the default, production branch. Never commit directly here in teams.
- `master` — old default name. Modern standard is `main`.
- `HEAD` — a pointer to your current position in history.
```bash
git branch                       # List branches
git checkout -b branchname       # Create + switch to new branch
git checkout branchname          # Switch to existing branch
```

---

## 11. The Full Workflow (Start to GitHub)
```
1. git init / git remote add origin  — connect or initialize
2. Create / edit files               — working directory
3. git add                           — staging area
4. git commit -m "message"           — local repository
5. git push                          — remote repository (GitHub)
```

Note: commits only happen locally.
`git push` uploads existing commits — it does not create new ones.

---

## 12. Bash vs Shell vs CLI

- **CLI** (Command Line Interface) — the text-based environment you type into
- **Shell** — the program that interprets commands and talks to the OS kernel
- **Bash** — a specific shell. The most common on Linux, including Kali.

Other shells exist: Zsh, Fish, Sh — Bash is the standard.

---

## Key Habits Built This Session

- Run `git status` constantly — before and after every action
- Write commit messages that complete: "If applied, this commit will ___"
- `git push` only needs `--set-upstream origin main` once per branch
- `rm -rf` is permanent — think before running it
- Tab autocomplete everything — saves time and prevents typos
- Arrow up — cycle command history instead of retyping
