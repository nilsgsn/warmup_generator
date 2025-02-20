import streamlit as st
import random

# Datenbank mit Warm-Ups
warm_ups = [
    {"name": "Simon Says", "category": "Movement", "grades": [5, 6], "instructions": "The teacher gives commands, but students should only follow them if they start with 'Simon says'."},
    {"name": "20 Questions", "category": "Thinking & Puzzles", "grades": [7, 8, 9, 10], "instructions": "One student thinks of an object, and others can ask up to 20 yes/no questions to guess it."},
    {"name": "Word Association", "category": "Vocabulary", "grades": [6, 7, 8, 9], "instructions": "Students take turns saying words that are connected to the previous word."},
    {"name": "Two Truths and a Lie", "category": "Communication", "grades": [7, 8, 9, 10], "instructions": "Each student says two true statements and one false one; classmates guess the lie."},
    {"name": "Find Someone Who...", "category": "Communication", "grades": [5, 6, 7], "instructions": "Students walk around and find classmates who fit given descriptions (e.g., 'has a pet')."},
    {"name": "Running Dictation", "category": "Movement", "grades": [6, 7, 8, 9], "instructions": "A text is posted on the wall. One student runs, reads, and dictates it to a partner."},
    {"name": "Spelling Relay", "category": "Vocabulary", "grades": [5, 6, 7], "instructions": "Students race to spell words correctly by passing a letter from teammate to teammate."},
    {"name": "Grammar Auction", "category": "Grammar", "grades": [8, 9, 10], "instructions": "Sentences are 'auctioned' off, and students bid on the correct ones."},
    {"name": "Broken Telephone", "category": "Communication", "grades": [5, 6, 7], "instructions": "A whispered message travels down a line of students; the last one says it aloud."},
    {"name": "Pictionary", "category": "Vocabulary", "grades": [5, 6, 7, 8, 9, 10], "instructions": "Students draw vocabulary words while others guess."},
    {"name": "Story Cubes", "category": "Thinking & Puzzles", "grades": [7, 8, 9, 10], "instructions": "Students roll dice with images and create a story using all images."},
    {"name": "Charades", "category": "Movement", "grades": [5, 6, 7, 8], "instructions": "A student acts out a word while others guess."},
    {"name": "Odd One Out", "category": "Thinking & Puzzles", "grades": [6, 7, 8, 9, 10], "instructions": "Students find the unrelated word in a group of four words."},
    {"name": "Hot Seat", "category": "Vocabulary", "grades": [6, 7, 8, 9], "instructions": "One student sits with their back to the board while classmates describe a word for them to guess."},
    {"name": "Would You Rather...?", "category": "Communication", "grades": [5, 6, 7, 8, 9, 10], "instructions": "Students answer fun 'Would you rather' questions and explain their choices."},
    {"name": "Memory Chain", "category": "Thinking & Puzzles", "grades": [5, 6, 7, 8], "instructions": "Each student repeats previous words in order and adds a new one to the list."},
    {"name": "Secret Word", "category": "Vocabulary", "grades": [6, 7, 8, 9], "instructions": "A student describes a secret word without saying it, and others guess."},
    {"name": "Word Ladders", "category": "Vocabulary", "grades": [7, 8, 9, 10], "instructions": "Students change one letter at a time to transform a word into another."},
    {"name": "Sentence Building Relay", "category": "Grammar", "grades": [6, 7, 8], "instructions": "Each student adds a word to build a correct sentence in a relay race format."},
]

# Streamlit UI
st.set_page_config(page_title="English Warm-Up Generator", layout="centered")
st.title("English Warm-Up Generator")
st.subheader("created by Mr Übach in collaboration with ChatGPT")

# Schul-Logo hinzufügen
st.image("school_logo.png", width=200)

# Auswahlfelder
selected_grade = st.selectbox("Select Grade:", [5, 6, 7, 8, 9, 10])
selected_category = st.selectbox("Select Category:", ["All", "Vocabulary", "Grammar", "Communication", "Movement", "Thinking & Puzzles"])

# Spielauswahl per Knopfdruck
def get_random_warm_up():
    filtered_warm_ups = [w for w in warm_ups if selected_grade in w["grades"] and (selected_category == "All" or w["category"] == selected_category)]
    return random.choice(filtered_warm_ups) if filtered_warm_ups else None

if st.button("Generate Warm-Up"):
    warm_up = get_random_warm_up()
    if warm_up:
        st.write(f"### {warm_up['name']}")
        st.write(f"**Category:** {warm_up['category']}")
        st.write(f"**Instructions:** {warm_up['instructions']}")
    else:
        st.write("No warm-up available for this selection.")
