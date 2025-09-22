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
    print("\nWelcome to a new day, here are your Current Stats:"); time.sleep(0.1)
    print(f"Happiness: {happiness}/10"); time.sleep(0.1)
    print(f"Hunger: {hunger}/10"); time.sleep(0.1)
    print(f"Age: {age}"); time.sleep(0.1)
    print(f"Sphericalness: {sphericalness}/10"); time.sleep(0.1)
    print(f"Size: {size}/10"); time.sleep(0.1)

    print(f"\nWhat would you like to do now?"); time.sleep(0.1)
    print(f"1: Feed {rock_name}"); time.sleep(0.1)
    print(f"2: Put makeup on {rock_name}"); time.sleep(0.1)
    print(f"3: Lick {rock_name}"); time.sleep(0.1)
    print(f"4: Kick {rock_name} alongside you as you go on a walk"); time.sleep(0.1)
    action = input(f"5: Do Nothing\n(Input what you would like to do and press enter)\n")

    if action == '1':
        print(f"You feed {rock_name}"); time.sleep(0.1)
        print(f"{rock_name} loses 5 hunger and gains 1 happiness because {rock_name} likes eating")
        input("(Press enter to continue)")
        if hunger < 5:
            hunger = 0
        else:
            hunger -= 5
        if happiness < 10:
            happiness += 1
    
    elif action == '2':
        print(f"You apply very pretty makeup to {rock_name}"); time.sleep(0.5)
        print(f"{rock_name} feels very bonita and gains 3 happiness because of this, {rock_name} also gets a little bit hungrier(+1) and because of the make up they get a little bigger(size +1)"); time.sleep(0.1)
        input("Press enter to continue")
        if happiness < 8:
            happiness += 3
        else:
            happiness = 10
        if hunger != 0:
            hunger -= 1
        if size != 10:
            size +=1
    elif action == '3':
        print("You little freak"); time.sleep(0.5)
        print(f"You lick {rock_name}"); time.sleep(0.5)
        print(f"{rock_name} doesn't appreciate this very much(happiness -1), however you do make them more of a sphere(sphericalness +1)"); time.sleep(0.1)
        input("(Press enter to continue)")
        if happiness != 0:
            happiness -= 1
        if sphericalness != 10:
            sphericalness += 1
    elif action == '4':
        print(f"'Oww' {rock_name} yelps({rock_name} can't talk but if he could thats what he would say as you kick them)"); time.sleep(0.1)
        print(f"{rock_name} didn't love being kicked(happiness -1), but from kicking them around {rock_name}  gets a little rounder(Sphericalness +2) and a little bit smaller(size -1)"); time.sleep(0.1)
        input("Press enter to continue")
        if happiness != 0:
            happiness -= 1
        if sphericalness < 9:
            sphericalness += 2
        else:
            sphericalness = 10
        if size != 0:
            size -= 1
    else:
        print(f"You decide to not do anything with {rock_name} today"); time.sleep(0.1)
        print(f"{rock_name} is very bored and sad(happiness -2). They also get a little hungrier(hunger +1) and lose some of their youthful energy from not doing anything(age + 1)"); time.sleep(0.1)
        input("Press enter to continue")
        age += 1
        if happiness > 1:
            happiness -= 2
        else:
            happiness = 0
        if hunger != 10:
            hunger += 1

    print("The day passes"); time.sleep(0.1)
    print(f"{rock_name} gets slightly hungrier(+1), and ages by 1"); time.sleep(0.5)
    if hunger != 10:
        hunger += 1
    age += 1

    if input("Would you like to continue to the next day(yes/no)\n").lower() == "no":
        print(f"Without you there, {rock_name} slowly rots away and gets covered by moss, eventually breaking down into grains of sand and spreading all over the world")
        break
    
    print("The night passes"); time.sleep(1)
    for i in range(3):
        print("...\n"); time. sleep(0.5)
    
    if happiness == 0:
        print(f"You have neglected to take care of {rock_name}, and {rock_name} called your parents who take them from you with shame toward you in their eyes")
        break
    if hunger == 10:
        print(f"From the amount of times you have tried to feed {rock_name}, your pet rock who is a rock and cannot eat food, there is a large pile of food around {rock_name} and it turns to mold and dissolves {rock_name}")
        break
    if  age >= 100:
        print(f"After living a long and happy(if somewhat sad looking black) life with {rock_name}, you wither away and die and {rock_name} lives on with your niece")
        break
    if sphericalness == 10:
        print(f"The next day you go on a walk with {rock_name}, and because they are so spherical {rock_name} rolls down the street into a storm drain never to be seen again")
        break
    if size == 0:
        print(f"Your rock is now so small that another pet rock, named Rocky, eats {rock_name}")
        break
    if size == 10:
        print(f"There is now so much makeup on {rock_name} that you no longer have a pet rock anymore but a pet pile of makeup, still named {rock_name} because you are in denial\nHowever, this is a pet rock simulation and not a pet makeup pile simulation")
        break
    if hunger == 0:
        print("When you wake up the next morning you {rock_name} looks gaunt and very hungry, but they are a rock so nothing happens(it's probably just your imagination)")

time.sleep(1)
print("\nThank you for playing rock simulator\nIf you would like to play again rerun the program")