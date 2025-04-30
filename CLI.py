import argparse

from Character import CharacterManager
from CharacterBuilder import CharacterBuilder
from Item import Item


# fix pep8 for entire cli
def build_character():
    """

    """
    name = input("Character name: ")

    valid_classes = {
        "Barbarian",
        "Bard",
        "Cleric",
        "Druid",
        "Fighter",
        "Monk",
        "Paladin",
        "Ranger",
        "Rogue",
        "Sorcerer",
        "Warlock",
        "Wizard"
    }

    while True:
        char_class = input(f"Character class (Valid classes: {', '.join(valid_classes)}): ").strip().capitalize()
        if char_class in valid_classes:
            break
        print("Invalid class choice! Please select from the listed classes.")

    builder = CharacterBuilder().set_name(name).set_class(char_class)

    stats = {}
    for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
        stat_val = input(f"{stat} (enter to skip): ")

        if not stat_val:
            continue
        if stat_val.isdigit() and int(stat_val) > 0:
            stats[stat] = int(stat_val)
        else:
            print("Invalid input! Please enter a positive whole number.")
    builder.set_stats(stats)

    items = []
    while True:
        add = input("Add item? (y/n): ").strip().lower()
        if add != 'y':
            break
        name = input("Item name: ")
        desc = input("Description: ")
        value = int(input("Value: "))
        items.append(Item(name, desc, value))
    builder.set_inventory(items)

    return builder.build()


def prompt_mode():
    """
    Ask the user to choose between loading or building characters.
    """
    while True:
        mode = input("Do you want to [load] existing characters or [build] new ones? ").strip().lower()
        if mode in {"load", "build"}:
            return mode
        print("Invalid choice. Type 'load' or 'build'.")


def main():
    parser = argparse.ArgumentParser(description="DND Character CLI")
    parser.add_argument("--file",  default="characters.json",
                                                help="Path to JSON file for saving/loading characters")
    args = parser.parse_args()

    mode = prompt_mode()

    if mode == "build":
        characters = []
        while True:
            char = build_character()
            characters.append(char)

            add_more = input("Create another character? (y/n): ").strip().lower()
            if add_more != 'y':
                break

        file_name = input(f"Save characters to file ({args.file} by default): ").strip() or args.file
        if not file_name.endswith(".json"):
            file_name += ".json"

        CharacterManager.save_characters(characters, file_name)

    elif mode == "load":
        try:
            chars = CharacterManager.load_characters(args.file)
            for char in chars:
                print(char)
        except FileNotFoundError:
            print(f"Error: File {args.file} not found.")


if __name__ == "__main__":
    main()

# TODO: make CLI not just create characters, but also read from json.
