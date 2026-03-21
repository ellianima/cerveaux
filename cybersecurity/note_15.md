# 🌐 Networking Fundamentals — Client-Server, HTTP & Protocols

> **Source:** TryHackMe — Pre-Security / Networking Fundamentals Module
> **Purpose:** Core networking concepts for cybersecurity
> **Covers:** Client-Server model, Request/Response, Protocol, Port,
> DNS, HTTP/HTTPS, HTTP Methods, GET requests, DevTools Network tab

---

## 🧒 Feynman Explanation — The Pizza Analogy

Everything in networking can be explained with a pizza shop:

| Networking Concept | Pizza Analogy                                          |
| ------------------ | ------------------------------------------------------ |
| **Client**         | You (Alice) — the one who wants something              |
| **Server**         | Luigi's Pizza — the one who provides it                |
| **Request**        | "One large pepperoni pizza and a coke!"                |
| **Response**       | The pizza arriving at your table                       |
| **Protocol**       | The menu + ordering rules (what you can order, how)    |
| **Port**           | Which door — Takeout (A), Restaurant (B), Delivery (C) |
| **DNS**            | GPS — you say "Luigi's Pizza", it finds the address    |

Every single interaction on the internet follows this exact pattern.
Your browser is Alice. Every website is Luigi's Pizza.

---

## 🔷 1. Client & Server Model

### The Golden Rule

> **The client ALWAYS initiates the request.**
> The server ALWAYS waits and responds.

```
CLIENT (Browser/App)          SERVER (Web Server)
─────────────────             ──────────────────
Sends request        ──▶      Receives request
Waits for response            Processes request
Receives response    ◀──      Sends response
Renders/uses data             Waits for next request
```

### Real-World Examples

| Client         | Server          | What It Requests |
| -------------- | --------------- | ---------------- |
| Chrome browser | tryhackme.com   | HTML page        |
| Spotify app    | Spotify servers | Audio stream     |
| Your email app | Gmail servers   | New emails       |
| VS Code        | GitHub          | Code repository  |
| ATM machine    | Bank server     | Account balance  |

> 💡 **Key insight:** A machine can be BOTH client and server
> simultaneously. A web server serves HTML to browsers (server)
> but also requests data from a database (client). This is the
> basis of microservices architecture.

---

## 🔷 2. Request & Response

### Structure of a Request

```
A request must contain:
  1. What you WANT          (the resource — e.g., /index.html)
  2. How you want it        (the method — e.g., GET)
  3. Who you are            (headers — browser, cookies)
  4. Where to send it       (the host — tryhackme.com)

If the request is malformed → Error response
If the resource doesn't exist → 404 Not Found
If you don't have permission → 403 Forbidden
```

### Structure of a Response

```
A response always contains:
  1. Status code            (200 OK, 404 Not Found, 500 Error)
  2. Response headers       (metadata about the response)
  3. Response body          (the actual content — HTML, JSON, etc.)
```

### Viewing Requests Live — Browser DevTools

```
HOW TO OPEN:
  Press F12 → click "Network" tab → reload the page

WHAT YOU SEE:
  Every single request your browser makes:
  - index.html    (the webpage itself)
  - style.css     (the styling)
  - script.js     (the JavaScript)
  - favicon.ico   (the little icon in the browser tab)
  - Images, fonts, API calls — everything

CLICKING ONE REQUEST SHOWS:
  Headers tab  → request and response headers
  Response tab → the actual content returned
  Timing tab   → how long each part took

KEY FIELDS IN HEADERS:
  Scheme    → HTTP or HTTPS
  Host      → which server (httpdemo.local:8080)
  Filename  → which file (/ = index.html)
  Address   → IP address of server (127.0.0.1 = localhost)
  Status    → 200 OK = success
```

### 💻 Inspecting HTTP Requests (Practical)

```bash
# See full request and response headers
curl -v https://tryhackme.com

# See ONLY response headers
curl -I https://tryhackme.com

# See ONLY the response body (HTML)
curl -s https://tryhackme.com

# Make a GET request and save response
curl -o response.html https://tryhackme.com

# Python: make a GET request programmatically
import requests

r = requests.get("https://tryhackme.com")

print("Status:", r.status_code)           # 200
print("Server:", r.headers.get("Server")) # nginx/...
print("Content-Type:", r.headers.get("Content-Type"))
print("Body preview:", r.text[:300])      # first 300 chars of HTML

# Full headers dictionary
for key, value in r.headers.items():
    print(f"{key}: {value}")
```

---

## 🔷 3. Protocol

### 🧒 Feynman Explanation

Imagine you call a pizza shop but speak only Tagalog and they
speak only Italian. No pizza gets ordered. A **protocol** is the
agreed language and rules both sides follow — so they can
understand each other perfectly.

### What a Protocol Defines

```
A protocol specifies:

  1. Commands    — what requests are valid
                   e.g., GET, POST, PUT, DELETE

  2. Structure   — how a request is formatted
                   e.g., "command first, then the resource"

  3. Syntax      — exact format rules
                   e.g., HTTP/1.1 uses headers separated by \r\n

  4. Responses   — what response maps to what request
                   e.g., successful GET → 200 OK + content

  5. Errors      — how to handle bad requests
                   e.g., unknown resource → 404 Not Found
```

### Common Protocols and Their Ports

| Protocol  | Port | Purpose                | Encrypted?    |
| --------- | ---- | ---------------------- | ------------- |
| **HTTP**  | 80   | Web pages              | ❌ No         |
| **HTTPS** | 443  | Secure web pages       | ✅ Yes (TLS)  |
| **FTP**   | 21   | File transfer          | ❌ No         |
| **SFTP**  | 22   | Secure file transfer   | ✅ Yes (SSH)  |
| **SSH**   | 22   | Secure remote terminal | ✅ Yes        |
| **DNS**   | 53   | Domain name resolution | ❌ Usually no |
| **SMTP**  | 25   | Send email             | ❌ No         |
| **IMAP**  | 143  | Receive email          | ❌ No         |
| **RDP**   | 3389 | Windows remote desktop | ✅ Partial    |
| **SMB**   | 445  | Windows file sharing   | ❌ No         |

> ⚠️ **Security note:** Unencrypted protocols (HTTP, FTP, SMTP,
> SMB) send everything in plaintext. Anyone sniffing the
> network with Wireshark can read passwords, files, and
> emails in real time. Always use encrypted alternatives.

---

## 🔷 4. Ports

### 🧒 Feynman Explanation

One building (server) can offer many services through different
doors. Takeout uses Door A, Dining uses Door B, Delivery uses
Door C. Ports are those doors — each service gets its own door
number so traffic goes to the right place.

### Port Ranges

```
0–1023      Well-known ports (reserved for standard services)
            HTTP=80, HTTPS=443, SSH=22, FTP=21

1024–49151  Registered ports (applications register these)
            MySQL=3306, PostgreSQL=5432, Redis=6379

49152–65535 Dynamic/ephemeral ports (used by clients temporarily)
            Your browser uses a random high port for each request
```

### How Ports Work in Practice

```
Client connects to: 192.168.1.100:80   → Web server (HTTP)
Client connects to: 192.168.1.100:443  → Web server (HTTPS)
Client connects to: 192.168.1.100:22   → SSH server
Client connects to: 192.168.1.100:3306 → MySQL database
Client connects to: 192.168.1.100:8080 → Custom app server

Same IP address → different port → completely different service
```

### 💻 Port Scanning (Core Pentester Skill)

```bash
# Scan top 1000 ports (quick)
nmap 192.168.1.100

# Scan ALL 65535 ports (thorough)
nmap -p- 192.168.1.100

# Scan with service version detection
nmap -sV 192.168.1.100

# Scan specific ports
nmap -p 22,80,443,3306,8080 192.168.1.100

# Check if a specific port is open (Python)
import socket

def check_port(host, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

# Test common web ports
for port in [80, 443, 8080, 8443]:
    status = "OPEN" if check_port("tryhackme.com", port) else "CLOSED"
    print(f"Port {port}: {status}")
```

---

## 🔷 5. DNS — Domain Name System

### 🧒 Feynman Explanation

You know your friend's name (Alice), but to text her, you need
her phone number. DNS is your contacts app — you type a name
(tryhackme.com) and it gives you the number (104.26.10.229).

```
Human-readable:   tryhackme.com
Machine-readable: 104.26.10.229

DNS translates between them — automatically, in milliseconds.
```

### DNS in the Pizza Analogy

```
Alice knows "Luigi's Pizza" (the name)
But to get there, she needs the ADDRESS (coordinates)
Bob enters "Luigi's Pizza" into GPS
GPS returns: "42 Street, New York, NY 10001"
Bob drives there using the coordinates

Your browser  = Alice
"Luigi's Pizza" = tryhackme.com
GPS           = DNS server
Coordinates   = IP address (104.26.10.229)
```

### What an IP Address Is

```
IP = Internet Protocol address
   = The unique "home address" of a device on a network

IPv4: 192.168.1.10    (4 numbers, 0-255, separated by dots)
IPv6: 2001:db8::1     (newer, much larger address space)

Parts of an IP address:
  192.168.1   → network part (which neighborhood)
  .10         → host part (which house in that neighborhood)

Special addresses:
  127.0.0.1   → localhost (your own machine)
  192.168.x.x → private network (home/office, not internet)
  8.8.8.8     → Google's public DNS server
```

---

## 🔷 6. HTTP/HTTPS — The Web Protocol

### 🧒 Feynman Explanation

HTTP is the language browsers and web servers use. It's like
a very formal ordering system: "GET me /index.html please."
The server says "200 OK, here it is." Every web interaction
follows this exact script.

HTTPS is the same thing, but spoken in a locked room where
nobody else can eavesdrop — encrypted with TLS.

### HTTP is Stateless

```
STATELESS = the server has NO memory between requests

Request 1: "GET /home"
  Server: "OK here's the home page" — then FORGETS you

Request 2: "GET /dashboard" (you're logged in!)
  Server: "Who are you? I don't remember you."

SOLUTION: Cookies and Session Tokens
  After login → server creates a session token
  Token stored in a cookie: Cookie: session=abc123xyz
  Sent with EVERY subsequent request
  Server checks token → "oh it's you, welcome back!"
```

### All 9 HTTP Methods

| Method      | Purpose                                 | Request has Body? | Idempotent? |
| ----------- | --------------------------------------- | ----------------- | ----------- |
| **GET**     | Retrieve a resource                     | No                | ✅ Yes      |
| **POST**    | Submit data / create resource           | Yes               | ❌ No       |
| **PUT**     | Replace entire resource                 | Yes               | ✅ Yes      |
| **PATCH**   | Update part of resource                 | Yes               | ❌ No       |
| **DELETE**  | Remove a resource                       | No                | ✅ Yes      |
| **HEAD**    | Like GET but headers only               | No                | ✅ Yes      |
| **OPTIONS** | Ask what methods are allowed            | No                | ✅ Yes      |
| **CONNECT** | Set up tunnel (used for HTTPS proxying) | No                | ❌ No       |
| **TRACE**   | Debug — echoes request back             | No                | ✅ Yes      |

> 💡 **Idempotent** = running it multiple times gives the
> same result. DELETE once = DELETE ten times = same end state.
> POST ten times = ten new records created (not idempotent).

### The GET Method — Most Common

```
GET retrieves a resource without modifying anything.

When you visit https://tryhackme.com/index.php:
  Your browser sends:
    GET /index.php HTTP/1.1
    Host: tryhackme.com
    User-Agent: Mozilla/5.0...
    Accept: text/html...

  Server responds:
    HTTP/1.1 200 OK
    Content-Type: text/html
    Content-Length: 5432

    <!DOCTYPE html>
    <html>...actual webpage HTML...</html>

Loading ONE webpage triggers MANY GET requests:
  GET /           → index.html    (the page structure)
  GET /style.css  → stylesheet    (the styling)
  GET /script.js  → JavaScript    (the interactivity)
  GET /favicon.ico → tiny icon    (browser tab icon)
  GET /images/... → each image    (separate requests)
```

### 💻 HTTP Requests in Practice

```python
import requests

# ── GET — retrieve data ───────────────────────────────────────────
r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("GET Status:", r.status_code)
print("GET Data:", r.json())

# ── POST — submit data ────────────────────────────────────────────
data = {"title": "My Post", "body": "Hello", "userId": 1}
r = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)
print("POST Status:", r.status_code)  # 201 Created
print("POST Response:", r.json())

# ── PUT — replace entire resource ────────────────────────────────
r = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={"title": "Updated", "body": "New body", "userId": 1}
)
print("PUT Status:", r.status_code)   # 200 OK

# ── DELETE — remove resource ──────────────────────────────────────
r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print("DELETE Status:", r.status_code)  # 200 OK

# ── HEAD — headers only, no body ─────────────────────────────────
r = requests.head("https://tryhackme.com")
print("Content-Type:", r.headers.get("Content-Type"))
print("Server:", r.headers.get("Server"))
# Body is empty — only headers returned

# ── OPTIONS — what methods does this endpoint allow? ─────────────
r = requests.options("https://httpbin.org/anything")
print("Allowed:", r.headers.get("Allow"))
```

---

## 🔷 7. Reading the DevTools Network Tab

### What Each Column Means

```
In F12 → Network tab:

Status   → HTTP status code (200=OK, 404=Not Found, 500=Error)
Method   → GET, POST, PUT, etc.
Domain   → which server the request went to
File     → which resource was requested
Type     → document, stylesheet, script, image, xhr, fetch
Size     → bytes transferred over network
Time     → how long the request took

CLICKING A REQUEST SHOWS:
  Headers tab:
    Scheme    → http or https
    Host      → server hostname
    Filename  → resource path
    Address   → server IP address
    Status    → 200 OK
    Version   → HTTP/1 or HTTP/2

  Response tab:
    The actual HTML/JSON/CSS/JS content returned

  Timing tab:
    DNS lookup time
    Connection time
    SSL handshake time
    Time to first byte (TTFB)
    Download time
```

> ⚠️ **Pentest use:** The Network tab reveals ALL requests
> including API calls, authentication tokens in headers,
> hidden endpoints not visible on the page, and the exact
> request format needed to replicate/manipulate requests
> in Burp Suite.

### Cascade Effect — One Page = Many Requests

```
You request: https://httpdemo.local:8080/

Browser sends:
  1. GET /           → 200 OK   (737B) — HTML page
  2. GET /style.css  → 200 OK   (349B) — CSS (from <link> tag)
  3. GET /script.js  → 200 OK   (355B) — JS (from <script> tag)
  4. GET /favicon.ico→ 404      (520B) — icon (auto-requested)

Total: 4 requests, 1.21KB transferred, 349ms load time

Why this matters for security:
  → Each request is an attack surface
  → JS files often contain API keys, endpoints, secrets
  → CSS files can reveal file structure
  → 404 responses reveal attempted paths
```

---

## 🔗 Security Attack Map

| Concept            | Attack                  | Tool/Technique            |
| ------------------ | ----------------------- | ------------------------- |
| HTTP (unencrypted) | Credential sniffing     | Wireshark, tcpdump        |
| Open ports         | Service exploitation    | Nmap → searchsploit       |
| DNS                | Zone transfer, spoofing | `dig axfr`, dnsspoof      |
| HTTP Methods       | Unauthorized PUT/DELETE | curl, Burp Suite          |
| Stateless HTTP     | Session token theft     | XSS + `document.cookie`   |
| GET parameters     | SQL injection, XSS      | `?id=1'--`, `?q=<script>` |
| Response headers   | Server fingerprinting   | curl -I, Wappalyzer       |
| DevTools Network   | API endpoint discovery  | Manual recon in browser   |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### HTTP/1.1 vs HTTP/2 vs HTTP/3

```
HTTP/1.1  → One request per TCP connection (slow, sequential)
HTTP/2    → Multiple requests on ONE connection (multiplexing)
            Much faster, used by most modern sites
HTTP/3    → Uses UDP instead of TCP (QUIC protocol)
            Even faster, used by Google, Cloudflare

You can see which version in DevTools → Network → Protocol column
```

### The Request-Response Full Picture

```
You type: https://tryhackme.com

1. Browser checks DNS cache → miss
2. DNS lookup → 104.26.10.229
3. TCP 3-way handshake (SYN → SYN-ACK → ACK)
4. TLS handshake (HTTPS certificate negotiation)
5. Browser sends: GET / HTTP/2
                  Host: tryhackme.com
                  Cookie: session=abc...
6. Server receives, processes, queries database
7. Server sends: HTTP/2 200 OK
                 Content-Type: text/html
                 [HTML body]
8. Browser parses HTML → finds <link>, <script>, <img>
9. Browser sends MORE GET requests for each asset
10. Browser renders complete page
    Total time: ~200-400ms
```

### Curl Cheat Sheet for Analysts

```bash
# Full verbose request (see everything)
curl -v https://target.com

# Custom method
curl -X DELETE https://target.com/api/user/1
curl -X PUT https://target.com/api/user/1 -d '{"name":"admin"}'

# Custom headers (auth token, custom user agent)
curl -H "Authorization: Bearer TOKEN" https://target.com/api
curl -H "User-Agent: Mozilla/5.0" https://target.com

# POST form data (login attempt)
curl -X POST -d "username=admin&password=admin" https://target.com/login

# POST JSON data
curl -X POST -H "Content-Type: application/json" \
     -d '{"username":"admin","password":"admin"}' \
     https://target.com/api/login

# Follow redirects
curl -L https://target.com

# Save cookies and reuse them
curl -c cookies.txt https://target.com/login
curl -b cookies.txt https://target.com/dashboard
```

---

_Notes compiled from TryHackMe — Pre-Security Networking Module_
_Enriched with Feynman explanations, practical code, and security context_
