# 🧙 DND Character Creator

## 1. Introduction

### What is your application?
The **DND Character Creator** is a Python-based CLI application designed to help players build, manage, and store their DND characters. Using the **Builder Design Pattern**, players can create characters with customizable stats, inventory, and class selection. The program also allows saving and loading characters via JSON for persistent gameplay.

### How to run the program?
Ensure Python is installed, then clone the repository and navigate to the project directory:
```bash
git clone github.com/simuscx/oop-coursework
cd oop-coursework-main
python3 -m venv venv
activate venv
pip install -r requirements.txt  # If needed
```
### Run the CLI:
```
python CLI.py
```
### How to use the program?
Upon running the CLI, users are prompted to either build a new character or load existing ones from a saved JSON file (for longer campaigns), The creating process involves:
* Choosing a name.
* Selecting a class from available options.
* Setting character stats (or using defaults).
* Adding custom inventory items (optional).
* Saving the character for future use.

## 2. Body/Analysis

### How does the program implement functional requirements? 
#### Use of Git and GitHub:
The entire project, including all source files and the Markdown-formatted README, is stored in a GitHub repository (hi :)), ensuring version control and accessibility

#### Implementation of OOP principles:
This project follows four key object-oriented programming (OOP) pillars:
* Polymorphism: The **Character** class defines an abstract method **special_ability()** that is implemented differently across subclasses.
```
@abc.abstractmethod
def special_ability(self) -> str:
    pass

class Barbarian(Character):
    def special_ability(self) -> str:
        return "Rage: Unleash devastating attacks with increased strength!"
```
* Abstraction: the **Character** class serves as an abstract base class, encapsulating common attributes while requiring subclasses to define specific behavior.
* Inheritance: Character subclasses (**Barbarian, Wizard, Rogue**, etc.) inherit from the *Character* base class, reusing existing functionality.
* Encapsulation: the **_inventory** attribute is private, ensuring that character inventories are properly managed without external modification.

#### Design Pattern: Builder:
The project uses the **Builder Design Pattern** to construct characters in a structured manner:
```
builder = CharacterBuilder()
hero = builder.set_name("Character1").set_class("Monk").set_stats({"STR": 1}).build()
```
This pattern allows for **step-by-step object creation**, ensuring a consistent structure across different character types.

#### Composition & Aggregation:
* **Composition:** the **Character** class includes an **_inventory** list of **Item** objects, ensuring that items belong to characters.
* **Aggregation:** the **CharacterManager** class aggregates multiple characters, managing their storage and retrieval.

### Reading & Writing to Files:
Characters are saved and loaded using **JSON file storage:**
```
CharacterManager.save_characters([hero, bard], "characters.json")
loaded_characters = CharacterManager.load_characters("characters.json")
```
This ensures persistence across game sessions, for further context look into **load_character** and **save_character** in the class of **CharacterManager** (Character.py)

### Unit Testing
Core functionality is tested using **unittest**, covering:
* **Inventory Management:** Ensures items are correctly stored and retrieved
* **Character Persistence:** Verifies saving/loading maintains data integrity.
* **Default Stats Handling:** Confirms missing stats are assigned default values
* **Error Handling:** Tests loading from nonexistent files.
```
python -m unittest unittest_example.py
```
### Code Style
This project is written in **Python** and follows **PEP8 style guidelines** to maintain readability and consistency.
To ensure proper formatting, the code was reformatted with **Black** and PyCharm's built-in reformatting tools.
## 3. Results and Summary

### Results
* Successfully implemented a **DND character creation system** with flexible customization
* Ensured **persistent storage** of characters using JSON.
* Applied **OOP principles** and the **Builder pattern** to maintain structured code.
* Covered essential features with **unit testing** to ensure program reliability.

### Conclusions
The **DND Character Creator** streamlines the process of character creation, offering structured customization while leveraging Python's OOP capabilities. It's **test-driven approach** ensures correctness, making it a useful tool for both players and dungeon masters.

### Future Extensions
* **Combat System**: Add attack/damage mechanics and HP tracking. (HP is setup, but no combat system therefore no need to track it)
* **Multiplayer Integration:** Allow players to share characters via an API.
* **GUI Version:** Expand beyond CLI to a graphical interface.

## 4. Optional: Resources & References

* https://www.dndbeyond.com/
* https://docs.python.org/
* https://peps.python.org/pep-0008/
* https://docs.python.org/3/library/unittest.html
* generative AI, but solely for ideas and the explanation/simplification of concepts.
