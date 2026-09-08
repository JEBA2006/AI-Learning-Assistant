# Quiz Generation Agent

def generate_quiz(material):
    print("\n📝 Quiz Agent is working...")

    sentences = [
        sentence.strip()
        for sentence in material.replace("\n", " ").split(".")
        if len(sentence.strip()) > 20
    ]

    quiz = []

    for i, sentence in enumerate(sentences[:5], start=1):
        words = sentence.split()

        if len(words) >= 5:
            answer = words[-1].strip(".,!?")

            question = (
                f"Question {i}: Complete the following statement:\n"
                f'"{sentence.rsplit(" ", 1)[0]} ______"'
            )

            quiz.append({
                "question": question,
                "answer": answer
            })

    if not quiz:
        quiz.append({
            "question": "No sufficient material was provided to create a quiz.",
            "answer": "N/A"
        })

    return quiz