# Question Answering Agent

def answer_question(material, question):
    print("\n🔎 Q&A Agent is working...")

    material_words = material.lower().split()
    question_words = question.lower().split()

    matching_words = []

    for word in question_words:
        word = word.strip(".,?!")
        if len(word) > 3 and word in material_words:
            matching_words.append(word)

    if matching_words:
        sentences = material.replace("\n", " ").split(".")
        relevant_sentences = []

        for sentence in sentences:
            for word in matching_words:
                if word in sentence.lower():
                    relevant_sentences.append(sentence.strip())
                    break

        if relevant_sentences:
            return " ".join(relevant_sentences[:3])

    return "Sorry, I could not find the answer in the provided course material."