# SignalDesk Agent Console Architecture

SignalDesk Agent Console is a safety-first IT triage agent demo built for the Microsoft Agents League Hackathon Reasoning Agents track.

The project simulates how an IT support agent system can route tickets, retrieve grounded support guidance, run health checks, log decisions, and require human approval before risky actions.

## System Flow

1. A user selects a fake IT support ticket.
2. The router reads the ticket category.
3. The router assigns the ticket to a specialist agent.
4. The assigned agent searches the fake knowledge base.
5. The system returns recommended steps with a cited source.
6. A health check confirms that required local resources are available.
7. High-risk tickets trigger a human approval gate.
8. The system logs the routing decision, source, risk level, approval status, and health check result.

## Agent Roles

| Agent  | Purpose                                                                                     |
| ------ | ------------------------------------------------------------------------------------------- |
| Clank  | Handles device troubleshooting, VPN issues, laptop storage, and technical support tasks.    |
| Shield | Handles suspicious emails, security reports, risky actions, and escalation-aware workflows. |
| Docs   | Handles access, policy, Microsoft 365 sign-in, and knowledge base questions.                |

## Core Components

| Component              | File                       | Purpose                                                                     |
| ---------------------- | -------------------------- | --------------------------------------------------------------------------- |
| Ticket data            | `data/tickets.json`        | Stores fake IT support tickets for the demo.                                |
| Knowledge base         | `data/knowledge_base.json` | Stores fictional support guidance and cited sources.                        |
| Agent router           | `app.py`                   | Maps ticket categories to specialist agents.                                |
| Health check           | `app.py`                   | Confirms tickets, knowledge base, and logs folder are available.            |
| Approval gate          | `app.py`                   | Requires approval before proceeding with high-risk actions.                 |
| Audit logging          | `app.py`                   | Writes local JSON logs for each processed ticket.                           |
| Log folder placeholder | `logs/.gitkeep`            | Keeps the logs folder in the public repo without committing generated logs. |

## Safety Design

SignalDesk does not use real customer data, real company data, private logs, credentials, secrets, or proprietary files.

All demo tickets, policies, and knowledge base sources are fictional.

High-risk tickets do not proceed silently. They require human approval before the action continues. If approval is denied, the action is blocked and the ticket is escalated.

## Microsoft IQ / Foundry Fit

SignalDesk is designed to align with Microsoft Foundry and Foundry IQ patterns:

* Grounded answers from a controlled knowledge source
* Routing between task-specific agents
* Cited support guidance
* Reviewable reasoning flow
* Human-in-the-loop control for risky actions
* Reliability checks before task handling

This first version uses a local fake knowledge base so the project remains safe, simple, and demo-ready. A future version could connect the knowledge base retrieval layer to Microsoft Foundry or Foundry IQ.
