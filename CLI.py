import argparse

from Character import CharacterManager
from CharacterBuilder import CharacterBuilder
from Item import Item


# fix pep8 for entire cli
def build_character():
    """ """
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
        "Wizard",
    }

    while True:
        char_class = (
            input(f"Character class (Valid classes: {', '.join(valid_classes)}): ")
            .strip()
            .capitalize()
        )
        if char_class in valid_classes:
            break
        print("Invalid class choice! Please select from the listed classes.")

    builder = CharacterBuilder()
    builder.set_name(name).set_class(char_class)

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

    add_items = input("Add item(s)? (y/[d]efault/n): ").strip().lower()

    # validate input
    expected_input = ["y", "n", "d", "default"]
    while True:
        print(add_items)
        if add_items not in expected_input:
            print(f"Invalid input. Expected input: {expected_input}")
            continue
        break

    # set inventory choices
    if add_items == "n":
        builder.set_inventory([])

    elif add_items == "y":
        created_items = []
        creating_item = True

        while creating_item:
            name = input("Item name: ")
            desc = input("Description: ")
            value = int(input("Value: "))
            new_item = Item(name, desc, value)

            created_items.append(new_item)

            more_item = input("Do you want to create more items? ").strip().lower()
            if more_item == "y":
                continue
            if more_item == "n":
                creating_item = False

        builder.set_inventory(created_items)

    return builder.build()


def prompt_mode():
    """
    Ask the user to choose between loading or building characters.
    """
    while True:
        mode = (
            input("Do you want to [load] existing characters or [build] new ones? ")
            .strip()
            .lower()
        )
        if mode in {"load", "build"}:
            return mode
        print("Invalid choice. Type 'load' or 'build'.")


def main():
    """
    Entry point for the DND Character CLI
    Takes care of building and saving character profiles to a JSON file.
    Load and view previously saved characters from a JSON file.
    """
    parser = argparse.ArgumentParser(description="DND Character CLI")
    parser.add_argument(
        "--file",
        default="characters.json",
        help="Path to JSON file for saving/loading characters.",
    )
    args = parser.parse_args()

    mode = prompt_mode()

    if mode == "build":
        characters = []
        while True:
            char = build_character()
            characters.append(char)

            add_more = input("Create another character? (y/n): ").strip().lower()
            if add_more != "y":
                break

        file_name = input(f"Save to file (default: {args.file}): ").strip() or args.file
        if not file_name.endswith(".json"):
            file_name += ".json"

        CharacterManager.save_characters(characters, file_name)
        print(f"\nSaved {len(characters)} character(s) to {file_name}")

    elif mode == "load":
        file_name = input(
            "Enter file to load characters from (e.g. hero.json): "
        ).strip()
        if not file_name:
            print("No file name provided.")
            return

        if not file_name.endswith(".json"):
            file_name += ".json"

        try:
            characters = CharacterManager.load_characters(file_name)
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            return

        print(f"\nLoaded {len(characters)} character(s):\n")
        for i, char in enumerate(characters, 1):
            print(f"{i}. {char}")


if __name__ == "__main__":
    main()
