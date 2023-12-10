#Project Name: Rock paper scissor
def rock_paper(num):
  b = ""
  import random
  a = random.randrange(1, 3)
  c = ""
  d = ""
  if a == 1:
    c = "Rock"
  elif a == 2:
    c = "Paper"
  else:
    c = "Scissor"
  if num == 1:
    d = "Rock"
  elif num == 2:
    d = "Paper"
  elif num == 3:
    d = "Scissor"
  else:
    d = num
  if a == 1 and num == 1:
    b = "It's draw..!!"
  elif a == 2 and num == 2:
    b = "It's draw..!!"
  elif a == 3 and num == 3:
    b = "It's draw..!!"
  elif a == 1 and num == 2:
    b = "Wohoo!!...You own the point"
  elif a == 3 and num == 1:
    b = "Wohoo!!...You own the point"
  elif a == 2 and num == 3:
    b = "Wohoo!!...You own the point"
  elif a == 1 and num == 3:
    b = "Ohoo..!! You lost it"
  elif a == 2 and num == 1:
    b = "Ohoo..!! You lost it"
  elif a == 3 and num == 2:
    b = "Ohoo..!! You lost it"
  else:
    b = "Invalid input..!!... You have to choose between the above options.."
  return (f"The device has choosen {c}, and you have choosen {d}\n{b}")
player = int(input("Choose one between Stone(1), Paper(2), Scissor(3): "))
Result = rock_paper(player)
print (Result)