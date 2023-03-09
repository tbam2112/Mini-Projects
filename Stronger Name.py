#Define the alphabet
vowel = ["a", "e", "i", "o", "u"]
consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

#Program gets two names to compare
your_name = input("Whats you name? ")
your_name = your_name.lower()
another_name = input("Whats another name? ")
another_name = another_name.lower()

#Program converts names into numbers
def name_math(name):
    number = 1
    for i in name:
        if i in vowel:
            number*=2
        else: 
            number+=1
    return number

#Program replaces your name with the new number
your_name = name_math(your_name)
another_name = name_math(another_name)

#Compares both names by the number it was given
if your_name > another_name:
    print("You're name is strong. ")

else:
    print("You're name isn't that strong. ") 

