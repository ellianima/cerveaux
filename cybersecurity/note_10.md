# 🌐 HTTP & HTTPS — How the Web Actually Works

> **Source:** TryHackMe — How The Web Works Module
> **Purpose:** Core web knowledge for cybersecurity & web development

---

## 🧒 Feynman Explanation — What is HTTP?

Imagine you walk into a library. You (the browser) ask the librarian
(the web server) for a specific book (a webpage). The librarian
understands your request because you both speak the same language —
that language is **HTTP**. The librarian finds the book and hands it
back to you. That's literally it.

**HTTPS** is the same thing, except now you and the librarian are
whispering in a secret code that nobody else in the library can
understand — even if someone is listening.

---

## 🔷 1. HTTP vs HTTPS

| Feature                     | HTTP                        | HTTPS                              |
| --------------------------- | --------------------------- | ---------------------------------- |
| Full Name                   | HyperText Transfer Protocol | HyperText Transfer Protocol Secure |
| Encrypted?                  | ❌ No                       | ✅ Yes (TLS/SSL encryption)        |
| Port                        | 80                          | 443                                |
| Verifies server identity?   | ❌ No                       | ✅ Yes (via certificates)          |
| Safe for passwords/banking? | ❌ Never                    | ✅ Yes                             |
| Invented by                 | Tim Berners-Lee, 1989–1991  | Extension of HTTP + TLS            |

> ⚠️ **Security note:** HTTP sends everything in **plain text**.
> An attacker on the same network can read your passwords, cookies,
> and form data with a simple packet sniffer (Wireshark, tcpdump).
> Always use HTTPS.

---

## 🔷 2. URLs — Uniform Resource Locator

### 🧒 Feynman Explanation

A URL is like a **home address for a resource on the internet**.
Just like a postal address has a country, city, street, and house
number — a URL has a scheme, host, port, path, and more.

```
http://user:password@tryhackme.com:80/view-room?id=1#task3
```

| Part             | Example         | What it means                                  |
| ---------------- | --------------- | ---------------------------------------------- |
| **Scheme**       | `http`          | Protocol to use (HTTP, HTTPS, FTP)             |
| **User**         | `user:password` | Credentials for login (rare, insecure)         |
| **Host/Domain**  | `tryhackme.com` | The server's address                           |
| **Port**         | `80`            | Door number on the server (80=HTTP, 443=HTTPS) |
| **Path**         | `/view-room`    | Which resource/file you want                   |
| **Query String** | `?id=1`         | Extra parameters sent to the path              |
| **Fragment**     | `#task3`        | Jump to a specific section on the page         |

> 💡 **Key insight:** Ports are like apartment numbers in a building.
> The building is the server — the port tells you which specific
> service inside that building to talk to.

### 💻 Code Example — Parsing a URL in Python

```python
from urllib.parse import urlparse, parse_qs

url = "http://tryhackme.com:80/view-room?id=1&user=admin#task3"
parsed = urlparse(url)

print("Scheme:  ", parsed.scheme)    # http
print("Host:    ", parsed.hostname)  # tryhackme.com
print("Port:    ", parsed.port)      # 80
print("Path:    ", parsed.path)      # /view-room
print("Query:   ", parsed.query)     # id=1&user=admin
print("Fragment:", parsed.fragment)  # task3

# Parse query string into a dict
params = parse_qs(parsed.query)
print("Params:  ", params)           # {'id': ['1'], 'user': ['admin']}
```

> ⚠️ **Security note:** Query strings are visible in browser history,
> server logs, and referrer headers. Never put passwords or tokens
> in a URL query string.

---

## 🔷 3. HTTP Request & Response

### 🧒 Feynman Explanation

Think of HTTP like ordering food at a restaurant:

- **You** (browser) = the customer
- **Waiter** = the internet
- **Kitchen** (web server) = where the food is made
- **Your order** = the HTTP Request
- **The food delivered** = the HTTP Response

### 📤 Example HTTP Request

```http
GET / HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Referer: https://tryhackme.com/
```

| Line             | Meaning                                  |
| ---------------- | ---------------------------------------- |
| `GET / HTTP/1.1` | Method=GET, Path=/, Protocol version=1.1 |
| `Host`           | Which website on this server we want     |
| `User-Agent`     | Our browser name and version             |
| `Referer`        | Which page sent us here                  |
| _(blank line)_   | Signals end of request                   |

### 📥 Example HTTP Response

```http
HTTP/1.1 200 OK
Server: nginx/1.15.8
Date: Fri, 09 Apr 2021 13:34:03 GMT
Content-Type: text/html
Content-Length: 98

<html>
<head><title>TryHackMe</title></head>
<body>Welcome To TryHackMe.com</body>
</html>
```

| Line              | Meaning                                            |
| ----------------- | -------------------------------------------------- |
| `HTTP/1.1 200 OK` | Protocol version + status code (success)           |
| `Server`          | Web server software and version                    |
| `Date`            | Server's current date/time                         |
| `Content-Type`    | Type of data being returned                        |
| `Content-Length`  | Size of response (lets client detect missing data) |
| _(blank line)_    | Signals end of headers                             |
| HTML body         | The actual webpage content                         |

### 💻 Code Example — Making an HTTP Request in Python

```python
import requests

response = requests.get("https://tryhackme.com")

print("Status Code:", response.status_code)       # 200
print("Server:", response.headers.get("Server"))  # nginx/...
print("Content-Type:", response.headers.get("Content-Type"))
print("Body preview:", response.text[:200])        # First 200 chars of HTML
```

---

## 🔷 4. HTTP Methods

### 🧒 Feynman Explanation

HTTP methods are like **verbs** — they tell the server _what action_
you want to perform on a resource.

| Method      | Action                       | Real-World Analogy                           |
| ----------- | ---------------------------- | -------------------------------------------- |
| **GET**     | Retrieve data                | Reading a menu                               |
| **POST**    | Submit/create data           | Placing an order                             |
| **PUT**     | Update existing data         | Changing your order                          |
| **DELETE**  | Remove data                  | Cancelling your order                        |
| **PATCH**   | Partially update data        | Modifying one item in your order             |
| **HEAD**    | Get headers only (no body)   | Asking "do you have X?" without receiving it |
| **OPTIONS** | Ask what methods are allowed | Asking "what can I do here?"                 |

### 💻 Code Example — All HTTP Methods in Python

```python
import requests

base = "https://jsonplaceholder.typicode.com"

# GET — fetch a post
r = requests.get(f"{base}/posts/1")
print("GET:", r.status_code, r.json()["title"])

# POST — create a new post
r = requests.post(f"{base}/posts", json={
    "title": "My Post",
    "body": "Hello world",
    "userId": 1
})
print("POST:", r.status_code, r.json())

# PUT — replace entire post
r = requests.put(f"{base}/posts/1", json={
    "title": "Updated Title",
    "body": "Updated body",
    "userId": 1
})
print("PUT:", r.status_code)

# DELETE — remove a post
r = requests.delete(f"{base}/posts/1")
print("DELETE:", r.status_code)  # 200
```

> ⚠️ **Security note:** APIs that accept PUT/DELETE without proper
> authentication are vulnerable to **unauthorized data modification**.
> Always test APIs for missing auth checks — a classic bug bounty find.

---

## 🔷 5. HTTP Status Codes

### 🧒 Feynman Explanation

Status codes are the server's **one-line reaction** to your request.
Like a thumbs up, a redirect sign, a "not your fault" shrug, or a
"we broke something" alarm.

### Status Code Ranges

| Range   | Category      | Meaning                      |
| ------- | ------------- | ---------------------------- |
| **1xx** | Informational | Keep going, request received |
| **2xx** | Success       | All good!                    |
| **3xx** | Redirection   | Go look somewhere else       |
| **4xx** | Client Error  | You made a mistake           |
| **5xx** | Server Error  | We made a mistake            |

### Common Status Codes You Must Know

| Code    | Name                  | Meaning                               |
| ------- | --------------------- | ------------------------------------- |
| **200** | OK                    | Request succeeded                     |
| **201** | Created               | New resource created (POST success)   |
| **301** | Moved Permanently     | Page moved forever, update your links |
| **302** | Found                 | Temporary redirect                    |
| **400** | Bad Request           | Your request was malformed            |
| **401** | Not Authorised        | Login required                        |
| **403** | Forbidden             | Logged in but not allowed             |
| **404** | Not Found             | Resource doesn't exist                |
| **405** | Method Not Allowed    | Wrong HTTP method used                |
| **500** | Internal Server Error | Server crashed/broke                  |
| **503** | Service Unavailable   | Server overloaded or in maintenance   |

### 💻 Code Example — Handling Status Codes

```python
import requests

def fetch(url):
    r = requests.get(url)

    if r.status_code == 200:
        print("✅ Success!")
    elif r.status_code == 301:
        print("➡️ Permanently moved to:", r.headers.get("Location"))
    elif r.status_code == 401:
        print("🔒 Need to authenticate first")
    elif r.status_code == 403:
        print("🚫 Access forbidden")
    elif r.status_code == 404:
        print("❓ Page not found")
    elif r.status_code >= 500:
        print("💥 Server error:", r.status_code)

    return r

fetch("https://httpstat.us/404")  # Test any status code
```

> ⚠️ **Security note:** A **403** tells an attacker the resource
> _exists_ but they lack permission. A **404** means it doesn't exist.
> This difference leaks information — a well-hardened server returns
> 404 for both to prevent enumeration.

---

## 🔷 6. HTTP Headers

### 🧒 Feynman Explanation

Headers are like **sticky notes attached to your letter** before
mailing it. They don't change the letter's content — they give
the post office (and recipient) extra instructions about how to
handle it.

### 📤 Common Request Headers (Client → Server)

| Header            | Purpose                        | Example                         |
| ----------------- | ------------------------------ | ------------------------------- |
| `Host`            | Which website you want         | `Host: tryhackme.com`           |
| `User-Agent`      | Your browser/software identity | `User-Agent: Mozilla/5.0`       |
| `Content-Length`  | Size of data being sent        | `Content-Length: 42`            |
| `Accept-Encoding` | Compression formats supported  | `Accept-Encoding: gzip`         |
| `Cookie`          | Stored session data sent back  | `Cookie: session=abc123`        |
| `Authorization`   | Credentials/token              | `Authorization: Bearer <token>` |

### 📥 Common Response Headers (Server → Client)

| Header             | Purpose                        | Example                       |
| ------------------ | ------------------------------ | ----------------------------- |
| `Set-Cookie`       | Tell client to save a cookie   | `Set-Cookie: name=adam`       |
| `Cache-Control`    | How long to cache the response | `Cache-Control: max-age=3600` |
| `Content-Type`     | Type of data in response       | `Content-Type: text/html`     |
| `Content-Encoding` | Compression used               | `Content-Encoding: gzip`      |
| `Server`           | Web server software            | `Server: nginx/1.15.8`        |

### 💻 Code Example — Reading & Sending Headers

```python
import requests

# Sending custom headers (e.g. pretending to be a different browser)
headers = {
    "User-Agent": "MyCustomBot/1.0",
    "Accept-Encoding": "gzip, deflate",
    "Authorization": "Bearer my-secret-token"
}

r = requests.get("https://httpbin.org/headers", headers=headers)

# Reading response headers
print("Server:", r.headers.get("Server"))
print("Content-Type:", r.headers.get("Content-Type"))
print("All headers:", dict(r.headers))
```

> ⚠️ **Security note:** The `Server` header leaks the web server
> software and version. Security-hardened servers remove or fake
> this header to slow down attackers doing reconnaissance.

---

## 🔷 7. Cookies

### 🧒 Feynman Explanation

HTTP has **no memory** — every request is brand new, like a goldfish
forgetting what it just saw. Cookies are **sticky notes** the server
gives your browser to carry around, so the server can recognize you
on the next visit.

### How Cookies Work (Full Flow)

```
1. Client requests webpage
   GET / HTTP/1.1
   Host: cookies.thm

2. Server responds + sets a cookie
   HTTP/1.1 200 OK
   Set-Cookie: name=adam

3. Client sends the cookie on every future request
   GET / HTTP/1.1
   Cookie: name=adam

4. Server sees cookie → recognizes you → shows personalized content
```

### Cookie Properties

| Property     | Meaning                                       |
| ------------ | --------------------------------------------- |
| `name=value` | The actual data stored                        |
| `Expires`    | When the cookie dies                          |
| `HttpOnly`   | JavaScript can't read it (XSS protection)     |
| `Secure`     | Only sent over HTTPS                          |
| `SameSite`   | Controls cross-site sending (CSRF protection) |
| `Domain`     | Which domains receive this cookie             |

### 💻 Code Example — Working with Cookies in Python

```python
import requests

session = requests.Session()

# Login (server sets a cookie)
login = session.post("https://httpbin.org/cookies/set/session/abc123")

# All future requests automatically send the cookie
r = session.get("https://httpbin.org/cookies")
print("Cookies:", r.json())  # {'cookies': {'session': 'abc123'}}

# Manually inspect cookies
for cookie in session.cookies:
    print(f"Name: {cookie.name}, Value: {cookie.value}, "
          f"HttpOnly: {cookie.has_nonstandard_attr('HttpOnly')}")
```

> ⚠️ **Security notes:**
>
> - Cookies without `HttpOnly` → vulnerable to **XSS** (JavaScript steals them)
> - Cookies without `Secure` → sent over HTTP → **sniffable**
> - Cookies without `SameSite=Strict` → vulnerable to **CSRF attacks**
> - Cookie values are often **session tokens** — stealing one = stealing identity

---

## 🔗 Cybersecurity Attack Map

| Concept                   | Attack                  | Tool/Technique       |
| ------------------------- | ----------------------- | -------------------- |
| HTTP (no encryption)      | Credential sniffing     | Wireshark, tcpdump   |
| URL query strings         | Parameter tampering     | Burp Suite           |
| HTTP methods              | Unauthorized PUT/DELETE | curl, Burp Suite     |
| Status codes (403 vs 404) | Resource enumeration    | gobuster, ffuf       |
| Response headers          | Server fingerprinting   | curl -I, Wappalyzer  |
| Cookies (no HttpOnly)     | XSS cookie theft        | `document.cookie`    |
| Cookies (no SameSite)     | CSRF attack             | Malicious form POST  |
| 401 responses             | Brute force auth        | Hydra, Burp Intruder |

---

## ⚡ Enriched Insights (Beyond the Source Material)

### The Request-Response Cycle (Full Picture)

```
You type URL → DNS lookup → TCP 3-way handshake →
TLS handshake (HTTPS) → HTTP Request sent →
Server processes → HTTP Response returned →
Browser renders HTML → Requests CSS/JS/images → Done
```

### HTTP/1.1 vs HTTP/2 vs HTTP/3

| Version  | Key Feature                                      |
| -------- | ------------------------------------------------ |
| HTTP/1.1 | One request per connection (slow)                |
| HTTP/2   | Multiplexing — many requests simultaneously      |
| HTTP/3   | Uses UDP instead of TCP (faster, used by Google) |

### Tools Professionals Use

| Tool           | Purpose                                 |
| -------------- | --------------------------------------- |
| **Burp Suite** | Intercept, modify, replay HTTP requests |
| **curl**       | Command-line HTTP requests              |
| **Postman**    | API testing with full HTTP control      |
| **Wireshark**  | See raw HTTP packets on the wire        |
| **httpx**      | Fast async HTTP in Python               |

### Bash One-Liners

```bash
# See response headers only
curl -I https://tryhackme.com

# Send a POST with data
curl -X POST -d "username=admin&password=1234" https://site.com/login

# See full request + response
curl -v https://tryhackme.com

# Send custom headers
curl -H "User-Agent: MyBot" -H "Authorization: Bearer token123" https://site.com
```

---

_Notes compiled from TryHackMe — How The Web Works Module_
_Enriched with Feynman explanations, code examples, and security context_
