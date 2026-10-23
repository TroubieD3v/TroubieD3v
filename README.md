<img src="assets/banner.svg" alt="TroubieD3v: I break web apps on purpose, then make sure the fix holds." width="100%">

I'm learning application security the hands-on way: write the vulnerable version, exploit it, write the fix,
then prove that the same attack no longer works. What I build for that is open source and runs locally:
a playground for learning the bugs, and a tool for finding them in real APIs.

### websec-lab

<a href="https://github.com/TroubieD3v/websec-lab"><img src="https://github.com/TroubieD3v/websec-lab/raw/main/docs/screenshots/demo.gif" alt="websec-lab: Alice reads Bob's booking in the vulnerable mode; in the fixed mode the same request is refused" width="100%"></a>

A web security playground with twelve labs mapped to the OWASP Top 10:2025, from SQL injection and XSS to
JWT forgery and race conditions. Each lab runs the vulnerable code and its fix side by side, shows the diff,
and checks on the server that your attack works against one and fails against the other.
**[Try it](https://github.com/TroubieD3v/websec-lab#quick-start-docker)** with one `docker compose up`.

### AuthScope

<a href="https://github.com/TroubieD3v/APIAuthorizationTester"><img src="https://github.com/TroubieD3v/APIAuthorizationTester/raw/main/docs/screenshots/demo.gif" alt="AuthScope: a test run, the permission matrix with policy violations, and the evidence for one finding" width="100%"></a>

An API authorization tester for AppSec work and authorized pentests. Import OpenAPI or Postman, add a few test
accounts, say who owns which objects, and it checks BOLA/IDOR, BFLA, BOPLA, unauthenticated and cross-tenant
access. It compares real responses with the policy instead of trusting status codes, so a `200 []` is not a finding,
and every violation comes with both requests, the diff and a `curl` to reproduce it.
**[Try it](https://github.com/TroubieD3v/APIAuthorizationTester#quick-start-docker)** with one `docker compose up`.

### Tools I use

![Python](https://img.shields.io/badge/Python-1a1d22?style=flat-square&logo=python&logoColor=7cc4e8)
![FastAPI](https://img.shields.io/badge/FastAPI-1a1d22?style=flat-square&logo=fastapi&logoColor=7cc4e8)
![TypeScript](https://img.shields.io/badge/TypeScript-1a1d22?style=flat-square&logo=typescript&logoColor=7cc4e8)
![React](https://img.shields.io/badge/React-1a1d22?style=flat-square&logo=react&logoColor=7cc4e8)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-1a1d22?style=flat-square&logo=tailwindcss&logoColor=7cc4e8)
![SQLite](https://img.shields.io/badge/SQLite-1a1d22?style=flat-square&logo=sqlite&logoColor=7cc4e8)
![Playwright](https://img.shields.io/badge/Playwright-1a1d22?style=flat-square&logo=playwright&logoColor=7cc4e8)
![Docker](https://img.shields.io/badge/Docker-1a1d22?style=flat-square&logo=docker&logoColor=7cc4e8)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-1a1d22?style=flat-square&logo=githubactions&logoColor=7cc4e8)

### Studying now

- Web application pentesting with the [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- Access control and authentication flaws in APIs ([OWASP API Security Top 10:2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/))
- Writing fixes that hold, and tests that prove they do
