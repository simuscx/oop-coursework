import argparse
from CharacterBuilder import CharacterBuilder
from Character import CharacterSaver
from Item import Item


# TODO: PEP8: two blank lines before top-level function and class definitions
def build_character():
    # TODO: docstring
    name = input("Character name: ")
    char_class = input("Character class: ")
    builder = CharacterBuilder().set_name(name).set_class(char_class)

    stats = {}
    for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:

        # TODO: consider "enter to skip" instead of blank
        val = input(f"{stat} (blank to skip): ")

        # TODO: val naming not very clear, maybe stat_val?

        # TODO: nice to have: using a regex/something to check if the input is a number, cause if char is entered,
        #  CLI breaks same as with invalid class choice below

        # TODO: maybe also nice to have: instead of showing blank to skip, show default stat if not entered
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

        # TODO: nice to have: maybe better handling when non-existent class is passed
        #  maybe just tell the user the class does not exist and stay in CLI
        """
        > Character class: test
        Traceback (most recent call last):
          
            main()
            char = build_character()
                   ^^^^^^^^^^^^^^^^^
            builder = CharacterBuilder().set_name(name).set_class(char_class)
            raise ValueError(f"Unsupported character class: {char_class}")
        
        ValueError: Unsupported character class: test
        """

        # TODO: also lowercase wizard is not existent (should it be?)

    elif args.action == "load":
        chars = CharacterSaver.load_characters(args.file)

        # TODO: for future reference, for char in chars is more human readable than for c in chars :)
        for c in chars:
            print(c)


if __name__ == "__main__":
    main()

# TODO: create several characters in one CLI, save to one file, perhaps name file too
