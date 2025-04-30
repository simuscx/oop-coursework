import argparse
from CharacterBuilder import CharacterBuilder
from Character import CharacterManager
from Item import Item

#fix pep8 for entire cli
def build_character():
    """

    """
    name = input("Character name: ")

    valid_classes = {
        "Barbarian", "Bard","Cleric",
        "Druid", "Fighter", "Monk",
        "Paladin", "Ranger", "Rogue",
        "Sorcerer", "Warlock", "Wizard"
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
            stats[stat]=int(stat_val)
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

#again, pep8
def main():
    parser = argparse.ArgumentParser(description="DND CLI")
    parser.add_argument("action", choices=["build", "load"])
    parser.add_argument("--file", default="characters.json")
    args = parser.parse_args()

    if args.action == "build":
        characters = []
        while True:
            char = build_character()
            CharacterManager.save_characters([char], args.file)

            add_more = input("Create another character? (y/n): ").strip().lower()
            if add_more != 'y':
                break

        file_name = input(f"Save characters to file ({args.file} by default): ").strip() or args.file
        CharacterManager.save_characters(characters, file_name)

    elif args.action == "load":
        try:
            chars = CharacterManager.load_characters(args.file)
            for char in chars:
                print(char)
        except FileNotFoundError:
            print(f"Error: File {args.file} not found.")

if __name__ == "__main__":
    main()

# TODO: create several characters in one CLI, save to one file, perhaps name file too
