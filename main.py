rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
p=int(input("What do you choose ? Type 0 for Rock, 1 for paper, 2 for Scissor."))
  
c=[rock,paper,scissors]

s=c[p]
print(s)
 
import random

d=random.randint(0,2)

e=[rock,paper,scissors]

a=e[d]
print("computer choose!")
print(a)

if s!= a:
 if  s<a:
    print( "you won")
 elif s >a:
    print("Computer won!")
elif s == a:
    print("Rematch")