'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice:")
youDict = {"s":1, "w":-1, "g":0}
reverseDict ={1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youstr]

# print(f" You chose {dict[you]}\nComputer chose {reverseDict[computer]}")
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if(computer == you):
  print("Its a draw")
else:
  if(computer==-1 and you ==1):
    print("You won!! ")

  elif(computer==1 and you ==-1):
    print("You Lose!! ")

  elif(computer==1 and you ==0):
    print("You won!! ")

  elif(computer==0 and you ==-1):
    print("You won!! ")

  elif(computer==0 and you ==1):
    print("You Lose!! ")

  else:
    print("Something Went Wrong!!!!")
# '''
# 1 for Snake
# -1 for Water
# 0 for Gun
# '''

# import random

# # Randomly assign computer's choice
# computer = random.choice([1, -1, 0])

# youstr = input("Enter your choice (s for snake, w for water, g for gun): ")
# youDict = {"s": 1, "w": -1, "g": 0}
# reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# # Validate input
# if youstr not in youDict:
#     print("Invalid input! Please enter 's', 'w', or 'g'.")
# else:
#     you = youDict[youstr]

#     # Display the choices
#     print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

#     # Determine the result
#     if computer == you:
#         print("It's a draw!")
#     else:
#         if (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
#             print("You won!!")
#         else:
#             print("You Lose!!")
