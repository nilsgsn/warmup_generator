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
    {"name": "Vocabulary Treasure Hunt", "category": "Vocabulary", "grades": [5, 6, 7], "instructions": "Students search the classroom for hidden vocabulary cards."},
    {"name": "Four Corners (Opinion Game)", "category": "Communication", "grades": [7, 8, 9, 10], "instructions": "Students go to a corner of the room that corresponds to their opinion on a statement."},
    {"name": "Act It Out (Charades)", "category": "Movement", "grades": [5, 6, 7, 8, 9, 10], "instructions": "A student acts out a word while others guess."},
    {"name": "Human Word Scramble", "category": "Movement", "grades": [6, 7, 8], "instructions": "Students form letters with their bodies to create words."},
    {"name": "Stand Up If…", "category": "Communication", "grades": [5, 6, 7, 8], "instructions": "Students stand up when a statement applies to them."},
    {"name": "Ball Toss Q&A", "category": "Communication", "grades": [5, 6, 7, 8, 9, 10], "instructions": "Students toss a ball to each other and ask questions when they catch it."},
    {"name": "Jump the Line (True or False)", "category": "Movement", "grades": [6, 7, 8, 9, 10], "instructions": "Students jump over a line if they think a statement is true or false."},

    # Neue Warm-Ups
    {"name": "Hangman", "category": "Thinking & Puzzles", "grades": [5, 6, 7], "instructions": "One student thinks of a word, and others guess letters to figure it out before the hangman is complete."},
    {"name": "Word Chains", "category": "Vocabulary", "grades": [6, 7, 8, 9, 10], "instructions": "Students create chains of words where each new word starts with the last letter of the previous word."},
    {"name": "Alphabet Race", "category": "Movement", "grades": [5, 6, 7], "instructions": "Students search the classroom for items that start with the letters of the alphabet."},
    {"name": "Speed Vocab Challenge", "category": "Vocabulary", "grades": [6, 7, 8, 9, 10], "instructions": "Students must quickly name words in specific categories."},
    {"name": "Past Tense Bingo", "category": "Grammar", "grades": [6, 7, 8], "instructions": "Students receive bingo cards with verbs in infinitive form and must form the past tense when the verb is called."},
    {"name": "Find the Mistake", "category": "Grammar", "grades": [7, 8, 9, 10], "instructions": "Students read sentences and identify grammatical errors."},
    {"name": "Verb Conjugation Race", "category": "Grammar", "grades": [5, 6, 7], "instructions": "Students conjugate verbs as quickly as possible in different tenses."},
    {"name": "Who Am I? (Question Formation)", "category": "Communication", "grades": [6, 7, 8, 9], "instructions": "One student thinks of a person, and others ask yes/no questions to find out who it is."},
    {"name": "Preposition Simon Says", "category": "Movement", "grades": [5, 6, 7], "instructions": "Like 'Simon Says', but with instructions that include prepositions that students must use."},
    {"name": "Irregular Verb Snap", "category": "Grammar", "grades": [6, 7, 8], "instructions": "Students lay down cards with irregular verbs and shout 'Snap' when two of the same verbs are revealed."},
    {"name": "Describe and Draw", "category": "Communication", "grades": [5, 6, 7, 8, 9, 10], "instructions": "One student describes a picture while another draws it."},
    {"name": "Roleplay Scenarios", "category": "Communication", "grades": [7, 8, 9, 10], "instructions": "Students act out different scenarios to practice conversation."},
    {"name": "The Whisper Challenge", "category": "Communication", "grades": [5, 6, 7, 8], "instructions": "A whispered sentence is passed down a line of students; the last one says it out loud."},
    {"name": "What’s Missing? (Memory Game)", "category": "Thinking & Puzzles", "grades": [5, 6, 7], "instructions": "Students memorize items on a tray that is shown briefly, then covered. They must say what is missing."},
]

# Streamlit UI
st.set_page_config(page_title="Warm-Up Generator", layout="centered")
st.title("🎲 Warm-Up Generator")

# Hintergrundfarbe setzen
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: rgb(240, 240, 240); /* Hellgrau als Hintergrund */
    }
    .stButton > button {
        background-color: rgb(0, 171, 215); /* Blau für den Button */
        color: white; /* Weiße Schrift für den Button */
    }
    h1 {
        color: rgb(0, 171, 215); /* Titel in Blau */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Zentrierte Auswahlfelder
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
selected_grade = st.selectbox("Select Grade:", [5, 6, 7, 8, 9, 10], index=0)
selected_category = st.selectbox("Select Category:", ["All", "Vocabulary", "Grammar", "Communication", "Movement", "Thinking & Puzzles"], index=0)
st.markdown("</div>", unsafe_allow_html=True)

# Spielauswahl per Knopfdruck
def get_random_warm_up():
    filtered_warm_ups = [w for w in warm_ups if selected_grade in w["grades"] and (selected_category == "All" or w["category"] == selected_category)]
    return random.choice(filtered_warm_ups) if filtered_warm_ups else None

# Zentrierter Button
if st.button("Generate Warm-Up", key="generate_button"):
    warm_up = get_random_warm_up()
    if warm_up:
        st.markdown(f"<h3 style='text-align: center;'>{warm_up['name']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'><strong>Category:</strong> {warm_up['category']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'><strong>Instructions:</strong> {warm_up['instructions']}</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='text-align: center;'>No warm-up available for this selection.</p>", unsafe_allow_html=True)

# Hinweis ganz unten
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Fügt Platz ein
st.markdown("<p style='text-align: center; font-size: smaller;'>created by Mr Übach in collaboration with ChatGPT</p>", unsafe_allow_html=True)

# Schul-Logo hinzufügen, zentriert und klein
st.markdown(
    "<div style='text-align: center;'><img src='main/school_logo.png' style='max-width: 100px; width: auto; height: auto;'></div>",
    unsafe_allow_html=True
)
