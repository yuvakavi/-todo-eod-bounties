def extract_blocker_info(blocker_text: str):

    blocker_text = blocker_text.lower()

    severity = "low"

    blocker_type = "general"

    owner = "unknown"

    if "pr" in blocker_text:
        blocker_type = "code review"
        owner = "review team"
        severity = "medium"

    if "server" in blocker_text:
        blocker_type = "infrastructure"
        owner = "devops"
        severity = "high"

    if "database" in blocker_text:
        blocker_type = "database"
        owner = "backend team"
        severity = "high"

    return {
        "blocker": blocker_text,
        "type": blocker_type,
        "severity": severity,
        "owner": owner
    }


result = extract_blocker_info(
    "Waiting for PR approval"
)

print(result)