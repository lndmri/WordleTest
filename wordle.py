import random

words = ["this",]

hidden_word = random.choice(word)

def check_word(guess):
    if hidden_word == guess:
        print("Congrats! You did it") 
        return True
    else:
        result = ""
        for i,j in zip(guess, hidden_word):
            if i==j:
                result = result + "C "

def main():
    attmpt = 5
    give_instructions()
    while (attempt > 0):
        guess = input("Enter four letter word")
        if check_word(guess):
            break
        else:
            arrempt -= 1 #attempt = attempt - 1
            print(f"You have {attempt} attempts left")
    else:
        print("GAME OVER")
