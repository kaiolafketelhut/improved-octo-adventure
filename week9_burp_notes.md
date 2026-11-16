# Week 9 - Burp Suite + TryHackMe

## Burp Basics
- Proxy 127.0.0.1:8080 - Intercept an/aus
- Intercept = Request anhalten + ändern
- Repeater = Request immer wieder schicken + ändern
- Intruder = Automatisiert viele Payloads (Community = langsam, aber reicht)

## Mein Lab-Test
- lab_fixed.py + Burp: <script> -> &lt;script&gt; = GEBLOCKT
- lab.py + Burp: <script> -> <script> = VERWUNDBAR

## TryHackMe Progress
- [ ] Pre-Security Path
- [ ] Junior Pentester Path
- [ ] Burp Suite Room
- [ ] OWASP Top 10 Room

## eJPT Cheat Sheet
- nmap -sC -sV -oN scan.txt <IP>
- SQLi: ' OR '1'='1 -- 
- XSS: <script>alert(1)</script>
- Hash: PBKDF2 + Salt, nie MD5
