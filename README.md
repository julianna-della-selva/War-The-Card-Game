# 🃏 War – Card Game (Python)

A command-line implementation of the classic **War** card game, built in **Python**. This project simulates a full two-player game (human vs human or human vs bot) using a standard 52-card deck, including recursive **War** rounds for tied cards.

## Project Overview

This project recreates the traditional rules of **War**, where two players draw cards from their decks and compare values. The higher card wins both cards, while ties trigger a special **War round** where players place additional cards face down and continue until a winner is determined.

The goal of the project was to practice **object-oriented programming**, game logic, recursion, and list-based data structures in Python.

## Features

- Full 52-card deck generation and shuffling  
- Interactive name input (human vs human or bot)  
- Automated turn-by-turn gameplay  
- Recursive **War** handling for tied cards  
- Edge case handling when a player lacks enough cards for war  
- Real-time console output showing cards, rounds, and deck sizes  

## Concepts & Skills Demonstrated

- **Object-Oriented Programming**
  - Classes: `Deck`, `Player`, `Round`
  - Encapsulation of game logic
- **Data Structures**
  - Lists used as queues for player hands
- **Algorithms & Logic**
  - Card comparison logic
  - Recursive resolution of consecutive wars
- **Python Fundamentals**
  - Modules (`random`)
  - Input/output handling
  - Control flow and conditionals

## Technologies Used

- **Language:** Python 3  
- **Libraries:**  
  - `random` (for deck shuffling)
- **Tools:**  
  - VS Code / Command Line

## Gameplay Rules Summary

- Each player starts with 26 cards
- Players draw the top card from their deck each round
- Higher card wins both cards
- If cards tie:
    - Each player places three cards face down
    - One card face up determines the winner
    - Process repeats if another tie occurs
- A player wins when the opponent runs out of cards
