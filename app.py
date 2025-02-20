import streamlit as st
import random

# Datenbank mit Warm-Ups
warm_ups = [
    # Grammatikspiele
    {"name": "Past Tense Challenge", "category": "Grammatik", "grades": [6, 7, 8], "description": "Students take turns forming sentences in past tense. Incorrect sentences are corrected as a group."},
    {"name": "Sentence Builder", "category": "Grammatik", "grades": [5, 6, 7], "description": "One student starts with a word, and each student adds a word to build a grammatically correct sentence."},
    {"name": "Verb Conjugation Race", "category": "Grammatik", "grades": [6, 7, 8, 9], "description": "Students compete in teams to conjugate verbs correctly as quickly as possible."},
    {"name": "Find the Mistake", "category": "Grammatik", "grades": [7, 8, 9, 10], "description": "Students correct mistakes in sentences written on the board."},
    {"name": "Conditionals Challenge", "category": "Grammatik", "grades": [8, 9, 10], "description": "Students form sentences using first, second, and third conditionals based on given prompts."},
    
    # Vokabelspiele
    {"name": "Pictionary", "category": "Vokabeln", "grades": [5, 6, 7, 8], "description": "Students draw vocabulary words while others guess what they are."},
    {"name": "Hot Seat", "category": "Vokabeln", "grades": [6, 7, 8, 9], "description": "One student sits in the 'hot seat' and tries to guess a word their classmates describe."},
    {"name": "Word Association", "category": "Vokabeln", "grades": [5, 6, 7, 8, 9], "description": "Students say words related to a given topic. Repetitions or pauses mean elimination."},
    {"name": "Word Snake", "category": "Vokabeln", "grades": [5, 6, 7, 8], "description": "Each student must say a word that begins with the last letter of the previous word."},
    {"name": "Synonym and Antonym Challenge", "category": "Vokabeln", "grades": [7, 8, 9, 10], "description": "Students provide synonyms or antonyms for given words."},
    
    # Kommunikationsspiele
    {"name": "Speed Dating Conversations", "category": "Kommunikation", "grades": [8, 9, 10], "description": "Students pair up for quick conversations on different topics before switching partners."},
    {"name": "Story Chain", "category": "Kommunikation", "grades": [5, 6, 7, 8], "description": "Each student adds a sentence to a growing story, building on what was said before."},
    {"name": "Interview a Partner", "category": "Kommunikation", "grades": [7, 8, 9, 10], "description": "Students ask each other pre-made or spontaneous interview questions."},
    {"name": "Describe and Draw", "category": "Kommunikation", "grades": [5, 6, 7], "description": "One student describes a picture while another student draws it without seeing the original."},
    {"name": "Role Play Scenarios", "category": "Kommunikation", "grades": [7, 8, 9, 10], "description": "Students act out real-life situations, such as ordering food or asking for directions."},
    
    # Bewegungsspiele
    {"name": "Simon Says", "category": "Bewegung", "grades": [5, 6], "description": "Students must follow commands that start with 'Simon says' but ignore other commands."},
    {"name": "Running Dictation", "category": "Bewegung", "grades": [7, 8, 9], "description": "Students take turns running to a text, memorizing a line, and dictating it to their partner."},
    {"name": "Act it Out", "category": "Bewegung", "grades": [5, 6, 7, 8], "description": "Students act out vocabulary words or phrases while others guess the meaning."},
    {"name": "Four Corners", "category": "Bewegung", "grades": [6, 7, 8], "description": "Each corner of the room represents an answer to a question, and students move to the correct one."},
    {"name": "Vocabulary Relay Race", "category": "Bewegung", "grades": [6, 7, 8, 9], "description": "Students run to the board to write vocabulary words related to a given topic."},
    
    # Denk- und Rätselspiele
    {"name": "20 Questions", "category": "Denken & Rätsel", "grades": [6, 7, 8, 9], "description": "Students ask yes/no questions to guess a mystery word or person."},
    {"name": "Riddle Time", "category": "Denken & Rätsel", "grades": [5, 6, 7, 8], "description": "Students solve English riddles and explain their reasoning."},
    {"name": "Word Jumble", "category": "Denken & Rätsel", "grades": [6, 7, 8, 9, 10], "description": "Students unscramble letters to form correct words."},
    {"name": "Logic Puzzle", "category": "Denken & Rätsel", "grades": [7, 8, 9, 10], "description": "Students solve short logic puzzles in groups."},
    {"name": "Find the Liar", "category": "Denken & Rätsel", "grades": [8, 9, 10], "description": "Each student tells two truths and one lie. The class guesses which statement is false."}
]

# Streamlit UI
st.title("English Warm-Up Generator")
st.sidebar.image("school_logo.png", use_column_width=True)
st.sidebar.write("Created by Mr Übach in collaboration with ChatGPT")

selected_grade = st.sidebar.selectbox("Select Grade", list(range(5, 11)))
selected_category = st.sidebar.selectbox("Select Category", ["Grammatik", "Vokabeln", "Kommunikation", "Bewegung", "Denken & Rätsel"])

if st.button("Generate Warm-Up"):
    filtered_warm_ups = [wu for wu in warm_ups if selected_grade in wu["grades"] and wu["category"] == selected_category]
    if filtered_warm_ups:
        warm_up = random.choice(filtered_warm_ups)
        st.subheader(warm_up["name"])
        st.write(warm_up["description"])
    else:
        st.write("No matching warm-ups found. Try a different category or grade.")
