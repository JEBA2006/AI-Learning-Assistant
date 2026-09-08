import streamlit as st

from learning_agent import create_learning_plan
from qa_agent import answer_question
from quiz_agent import generate_quiz


# Page settings
st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🎓",
    layout="centered"
)


# Title
st.title("🎓 AI Learning & Study Assistant")
st.write("Your AI assistant for learning, course materials, and quizzes.")


# Sidebar
st.sidebar.title("📚 Study Assistant")

option = st.sidebar.selectbox(
    "Choose a function",
    [
        "Create Learning Plan",
        "Ask Questions",
        "Generate Quiz"
    ]
)


# ---------------------------------------------------------
# 1. LEARNING PLAN
# ---------------------------------------------------------

if option == "Create Learning Plan":

    st.header("📅 Create Learning Plan")

    topic = st.text_input(
        "Enter the subject or topic",
        placeholder="Example: Machine Learning"
    )

    days = st.number_input(
        "How many days do you want to study?",
        min_value=1,
        max_value=30,
        value=5
    )

    if st.button("Create Plan"):

        if topic:

            plan = create_learning_plan(topic, days)

            st.success("Learning plan created!")

            for item in plan:
                st.write("✅", item)

        else:
            st.warning("Please enter a topic.")


# ---------------------------------------------------------
# 2. QUESTION ANSWERING
# ---------------------------------------------------------

elif option == "Ask Questions":

    st.header("🔎 Ask Questions")

    material = st.text_area(
        "Enter your course material",
        height=250,
        placeholder="Paste your course material here..."
    )

    question = st.text_input(
        "Ask your question",
        placeholder="Example: What is machine learning?"
    )

    if st.button("Get Answer"):

        if material and question:

            answer = answer_question(material, question)

            st.success("Answer")

            st.write(answer)

        else:
            st.warning(
                "Please enter both course material and your question."
            )


# ---------------------------------------------------------
# 3. QUIZ GENERATION
# ---------------------------------------------------------

elif option == "Generate Quiz":

    st.header("📝 Generate Quiz")

    material = st.text_area(
        "Enter your course material",
        height=250,
        placeholder="Paste your course material here..."
    )

    if st.button("Generate Quiz"):

        if material:

            quiz = generate_quiz(material)

            st.success("Quiz generated!")

            for item in quiz:

                st.subheader(item["question"])

                st.write(
                    "💡 Answer:",
                    item["answer"]
                )

        else:
            st.warning("Please enter course material.")