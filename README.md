# SignalDesk Agent Console

Safety-first IT triage agents that route issues, cite knowledge, log decisions, and require human approval.

## Overview

SignalDesk Agent Console is a small reasoning-agent demo for IT support triage.

It simulates a help desk environment using fake IT tickets and a fictional support knowledge base. When a user selects a ticket, SignalDesk routes the issue to a specialist agent, retrieves grounded guidance, cites the source used, runs health checks, logs the decision, and requires human approval before high-risk actions.

This project was created for the Microsoft Agents League Hackathon.

## Features

* Fake IT ticket triage
* Routed specialist agents
* Grounded knowledge base answers
* Cited fictional support sources
* Health checks
* Human approval gate for high-risk tickets
* Local JSON audit logs
* Public-safe sample data

## Agent Roles

| Agent  | Role                                         |
| ------ | -------------------------------------------- |
| Clank  | Device troubleshooting and technical support |
| Shield | Security reports and risky workflows         |
| Docs   | Policy, access, and knowledge base questions |

## Demo Tickets

The app includes fake tickets for:

* VPN keeps disconnecting
* Suspicious email received
* Cannot sign into Microsoft 365
* Laptop storage almost full
* Password reset policy question

## Project Structure

```text
signaldesk-agent-console/
├─ app.py
├─ data/
│  ├─ tickets.json
│  └─ knowledge_base.json
├─ logs/
│  └─ .gitkeep
├─ architecture.md
├─ README.md
├─ .gitignore
└─ LICENSE
```

## How to Run

Clone the repository, then run:

```bash
python app.py
```

Use the menu to select a ticket.

Run the health check with:

```text
H
```

Quit with:

```text
Q
```

## Demo Flow

1. Select a ticket.
2. SignalDesk classifies the ticket.
3. The router assigns a specialist agent.
4. The agent searches the knowledge base.
5. SignalDesk displays recommended steps with a cited source.
6. Health checks run.
7. High-risk tickets require human approval.
8. A local audit log is written.

## Safety Notes

This project uses fictional sample data only.

It does not include real company data, customer data, credentials, API keys, secrets, private logs, or proprietary files.

Generated log files are ignored by Git. The `logs/.gitkeep` file only keeps the folder visible in the repository.

## Development Note

This project was built by Malik Avery with AI-assisted development support from ChatGPT, Claude, Codex, and GitHub Copilot. All code was reviewed and submitted by the project owner.
