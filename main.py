from Item import Item
from Character import Barbarian, Bard

# Create items
sword = Item("Sword", "A sharp blade for battle", 150)
lyre = Item("Lyre", "A musical instrument for inspiring allies", 100)

# Create characters
hero = Barbarian("Grog")
hero.add_item_to_inventory(sword)

bard = Bard("Scanlan")
bard.add_item_to_inventory(lyre)

# Display details
print(hero)
print(bard)

# Save characters to files
with open("hero.json", "w") as file:
    hero.save_to_file(file)

with open("bard.json", "w") as file:
    bard.save_to_file(file)