import random

#empty variables
name = ""

#Items for Dinner Decision Maker
food_dict = {
    "American" : ["McDonalds", "Freddy's", "Spangles"],
    "Mexican" : ["Taco Bell", "Rene's"],
    "Italian" : ["Olive Garden", "Pizza"],
    "Asian" : ["Panda Express", "Hu-Hot", "Pho"],
    "BBQ" : ["Hog Wild", "Bite Me BBQ", "When Pigs Fly"]
}

#Introduction and gets username
def username():
    name = input(f"My name is Dr. Eww, and I will be assisting you today... Whats your name? ")
    name = name.upper()
    nickname = name[0] 
    uh_oh = input(f"{name}! \nI'm terribly sorry that name infuriates me and I don't quite know why... \nIf you don't mind I'll call you {nickname}, otherwise just say 'no'. ")
    if uh_oh.lower() != "no":
        name = nickname
        print(f"Sounds good {name}")
    else: 
        print(f"WOW! no wonder your name's {name}!")
    return name

#shows the catagories of dinner choices
def dinner_options():
    food_choice = [type for type in food_dict]
    print(list(enumerate(food_choice,1)))
    help = input(f"Ok {name} of these options what sounds good? please select a numerical option. ")
    return int(help)

#Selects a place to eat based on catagory choice
def output_choice(choice):
    while True:
        if choice < 1 or choice > 5:
            choice = input("You goofed, select a number 1 through 5! ")
            choice = int(choice)
        elif choice == 1:
            print("Ok go to, " + random.choice(food_dict["American"]) + " today!")
            quit()
        elif choice == 2:
            print("Ok go to, " + random.choice(food_dict["Mexican"]) + " today!")
            break
        elif choice == 3:
            print("Ok go to, " + random.choice(food_dict["Italian"]) + " today!")
            break
        elif choice == 4:
            print("Ok go to, " + random.choice(food_dict["Asian"]) + " today!")
            break
        elif choice == 5:
            print(f"Ok go to, " + random.choice(food_dict["BBQ"]) + " today!" )
            break
        


print(f"Welcome to Chicken Noodle Soup Labs, where we help you decide where to eat!")

name = username()

help = dinner_options()

output_choice(int(help)) 
    

