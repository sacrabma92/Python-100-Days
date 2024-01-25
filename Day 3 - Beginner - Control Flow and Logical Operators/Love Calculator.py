print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

name_1 = name1.lower()
name_2 = name2.lower()

T = name_1.count("t") + name_2.count("t")
R = name_1.count("r") + name_2.count("r")
U = name_1.count("u") + name_2.count("u")
E = name_1.count("e") + name_2.count("e")

L = name_1.count("l") + name_2.count("l")
O = name_1.count("o") + name_2.count("o")
V = name_1.count("v") + name_2.count("v")
E = name_1.count("e") + name_2.count("e")

suma_1 =  T + R + U +E
suma_2 = L + O + V + E

number = (f"{suma_1}{suma_2}")
converter = int(number)

if converter < 10 or converter > 90:
  print(f"Your score is {number}, you go together like coke and mentos.")
elif converter > 40 and converter < 50:
  print(f"Your score is {number}, you are alright together.")
else:
  print(f"Your score is {number}")
