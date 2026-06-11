import json
import os
from datetime import datetime, timezone
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


TICKETS = load_json(DATA_DIR / "tickets.json")
KNOWLEDGE_BASE = load_json(DATA_DIR / "knowledge_base.json")


AGENT_MAP = {
    "device": {
        "agent": "Clank",
        "reason": "Device and troubleshooting issues should be handled by the technical support agent."
    },
    "security": {
        "agent": "Shield",
        "reason": "Security reports need safer handling, approval checks, and escalation awareness."
    },
    "access": {
        "agent": "Docs",
        "reason": "Access issues often depend on documented sign-in and account support steps."
    },
    "policy": {
        "agent": "Docs",
        "reason": "Policy questions should be answered from grounded support documentation."
    }
}


def route_ticket(ticket):
    category = ticket.get("category", "unknown")
    route = AGENT_MAP.get(category, AGENT_MAP["policy"])
    return route["agent"], category, route["reason"]


def search_knowledge_base(category):
    for entry in KNOWLEDGE_BASE:
        if entry.get("category") == category:
            return entry
    return None


def run_health_check():
    checks = {
        "tickets_loaded": len(TICKETS) > 0,
        "knowledge_base_loaded": len(KNOWLEDGE_BASE) > 0,
        "logs_folder_exists": LOGS_DIR.exists()
    }
    all_pass = all(checks.values())
    return checks, all_pass


def write_log(ticket, agent, category, route_reason, kb_entry, approved, health_status):
    LOGS_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now(timezone.utc).isoformat()
    safe_timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")

    log_entry = {
        "timestamp_utc": timestamp,
        "ticket_id": ticket["id"],
        "title": ticket["title"],
        "category": category,
        "assigned_agent": agent,
        "route_reason": route_reason,
        "risk": ticket["risk"],
        "approved": approved,
        "health_check_passed": health_status,
        "knowledge_base_id": kb_entry["id"] if kb_entry else "None",
        "source_cited": kb_entry["source"] if kb_entry else "None"
    }

    log_path = LOGS_DIR / f"{ticket['id']}_{safe_timestamp}.json"

    with open(log_path, "w", encoding="utf-8") as file:
        json.dump(log_entry, file, indent=2)

    print(f"\n  [LOG] Entry written to {log_path}")


def request_approval(ticket):
    print("\n  APPROVAL REQUIRED")
    print(f"  Ticket: {ticket['title']}")
    print(f"  Risk level: {ticket['risk'].upper()}")
    print("  Reason: This ticket may involve security-sensitive action.")

    answer = input("\n  Approve this action? (yes/no): ").strip().lower()
    return answer == "yes"


def show_ticket_menu():
    print("\n" + "=" * 60)
    print("  SignalDesk Agent Console")
    print("  Safety-first IT Triage Agent")
    print("=" * 60)
    print("\n  Select a ticket:\n")

    for index, ticket in enumerate(TICKETS, 1):
        print(f"  [{index}] {ticket['title']}")

    print("\n  [H] Run health check")
    print("  [Q] Quit")
    print()


def display_health_check():
    checks, all_pass = run_health_check()

    print("\n  HEALTH CHECK:")
    for key, value in checks.items():
        status = "PASS" if value else "FAIL"
        print(f"  [{status}] {key}")

    print(f"\n  Status: {'ALL SYSTEMS OK' if all_pass else 'ISSUES DETECTED'}\n")
    return all_pass


def process_ticket(ticket):
    print("\n" + "-" * 60)
    print(f"  TICKET: {ticket['id']} - {ticket['title']}")
    print(f"  {ticket['description']}")
    print("-" * 60)

    health_passed = display_health_check()

    agent, category, route_reason = route_ticket(ticket)

    print(f"\n  [ROUTER] Category: {category.upper()}")
    print(f"  [ROUTER] Assigned agent: {agent}")
    print(f"  [ROUTER] Reason: {route_reason}")

    kb_entry = search_knowledge_base(category)

    if kb_entry:
        print(f"\n  [{agent}] Searching knowledge base...")
        print(f"  [{agent}] Found: {kb_entry['title']}")
        print("\n  RECOMMENDED STEPS:")
        print(f"  {kb_entry['content']}")
        print(f"\n  SOURCE: {kb_entry['source']}")
    else:
        print(f"\n  [{agent}] No knowledge base entry found for this category.")

    approved = True

    if ticket["risk"] == "high":
        approved = request_approval(ticket)

        if not approved:
            print("\n  [BLOCKED] Action was not approved. Ticket escalated.")
        else:
            print("\n  [APPROVED] Proceeding with recommended steps.")

    write_log(
        ticket=ticket,
        agent=agent,
        category=category,
        route_reason=route_reason,
        kb_entry=kb_entry,
        approved=approved,
        health_status=health_passed
    )

    print("\n  [DONE] Ticket processed.\n")


def main():
    while True:
        show_ticket_menu()
        choice = input("  Enter your choice: ").strip().upper()

        if choice == "Q":
            print("\n  Goodbye.\n")
            break

        if choice == "H":
            display_health_check()
            continue

        if choice.isdigit() and 1 <= int(choice) <= len(TICKETS):
            ticket = TICKETS[int(choice) - 1]
            process_ticket(ticket)
            continue

        print("\n  Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()