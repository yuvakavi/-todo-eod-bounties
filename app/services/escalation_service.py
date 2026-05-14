def escalate_issue(analysis: dict):

    severity = analysis["severity"]

    if severity == "high":

        print("\nHIGH SEVERITY ALERT")
        print(
            f"""
            Escalation Required

            Blocker: {analysis['blocker']}
            Type: {analysis['type']}
            Owner: {analysis['owner']}
            """
        )

    elif severity == "medium":

        print("\nMEDIUM SEVERITY ALERT")

    else:

        print("\nLOW SEVERITY")