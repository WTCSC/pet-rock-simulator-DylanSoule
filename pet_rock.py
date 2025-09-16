import time

rock_name = input("Welcome to rock simulator, lets begin by naming your rock. What would you like to name your rock\n")
input(f"Great! you now have a pet rock named {rock_name}, hopefully you take care of them(press enter to continue)")

understand = ''

while understand != 'no':
    input("In this rock simulator your rock will have stats that you can control through different actions, you choose what you want to increase and decrease")
    input("Let's go over all of the stats that you control!")
    input("To begin, we have happiness, pretty self explanatory. Try not to let it fall too far")
    input("Next we have hunger, also self explanatory, don't let the rock that totally has a stomach and a mouth get too hungry")
    input("The next stat is age. This is how old your rock is both physically and mentally")
    input("Almost done. Next we have sphericalness, this stat determines how round your rock is, from a jagged star to a perfect sphere")
    input("And finally we have size, this is how much space your rock takes up.")
    understand = input("Okay, I know that was a lot. Do you need to go over that again?(yes/no)\n")

input("\nOkay! lets begin")
time.sleep(0.1)

happiness = 5
hunger = 0
age = 0
sphericalness = 5
size = 8

while True:
    print("\nYour Current Stats:")
    time.sleep(0.1)
    print(f"Happiness: {happiness}/10")
    time.sleep(0.1)
    print(f"Hunger: {hunger}/10")
    time.sleep(0.1)
    print(f"Age: {age}")
    time.sleep(0.1)
    print(f"Sphericalness: {sphericalness}/10")
    time.sleep(0.1)
    print(f"Size: {size}/10")
    time.sleep(0.1)

    print(f"\nWhat would you like to do now?")
    time.sleep(0.1)
    print(f"1: Feed {rock_name}")
    time.sleep(0.1)
    print(f"2: Put makeup on {rock_name}")
    time.sleep(0.1)
    print(f"3: Lick {rock_name}")
    time.sleep(0.1)
    print(f"4: Kick {rock_name} alongside you as you go on a walk")
    time.sleep(0.1)
    action = input(f"5: Do Nothing\n")

    if action == '1':
        