import random
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

# Warm-Up-Spiele Datenbank
warmup_games = {
    "5": ["Simon Says", "Hangman", "Alphabet Race"],
    "6": ["Simon Says", "20 Questions", "Word Association"],
    "7": ["Taboo", "Speed Dating", "Story Relay"],
    "8": ["Debate Battle", "Sentence Race", "Two Truths and a Lie"],
    "9": ["Improv Speech", "Mafia Game", "Would You Rather"],
    "10": ["Roleplay Scenarios", "Fake News Detector", "Desert Island"],
}

# Spielanleitungen
instructions = {
    "Simon Says": "The teacher gives commands starting with 'Simon says'. If 'Simon says' is not used, students must not follow the command.",
    "Hangman": "Students guess letters to form a word before the stick figure is completed.",
    "Alphabet Race": "Students take turns saying words in alphabetical order.",
    "20 Questions": "One student thinks of a word, others ask yes/no questions to guess it.",
    "Word Association": "Each student must say a word related to the previous word.",
    "Taboo": "Students describe a word without using specific 'taboo' words.",
    "Speed Dating": "Students have quick conversations on given topics, then switch partners.",
    "Story Relay": "Each student continues a story with one sentence.",
    "Debate Battle": "Students are given a topic and must argue for or against it.",
    "Sentence Race": "Teams race to write grammatically correct sentences from given words.",
    "Two Truths and a Lie": "Students say three statements, two true and one false. Others guess the lie.",
    "Improv Speech": "Students pick a random topic and give a 1-minute speech.",
    "Mafia Game": "A storytelling game where 'mafia' try to eliminate others without being caught.",
    "Would You Rather": "Students choose between two difficult choices and explain why.",
    "Roleplay Scenarios": "Students act out real-life scenarios using English.",
    "Fake News Detector": "Students analyze headlines and decide if they are real or fake.",
    "Desert Island": "Students list items they would take to a desert island and justify their choices."
}

# Funktion zur Auswahl eines Warm-Ups
def select_warmup():
    level = class_level.get()
    if level in warmup_games:
        game = random.choice(warmup_games[level])
        instruction_text.set(f"Game: {game}\n\nInstructions: {instructions[game]}")
    else:
        instruction_text.set("No games available for this grade level.")

# GUI erstellen
root = tb.Window(themename="superhero")  # Modernes Theme
root.title("English Warm-Up Generator")
root.geometry("500x400")

# UI-Elemente
tb.Label(root, text="Select Class Level:", font=("Arial", 14)).pack(pady=10)
class_level = tb.Combobox(root, values=list(warmup_games.keys()), font=("Arial", 12))
class_level.pack()
class_level.current(0)

generate_button = tb.Button(root, text="Generate Warm-Up", command=select_warmup, bootstyle="primary")
generate_button.pack(pady=20)

instruction_text = tk.StringVar()
result_label = tb.Label(root, textvariable=instruction_text, wraplength=450, font=("Arial", 12))
result_label.pack(pady=10)

# Hauptloop starten
root.mainloop()
