import random
rock=('''  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
paper=('''    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''')
scissor=('''  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) ''')
game_images=[rock,paper,scissor]
ch1=int(input("Enter Your Choice  Rock:0 Paper:1 Scissor:2 : "))
if ch1>=0 and ch1<=2:
    print(game_images[ch1])
ch2=random.randint(0,2)
print(game_images[ch2])
print("Your Opponent's Choice : ",ch2)
if ch1==ch2:
    print("It's a draw ")
elif ch1==1 and ch2==2:
    print("You Win !")
elif ch1==0 and ch2==1:
    print("You Loose !")
elif ch1==2 and ch2==1:
    print("You Win !")
elif ch1==1 and ch2==0:
    print("You Win !")
elif ch1==2 and ch2==1:
    print("You Loose !")
elif ch1>3 or ch1<0:
    print("Invalid Choice !")


