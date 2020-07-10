import random
import pandas as pd

df = pd.read_csv('Datatable.csv')

while True:
    randNum = random.randrange(0, 12)
    answer = df['molecularGeometry'][randNum]
    print(df['bonds'][randNum], df['lonePairs'][randNum])
    guess = input()
    if answer == guess:
        print("Correct")
        if guess == "exit":
            break

        else:
            print("Incorrect")