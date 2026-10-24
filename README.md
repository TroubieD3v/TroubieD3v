<img src="assets/banner.svg" alt="TroubieD3v: I break web apps on purpose, then make sure the fix holds." width="100%">

<p align="center">
  Application and infrastructure security, learned hands-on: write the vulnerable version, exploit it, fix it,<br>
  then prove the same attack no longer works. Everything I build for that is open source and runs locally.
</p>

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/TroubieD3v/websec-lab"><img src="assets/card-websec-lab.svg" alt="websec-lab: break vulnerable code, watch the fix hold, verify both automatically" width="100%"></a>
      <p>Twelve labs from SQL injection and XSS to JWT forgery and race conditions. Each runs the vulnerable code and
      its fix side by side, shows the diff, and checks on the server that your attack lands on one and fails on the other.</p>
      <p><a href="https://github.com/TroubieD3v/websec-lab"><b>Repository</b></a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/websec-lab#quick-start-docker">Quick start</a></p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/TroubieD3v/AuthScope"><img src="assets/card-authscope.svg" alt="AuthScope: finds authorization bugs in REST APIs by checking who can really reach what" width="100%"></a>
      <p>Import OpenAPI or Postman, add test accounts, say who owns which objects. AuthScope compares real responses with
      your policy, so <code>200 []</code> is not a finding, and every violation comes with both requests and a curl to reproduce it.</p>
      <p><a href="https://github.com/TroubieD3v/AuthScope"><b>Repository</b></a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/AuthScope#quick-start-docker">Quick start</a></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/TroubieD3v/CloudGraph"><img src="assets/card-cloudgraph.svg" alt="CloudGraph: explains how small misconfigurations chain into an attack path" width="100%"></a>
      <p>Reads Docker Compose, Kubernetes and Terraform plans offline and builds a graph of who can reach what. It shows how
      an exposed pod, a mounted token and a broad role add up to a path to your secrets, traces every step to a line of
      config, and simulates which fix breaks the most chains before you touch a file.</p>
      <p><a href="https://github.com/TroubieD3v/CloudGraph"><b>Repository</b></a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/CloudGraph#quick-start-docker">Quick start</a></p>
    </td>
    <td width="50%" valign="top">
      <h4>One idea, three layers</h4>
      <p><b>Code</b>: in websec-lab you write the bug, exploit it and watch the fix refuse the same request.</p>
      <p><b>API</b>: AuthScope finds the same class of bugs in a running service, using your access policy as the oracle.</p>
      <p><b>Infrastructure</b>: CloudGraph shows how the platform around the service turns one bug into a path to the
      crown jewels, and which change cuts it.</p>
      <p>All three report evidence rather than guesses, separate "proven" from "possible", and ship a vulnerable and a
      hardened version so the tests can show both.</p>
    </td>
  </tr>
</table>

<details>
  <summary><b>See them in action</b></summary>
  <br>
  <p><b>websec-lab</b>: Alice reads Bob's booking in the vulnerable mode; in the fixed mode the same request is refused.</p>
  <img src="https://github.com/TroubieD3v/websec-lab/raw/main/docs/screenshots/demo.gif" alt="websec-lab demo" width="100%">
  <p><b>AuthScope</b>: a run against the demo API, the permission matrix, and the evidence for one finding.</p>
  <img src="https://github.com/TroubieD3v/AuthScope/raw/main/docs/screenshots/demo.gif" alt="AuthScope demo" width="100%">
  <p><b>CloudGraph</b>: attack paths in an insecure cluster, one highlighted in the graph, a what-if fix that removes four, and a diff against the hardened version.</p>
  <img src="https://github.com/TroubieD3v/CloudGraph/raw/main/docs/screenshots/demo.gif" alt="CloudGraph demo" width="100%">
</details>

<h3 align="center">Toolbox</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-1a1d22?style=for-the-badge&logo=python&logoColor=7cc4e8" alt="Python">
  <img src="https://img.shields.io/badge/Go-1a1d22?style=for-the-badge&logo=go&logoColor=7cc4e8" alt="Go">
  <img src="https://img.shields.io/badge/FastAPI-1a1d22?style=for-the-badge&logo=fastapi&logoColor=7cc4e8" alt="FastAPI">
  <img src="https://img.shields.io/badge/TypeScript-1a1d22?style=for-the-badge&logo=typescript&logoColor=7cc4e8" alt="TypeScript">
  <img src="https://img.shields.io/badge/React-1a1d22?style=for-the-badge&logo=react&logoColor=7cc4e8" alt="React">
  <img src="https://img.shields.io/badge/Tailwind-1a1d22?style=for-the-badge&logo=tailwindcss&logoColor=7cc4e8" alt="Tailwind CSS">
  <br>
  <img src="https://img.shields.io/badge/Kubernetes-1a1d22?style=for-the-badge&logo=kubernetes&logoColor=e8a33d" alt="Kubernetes">
  <img src="https://img.shields.io/badge/Terraform-1a1d22?style=for-the-badge&logo=terraform&logoColor=e8a33d" alt="Terraform">
  <img src="https://img.shields.io/badge/SQLite-1a1d22?style=for-the-badge&logo=sqlite&logoColor=e8a33d" alt="SQLite">
  <img src="https://img.shields.io/badge/Playwright-1a1d22?style=for-the-badge&logo=playwright&logoColor=e8a33d" alt="Playwright">
  <img src="https://img.shields.io/badge/Docker-1a1d22?style=for-the-badge&logo=docker&logoColor=e8a33d" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub%20Actions-1a1d22?style=for-the-badge&logo=githubactions&logoColor=e8a33d" alt="GitHub Actions">
</p>

<h3 align="center">Studying now</h3>

<p align="center">
  Web pentesting with the <a href="https://owasp.org/www-project-web-security-testing-guide/">OWASP Web Security Testing Guide</a><br>
  Access control and authentication flaws in APIs (<a href="https://owasp.org/API-Security/editions/2023/en/0x11-t10/">OWASP API Security Top 10:2023</a>)<br>
  Kubernetes and cloud attack paths: RBAC, NetworkPolicy, IAM (<a href="https://kubernetes.io/docs/concepts/security/rbac-good-practices/">RBAC good practices</a>)<br>
  Fixes that hold, and tests that prove they do
</p>
