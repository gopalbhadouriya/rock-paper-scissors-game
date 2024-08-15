
'''scissors = 3,paper = 2,rock = 3'''
import random
computer = random.choice([1,2,3])
you = input("Enter you choise in first letter: ")
youdict = {
  "r":1,
  "p":2,
  "s":3
}
younum = youdict[you]

dict = {
   1 : "r",
   2: "p",
   3: "s"
}
print(f"you choose {dict[younum]}\ncomputer chose {dict[computer]}")

if(computer == younum ):
    print("draw")
else:
    if(computer == 1 and you == "p"):
        print("you win")
    elif(computer == 1 and you == "s"):
        print("you loss")


    elif(computer == 2 and you == "r"):
        print("you loss")
    elif(computer == 2 and you == "s"):
        print("you win!")

    elif(computer == 3 and you == "r"):
        print("you win")
    elif(computer == 3 and you == "p"):
        print("you loss")







