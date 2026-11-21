<img src="assets/banner.svg" alt="TroubieD3v: I break web apps on purpose, then make sure the fix holds." width="100%">

<p align="center">
  Application and infrastructure security, learned hands-on: write the vulnerable version, exploit it, fix it,<br>
  then prove the same attack no longer works. Everything I build for that is open source and runs locally.
</p>

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/TroubieD3v/WebSec-Lab"><img src="assets/card-websec-lab.svg" alt="WebSec-Lab: break vulnerable code, watch the fix hold, verify both automatically" width="100%"></a>
      <p>Twelve labs from SQL injection and XSS to JWT forgery and race conditions. Each runs the vulnerable code and
      its fix side by side, shows the diff, and checks on the server that your attack lands on one and fails on the other.</p>
      <p><a href="https://github.com/TroubieD3v/WebSec-Lab"><b>Repository</b></a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/WebSec-Lab#quick-start-docker">Quick start</a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/WebSec-Lab/releases/latest"><img src="https://img.shields.io/github/v/release/TroubieD3v/WebSec-Lab?style=flat-square&label=release&labelColor=000000&color=5c5c5c" alt="Latest WebSec-Lab release" align="absmiddle"></a></p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/TroubieD3v/AuthScope"><img src="assets/card-authscope.svg" alt="AuthScope: finds authorization bugs in REST APIs by checking who can really reach what" width="100%"></a>
      <p>Import OpenAPI or Postman, add test accounts, say who owns which objects. AuthScope compares real responses with
      your policy, so <code>200 []</code> is not a finding, and every violation comes with both requests and a curl to reproduce it.</p>
      <p><a href="https://github.com/TroubieD3v/AuthScope"><b>Repository</b></a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/AuthScope#quick-start-docker">Quick start</a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/AuthScope/releases/latest"><img src="https://img.shields.io/github/v/release/TroubieD3v/AuthScope?style=flat-square&label=release&labelColor=000000&color=5c5c5c" alt="Latest AuthScope release" align="absmiddle"></a></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/TroubieD3v/CloudGraph"><img src="assets/card-cloudgraph.svg" alt="CloudGraph: explains how small misconfigurations chain into an attack path" width="100%"></a>
      <p>Reads Docker Compose, Kubernetes and Terraform plans offline and builds a graph of who can reach what. It shows how
      an exposed pod, a mounted token and a broad role add up to a path to your secrets, traces every step to a line of
      config, and simulates which fix breaks the most chains before you touch a file.</p>
      <p><a href="https://github.com/TroubieD3v/CloudGraph"><b>Repository</b></a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/CloudGraph#quick-start-docker">Quick start</a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/CloudGraph/releases/latest"><img src="https://img.shields.io/github/v/release/TroubieD3v/CloudGraph?style=flat-square&label=release&labelColor=000000&color=5c5c5c" alt="Latest CloudGraph release" align="absmiddle"></a></p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/TroubieD3v/AgentShield"><img src="assets/card-agentshield.svg" alt="AgentShield: tests what AI agents actually do, not just what they say" width="100%"></a>
      <p>Tests the whole agent, not just the model: which tools it calls, which data it touches, whose instruction it
      follows. It replays prompt injection, memory poisoning and data leaks against sandbox agents with mock tools,
      records the full trace, and shows the same attack recorded in Monitor mode and blocked in Enforce mode.</p>
      <p><a href="https://github.com/TroubieD3v/AgentShield"><b>Repository</b></a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/AgentShield#quick-start-docker">Quick start</a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/AgentShield/releases/latest"><img src="https://img.shields.io/github/v/release/TroubieD3v/AgentShield?style=flat-square&label=release&labelColor=000000&color=5c5c5c" alt="Latest AgentShield release" align="absmiddle"></a></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/TroubieD3v/SupplyChainRadar"><img src="assets/card-supplychain-radar.svg" alt="SupplyChain Radar: shows why a vulnerable package is in your project and which upgrade fixes it" width="100%"></a>
      <p>Reads lockfiles and SBOMs without ever running them, builds the real dependency graph and matches every resolved
      package against OSV advisories. Each finding shows the path that brought the package in and the lockfile line behind
      every hop. A package that was not evaluated is never reported as clean, and a what-if mode compares an upgrade
      before you touch a file.</p>
      <p><a href="https://github.com/TroubieD3v/SupplyChainRadar"><b>Repository</b></a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/SupplyChainRadar#60-second-quickstart">Quick start</a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/SupplyChainRadar/releases/latest"><img src="https://img.shields.io/github/v/release/TroubieD3v/SupplyChainRadar?style=flat-square&label=release&labelColor=000000&color=5c5c5c" alt="Latest SupplyChainRadar release" align="absmiddle"></a></p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/TroubieD3v/RLS-Sentinel"><img src="assets/card-rls-sentinel.svg" alt="RLS Sentinel: proves what PostgreSQL row-level security really lets each role do" width="100%"></a>
      <p>Turns "tenant A must not see tenant B" into real SQL run as each role inside a throwaway PostgreSQL, and records
      what the database actually did: which gate stopped it, which policies applied, and why. Anything it cannot prove
      stays inconclusive, never "safe". A live database is only ever read, a what-if lab replays a policy change before you ship it, and a generated
      schema of 1 000 tables and 10 000 policies runs end to end in under 30 seconds.</p>
      <p><a href="https://github.com/TroubieD3v/RLS-Sentinel"><b>Repository</b></a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/RLS-Sentinel#quick-start">Quick start</a> &nbsp;·&nbsp;
      <a href="https://github.com/TroubieD3v/RLS-Sentinel/releases/latest"><img src="https://img.shields.io/github/v/release/TroubieD3v/RLS-Sentinel?style=flat-square&label=release&labelColor=000000&color=5c5c5c" alt="Latest RLS-Sentinel release" align="absmiddle"></a></p>
    </td>
  </tr>
</table>

<h4 align="center">One idea, six layers</h4>

| Layer | Project | The question it answers |
| :-- | :-- | :-- |
| **Code** | [WebSec-Lab](https://github.com/TroubieD3v/WebSec-Lab) | Does the fix refuse the exact request that exploited the bug? |
| **API** | [AuthScope](https://github.com/TroubieD3v/AuthScope) | Can this user reach that object, judged against your own access policy? |
| **Infrastructure** | [CloudGraph](https://github.com/TroubieD3v/CloudGraph) | How does one bug become a path to the crown jewels, and which change cuts it? |
| **AI agents** | [AgentShield](https://github.com/TroubieD3v/AgentShield) | What does an agent with tools and memory do when untrusted text tells it to misbehave? |
| **Supply chain** | [SupplyChain Radar](https://github.com/TroubieD3v/SupplyChainRadar) | Which parent brought this vulnerable package in, and which upgrade really removes it? |
| **Database** | [RLS Sentinel](https://github.com/TroubieD3v/RLS-Sentinel) | Does row-level security keep every tenant in its own rows, role by role and command by command? |

<p align="center">
  All six report evidence rather than guesses, separate "proven" from "possible", and ship a vulnerable and a
  hardened version so the tests can show both.
</p>

<details>
  <summary><b>See them in action</b></summary>
  <br>
  <p><b>WebSec-Lab</b>: Alice reads Bob's booking in the vulnerable mode; in the fixed mode the same request is refused.</p>
  <img src="https://github.com/TroubieD3v/WebSec-Lab/raw/main/docs/screenshots/demo.gif" alt="WebSec-Lab demo" width="100%">
  <p><b>AuthScope</b>: a run against the demo API, the permission matrix, and the evidence for one finding.</p>
  <img src="https://github.com/TroubieD3v/AuthScope/raw/main/docs/screenshots/demo.gif" alt="AuthScope demo" width="100%">
  <p><b>CloudGraph</b>: attack paths in an insecure cluster, one highlighted in the graph, a what-if fix that removes four, and a diff against the hardened version.</p>
  <img src="https://github.com/TroubieD3v/CloudGraph/raw/main/docs/screenshots/demo.gif" alt="CloudGraph demo" width="100%">
  <p><b>AgentShield</b>: one prompt injection recorded in Monitor mode and blocked in Enforce mode, then the agent trace and a before/after comparison.</p>
  <img src="https://github.com/TroubieD3v/AgentShield/raw/main/docs/screenshots/demo.gif" alt="AgentShield demo" width="100%">
  <p><b>SupplyChain Radar</b>: every path from the app to a vulnerable shared dependency highlighted in the graph, then the finding with its evidence and the upgrade that fixes it. Demo data is synthetic and labelled as such.</p>
  <img src="https://github.com/TroubieD3v/SupplyChainRadar/raw/main/docs/screenshots/graph.png" alt="SupplyChain Radar dependency graph" width="100%">
  <img src="https://github.com/TroubieD3v/SupplyChainRadar/raw/main/docs/screenshots/finding-detail.png" alt="SupplyChain Radar finding detail" width="100%">
  <p><b>RLS Sentinel</b>: the vulnerable fixture finds 8 cross-tenant leaks, the evidence for one shows which gate let it through, a what-if fix removes two in a sandbox without regressions, and the secure variant finds none. All data is synthetic.</p>
  <img src="https://github.com/TroubieD3v/RLS-Sentinel/raw/main/docs/assets/demo.gif" alt="RLS Sentinel demo" width="100%">
</details>

<h3 align="center">Toolbox</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Go-000000?style=for-the-badge&logo=go&logoColor=white" alt="Go">
  <img src="https://img.shields.io/badge/FastAPI-000000?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/TypeScript-000000?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/React-000000?style=for-the-badge&logo=react&logoColor=white" alt="React">
  <img src="https://img.shields.io/badge/Tailwind-000000?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS">
  <br>
  <img src="https://img.shields.io/badge/Kubernetes-000000?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes">
  <img src="https://img.shields.io/badge/Terraform-000000?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform">
  <img src="https://img.shields.io/badge/SQLite-000000?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/PostgreSQL-000000?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Redis-000000?style=for-the-badge&logo=redis&logoColor=white" alt="Redis">
  <img src="https://img.shields.io/badge/Playwright-000000?style=for-the-badge&logo=playwright&logoColor=white" alt="Playwright">
  <img src="https://img.shields.io/badge/Docker-000000?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub%20Actions-000000?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

<h3 align="center">Studying now</h3>

| Studying | Reference | Where it shows up |
| :-- | :-- | :-- |
| Web pentesting | [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) | WebSec-Lab |
| Access control and authentication flaws in APIs | [OWASP API Security Top 10:2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) | AuthScope |
| Kubernetes and cloud attack paths: RBAC, NetworkPolicy, IAM | [RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/) | CloudGraph |
| Security of LLM apps and AI agents | [OWASP GenAI: LLM and Agentic Top 10](https://genai.owasp.org/) | AgentShield |
| Dependency risk and SBOMs | [OSV](https://osv.dev/) · [OpenSSF](https://openssf.org/) | SupplyChain Radar |
| Multi-tenant isolation in PostgreSQL | [Row security policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) | RLS Sentinel |

<p align="center"><i>Fixes that hold, and tests that prove they do.</i></p>
