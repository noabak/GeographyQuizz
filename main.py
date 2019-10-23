countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb","Spain": "Madrid","Palestine":"Jerusalem","France":"Paris","Morocco":"Rabat","Italia":"Roma","Siria":"Damascus","Portugal":"Lisboa", "Egypt":"Cairo"}

def run(name="User"):
    for k in countries_cities:
        print(">Game: What is the capital city of ",k," ?")
        answer=input(name+" :")
        if(answer.lower() == countries_cities[k].lower()):
            print(">Game: This is correct!")
        else:
            print(">Game: Your answer is wrong! The right answer is: ",countries_cities[k])

'''The Geography game: The user has to guess the capital city of some country'''

print(" +++++ WELCOME TO THE GEOGRAPHY GAME +++++")
repetir= True
while repetir:
  user= input("Please enter your name:")
  run(user)
  rep= input("Do you want to play again? Y/N")
  if rep.upper()== "Y":
      run(user)
  elif rep.upper()== "N":
      break
  else:
      print("Invalid caracter! Bye!")
      break