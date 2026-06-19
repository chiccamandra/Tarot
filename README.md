# Oracles: Tarot & I Ching Simulators 🃏🔮☯️

Welcome to **Oracles**, a collection of lightweight Python command-line tools designed to simulate ancient divination systems. 

This repository serves as a personal coding milestone, demonstrating how foundational programming concepts—such as lists, dictionaries, nested loops, and input validation—can map complex, traditional symbolic frameworks into clean execution logic.

---

## 🃏 1. Tarot Reader (`tarot_reader.py`)

A dynamic simulator that generates a complete Tarot deck and executes a classic 3-card spread ("Past, Present, Future").

### ✨ Features
* **Dual Deck System:** Users can choose to draw from the 22 Major Arcana only (using traditional French names) or the Full 78-card deck.
* **Automated Generation:** The 56 Minor Arcana are dynamically generated on the fly using a Cartesian product (nested loops) to pair values and suits into a custom dictionary.
* **Input Validation:** A robust `while` loop prevents terminal crashes by continuously prompting the user until a valid choice (`1` or `2`) is entered.
* **Duplicate-Free Drawing:** Uses Python's `random.sample` to guarantee that the same card cannot be drawn twice in a single reading.

---

## ☯️ 2. I Ching Hexagram Generator (`iching_generator.py`)

A mathematical approach to the structure of the *I Ching* (The Book of Changes), generating the 64 foundational hexagrams from the ground up.

### ✨ Features
* **Trigram Architecture:** Reflecting traditional philosophy, the script first generates the 8 primary trigrams (combinations of 3 solid or broken lines) using a 3-level nested loop.
* **Matrix Coupling (8x8):** It combines a lower and an upper trigram through dual loops, pairing them automatically to create the complete set of 64 unique 6-line hexagrams.
* **Pure Logic Mapping:** Uses explicit array structures (`7` for solid lines, `8` for broken lines) to prepare a clean database for future randomized divination scripts.

---

## 🚀 How to Run the Scripts

To try out any of the simulators, make sure you have Python installed, open your terminal within this directory, and run:

```bash
# To run the Tarot Reader
python tarot_reader.py

# To run the I Ching Generator
python iching_generator.py
