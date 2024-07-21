import random
n=random.randint(1,100)
a=-1

guess=1
while a!=n:
 
    a=int(input("Guess the Number Between : "))
    guess += 1
    if(a==n):
        print("You Guessed the rigth number:")
        break
    elif a>n : 
        print("Enter smaller number:")    
        

    else:
            print("Enter Larger number:")    
            

print(f"You have guessed the Correct number in {guess} attemps:")