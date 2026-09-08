# Learning Plan Agent

def create_learning_plan(topic, days):
    print("\n📚 Learning Plan Agent is working...")

    try:
        days = int(days)
    except ValueError:
        days = 5

    if days <= 0:
        days = 5

    plan = []

    for day in range(1, days + 1):
        if day == 1:
            task = f"Introduction to {topic}"
        elif day == days:
            task = f"Revision and practice of {topic}"
        else:
            task = f"Study important concepts of {topic} - Part {day - 1}"

        plan.append(f"Day {day}: {task}")

    return plan