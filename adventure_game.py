import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def get_valid_choice(option1, option2):
    print_pause(option1)
    print_pause(option2)

    while True:
        choice = input("(Please enter 1 or 2.)\n").strip()
        if choice == "1" or choice == "2":
            return choice
        print_pause("That choice is not valid. Please try again.")


def intro(villain, relic):
    print_pause(
        "You arrive at the edge of a silent valley just before sunset."
    )
    print_pause(
        "The villagers say that strange lights have been seen near "
        "the old cave in the mountain."
    )
    print_pause(
        f"They also whisper that a {villain} has been guarding "
        f"the hidden {relic}."
    )
    print_pause("Some believe the relic can save the valley.")
    print_pause("Others say no one who searches for it ever returns.")
    print_pause("In front of you stands an abandoned watchtower.")
    print_pause("To your right is the entrance to the cave.")
    print_pause("At your side you carry only a weak wooden staff.")


def tower(items):
    print_pause("You walk carefully toward the abandoned watchtower.")
    print_pause("The door is half-broken, and the air inside smells of dust.")

    if "silver lantern" in items:
        print_pause("You already searched the tower before.")
        print_pause("There is nothing else useful here.")
    else:
        print_pause("Inside, you find a silver lantern hanging on the wall.")
        print_pause("It still works, and its light feels strangely warm.")
        print_pause("You take the silver lantern with you.")
        items.append("silver lantern")

    print_pause("You leave the tower and return to the valley.")


def cave_entrance(villain, relic, items):
    print_pause("You step toward the cave entrance.")
    print_pause("Cold air flows out from the darkness.")
    print_pause("The stone floor is wet, and every sound echoes around you.")

    choice = get_valid_choice(
        "Enter 1 to go deeper into the cave.",
        "Enter 2 to return to the valley."
    )

    if choice == "1":
        deep_cave(villain, relic, items)
    else:
        print_pause("You decide not to rush into danger.")
        print_pause("You head back to the valley.")
        valley(villain, relic, items)


def deep_cave(villain, relic, items):
    print_pause("You move deeper into the cave.")
    print_pause("Soon, the path splits into two narrow tunnels.")
    print_pause("One path is dark and silent.")
    print_pause("The other glows with a faint blue light.")

    choice = get_valid_choice(
        "Enter 1 to follow the glowing tunnel.",
        "Enter 2 to enter the dark tunnel."
    )

    if choice == "1":
        glowing_chamber(villain, relic, items)
    else:
        dark_tunnel(villain, relic, items)


def glowing_chamber(villain, relic, items):
    print_pause("You follow the blue glow until you reach a hidden chamber.")
    print_pause("Crystals shine across the walls like frozen stars.")

    if "moon blade" in items:
        print_pause("The crystal chamber is quiet now.")
        print_pause("You already claimed its treasure before.")
    else:
        print_pause(
            "At the center of the chamber, resting on a stone altar, "
            "you see a sword."
        )
        print_pause("Its blade reflects the crystal light with a pale glow.")
        print_pause(
            "You take the Moon Blade and leave your wooden staff behind."
        )
        items.append("moon blade")

    print_pause("You make your way back to the deeper part of the cave.")
    final_encounter(villain, relic, items)


def dark_tunnel(villain, relic, items):
    print_pause("You walk into the dark tunnel.")
    print_pause("The silence becomes heavier with every step.")

    if "silver lantern" in items:
        print_pause("You raise your silver lantern.")
        print_pause("Its light reveals warning marks on the walls.")
        print_pause("You avoid a hidden trap just in time.")
        print_pause(
            "At the end of the tunnel, a stone gate opens into a "
            "large chamber."
        )
        final_encounter(villain, relic, items)
    else:
        print_pause(
            "Without a good light, you fail to notice a trap on the ground."
        )
        print_pause("The floor beneath you cracks open.")
        print_pause("You fall into a deep pit.")
        print_pause("Your journey ends here.")
        print_pause("GAME OVER!")
        play_again()


def final_encounter(villain, relic, items):
    print_pause("At last, you enter the heart of the cave.")
    print_pause(
        f"There, standing beside the hidden {relic}, is the {villain}."
    )

    if "moon blade" in items:
        print_pause(f"The {villain} rushes toward you with a roar.")
        print_pause("You stand your ground and draw the Moon Blade.")
        print_pause(
            "The blade flashes brightly, filling the chamber with light."
        )
        print_pause(f"The {villain} stumbles back, blinded and defeated.")
        print_pause(
            f"You claim the {relic} and carry it safely out of the cave."
        )
        print_pause("The valley is saved.")
        print_pause("YOU WIN!")
        play_again()
    else:
        print_pause("You try to defend yourself with what you have.")
        print_pause(f"But the {villain} is far too powerful.")
        print_pause("You are forced back until there is nowhere left to run.")
        print_pause("You have been defeated.")
        print_pause("GAME OVER!")
        play_again()


def valley(villain, relic, items):
    print_pause("")
    print_pause("You are standing once again in the quiet valley.")

    choice = get_valid_choice(
        "Enter 1 to explore the watchtower.",
        "Enter 2 to enter the cave."
    )

    if choice == "1":
        tower(items)
        valley(villain, relic, items)
    else:
        cave_entrance(villain, relic, items)


def play_again():
    while True:
        answer = input("Would you like to play again? (y/n)\n").strip().lower()
        if answer == "y":
            print_pause("A new adventure begins...")
            print_pause("")
            play_game()
            break
        if answer == "n":
            print_pause("Thanks for playing. Farewell, traveler!")
            break
        print_pause("Please enter y or n.")


def play_game():
    villains = [
        "shadow beast",
        "stone guardian",
        "cave sorcerer",
        "ash dragon"
    ]
    relics = [
        "Sun Orb",
        "Crystal Heart",
        "Ancient Crown",
        "Golden Rune"
    ]

    villain = random.choice(villains)
    relic = random.choice(relics)
    items = []

    intro(villain, relic)
    valley(villain, relic, items)


if __name__ == "__main__":
    play_game()
