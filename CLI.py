import argparse
from CharacterBuilder import CharacterBuilder
from Character import CharacterSaver
from Item import Item

def build_character():
    name = input("Character name: ")
    char_class = input("Character class: ")
    builder = CharacterBuilder().set_name(name).set_class(char_class)

    stats = {}
    for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
        val = input(f"{stat} (blank to skip): ")
        if val:
            stats[stat] = int(val)
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

def main():
    parser = argparse.ArgumentParser(description="DND CLI")
    parser.add_argument("action", choices=["build", "load"])
    parser.add_argument("--file", default="characters.json")
    args = parser.parse_args()

    if args.action == "build":
        char = build_character()
        CharacterSaver.save_characters([char], args.file)
    elif args.action == "load":
        chars = CharacterSaver.load_characters(args.file)
        for c in chars:
            print(c)

if __name__ == "__main__":
    main()

# TODO: create several characters in one CLI, save to one file, perhaps name file too