import streamlit as st
import random

# Datenbank mit Warm-Up-Spielen
warmup_games = [
    {"name": "Simon Says", "grades": [5, 6], "instructions": "The teacher gives commands (e.g., 'Simon says touch your nose'). Students must only follow commands if they start with 'Simon says'."},
    {"name": "Word Association", "grades": [7, 8, 9], "instructions": "One student says a word, the next must say a related word (e.g., 'sun' -> 'hot')."},
    {"name": "20 Questions", "grades": [6, 7, 8, 9, 10], "instructions": "One student thinks of a word. Others ask yes/no questions to guess it within 20 tries."},
    {"name": "Categories", "grades": [5, 6, 7, 8], "instructions": "The teacher names a category (e.g., animals), and students take turns naming words from that category."},
    {"name": "Spelling Race", "grades": [5, 6], "instructions": "Students form teams. The teacher says a word, and the first team to spell it correctly wins."},
    {"name": "Story Chain", "grades": [7, 8, 9, 10], "instructions": "Each student adds one sentence to a collaborative story, continuing from the last sentence."},
    {"name": "Two Truths and a Lie", "grades": [7, 8, 9, 10], "instructions": "Each student states two true things and one false thing about themselves. Others guess the lie."},
    {"name": "Odd One Out", "grades": [5, 6, 7, 8], "instructions": "The teacher gives a set of 3-4 words. Students must identify which one doesn’t belong and explain why."},
    {"name": "Alphabet Game", "grades": [6, 7, 8], "instructions": "Students go around the room naming words that start with the next letter of the alphabet (e.g., Apple, Banana, Cat)."},
    {"name": "Find Someone Who...", "grades": [5, 6, 7, 8, 9], "instructions": "Each student has a worksheet (e.g., 'Find someone who has a pet'). They walk around asking classmates questions."}
]

# Streamlit-Design
st.set_page_config(page_title="English Warm-Up Generator", layout="centered")
st.title("🎲 English Warm-Up Generator")
st.subheader("Get a random warm-up activity for your class!")

# Klassenstufe auswählen
grade = st.selectbox("Select your class grade:", list(range(5, 11)))

# Warm-Up-Spiel generieren
if st.button("Generate Warm-Up Game 🎮"):
    filtered_games = [game for game in warmup_games if grade in game["grades"]]
    if filtered_games:
        selected_game = random.choice(filtered_games)
        st.success(f"**{selected_game['name']}**")
        st.write(selected_game["instructions"])
    else:
        st.warning("No games found for this grade level.")
