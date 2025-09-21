import random
word=['jeevaa','cemira','annie','joshy']
rand=random.choice(word)
print("The Word Choosen is ",rand)
print("Hint : The name of you and your liked ones!")
guess=input("Enter an Letter to guess : ").lower()
under_score='_'
n=len(rand)
for a in range(n):
    under_score+='_'
print(under_score)
b=''
for i in rand:
    if i==guess:
        b+=i
    else:
        b+='_'
print(b)
