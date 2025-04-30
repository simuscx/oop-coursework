# DND Character Creator (OOP Coursework)

A Python-based CLI tool for creating, managing, and storing DND characters using a **Builder Design Pattern**. Customize stats, assign inventory items, and save/load heroes for your next adventure!

## Features
- **Character Creation**: Choose a class, set stats, and define inventory.
- **Builder Pattern**: Step-by-step character construction.
- **Save & Load**: Store characters in JSON and retrieve them later.
- **CLI Interface**: Interactive character management.
- **Unit Testing**: Comprehensive tests ensure reliability for character creation, saving/loading, and inventory management.

## Installation
Ensure you have Python installed, then clone the repo and install dependencies (if any):
```bash
git clone github.com/simuscx/oop-coursework
cd DND-Character-Creator
pip install -r requirements.txt 

## Installation
Ensure you have Python installed, then clone the repo and install dependencies (if any):
```bash
git clone github.com/simuscx/oop-coursework
cd oop-coursework-main
pip install -r requirements.txt (recommended on venv)
```
# Usage

Run the main CLI tool:
```
python CLI.py
```
You'll be prompted to **create or load** characters, set their attributes and manage inventory.
## File breakdown
* main.py – Example implementation of character creation and saving.
* CLI.py – Interactive interface for building/loading characters.
* Character.py – Base character class definitions, CharacterManager class which is responsible for loading and saving characters into .json files.
* Item.py – Defines game items.
* unittest_example.py – Implements unit tests for critical game mechanics

## Unit Testing

This project includes unit tests to verify correct behavior of character creation, inventory management, and file storage.

Run the tests using:
```
python -m unittest unittest_example.py
```
Example unit tests include:
* **Inventory Management** – Ensures items are correctly stored and retrieved.
* **Character Persistence** – Tests saving/loading characters without data loss.
* **Default Stats Handling** – Confirms character stats retain defaults if not explicitly set.
* **Error handling** – Tests loading from nonexistent files.

## Example Character Creation
```
python CLI.py
Do you want to [load] existing characters or [build] new ones? build
Character name: Character1
Character class (Valid classes: Sorcerer, Monk, Rogue, Bard, Barbarian, Paladin, Wizard, Ranger, Fighter, Warlock, Druid, Cleric): Monk
STR (enter to skip): 1
DEX (enter to skip): 1
CON (enter to skip): 1
INT (enter to skip): 1
WIS (enter to skip): 1
CHA (enter to skip): 1
Add item(s)? (y/[d]efault/n): y
Item name: Item1
Description: ItemDesc1
Value: 1
Do you want to create more items? N
Create another character? (y/n): N
Save to file (default: characters.json): TestCharacter1

Character data saved to TestCharacter1.json

Saved 1 character(s) to TestCharacter1.json
```
## Example Character Loading
```
python CLI.py
Do you want to [load] existing characters or [build] new ones? load
Enter file to load characters from (e.g. hero.json): TestCharacter1 (both work, TestCharacter1
and TestCharacter1.json)

Loaded 1 character(s):

1. Monk Character1 with stats {'STR': 1, 'DEX': 1, 'CON': 1, 'INT': 1, 'WIS': 1, 'CHA': 1}. Inventory: ['Item1']
```
# Contributing?
I made this project for an university coursework, but if you want to expand the project – fork the repo, make improvements and submit a PR! :)