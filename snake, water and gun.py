import random

print("\nHello welcome to snake, water and gun game.")
print("\nThis is same as rock, papers and scissors game.")
print("\nThe rules are: \n1)Snake wins over water \n2)Water wins over gun \n3)Gun wins over snake.")
print("\nLets start.......!")

human = input("Choose between snake, water and gun: ")
object = ["Snake", "Water", "Gun"]
computer = random.choice(object)
print(f"You choose \"{human}\" and computer choose \"{computer}\".")
print(f"\n{human} X {computer}")

if(human.lower() == "snake" and computer.lower() == "snake" ):
    print("\nSo its a tie.")
elif(human.lower() == "snake" and computer.lower() == "water"):
    print(f"\n{human} wins. So you won.")
elif(human.lower() == "snake" and computer.lower() == "gun"):
    print(f"\n{computer} wins. So you loose.")
elif(human.lower() == "water" and computer.lower() == "snake"):
    print(f"\n{computer} wins. So you loose.")
elif(human.lower() == "water" and computer.lower() == "water"):
    print(f"\nIts a tie.")
elif(human.lower() == "water" and computer.lower() == "gun"):
    print(f"\n{human} wins. So you won.")
elif(human.lower() == "gun" and computer.lower() == "snake"):
    print(f"\n{human} wins. So you won.")
elif(human.lower() == "gun" and computer.lower() == "water"):
    print(f"\n{computer} wins. So you loose")
elif(human.lower() == "gun" and computer.lower() == "gun"):
    print(f"\nSo its a tie")
else:
    raise SyntaxError("Invalid syntax.....!")
    

print("\nThank you for playing.")

    