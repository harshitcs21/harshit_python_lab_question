import random
a = random.randint(1,9)
while  True :
    x = int(input("\nGuess the number : "))
    if x != a :
        print("\nWrong Guess. Try Again")
        continue 
    elif x == a :
        print("\nWell guessed!")
        break
