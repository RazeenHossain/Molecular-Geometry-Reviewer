import random
import pandas as pd

df = pd.read_csv('Datatable.csv')
print(
    "Enter the correct molecular geometry based on the number of bonding groups and lone pairs of electrons given. "
    "Enter exit to quit.")
while True:
    randNum = random.randrange(0, 13)
    answer = df['molecularGeometry'][randNum]
    print("Bonding Domains: ", df['bonds'][randNum], "\nLone Pairs: ", df['lonePairs'][randNum])
    guess = input()
    if answer == guess.casefold():
        print("Correct\n")
    elif guess == "exit":
        break
    else:
        print("Incorrect\n")
