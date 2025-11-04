import time
import random



def load_valid_words():
    valid_words = []

    with open("words.txt") as f:
        for line in f:
            line = line.strip()
            valid_words.append(line)

    return valid_words 

def run_timer():
    x = 30
    for i in range(x):
        print(x-i, end=" ", flush=True)
        time.sleep(1)
    print()
    print("timer is up")

def get_random_letter(letters, counts=None):
    if counts is None:
        counts = [1]*len(letters)
    letter_list = ""
    for i in range(len(letters)):
        letter = letters[i]
        count = counts[i]
        for j in range(count):  
            letter_list = letter_list+letter
    l = random.choice(letter_list)
    return l

def get_vowel():
    vowels = "AEIOU"
    vowel_counts = [ 15, 21, 13, 13, 5 ]
    v = get_random_letter(vowels, vowel_counts)
    return v

def get_consonant():
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    consonant_counts = [ 2,3,6,2,3,2,1,1,5,4,8,4,1,9,9,9,1,1,1,1,1 ]
    c = get_random_letter(consonants, consonant_counts)
    return c




def play_letters():
    print("Lets play a letter round!")
    board = ""


    #loop to ask player to select v - vowel / c consonant
    # and fill 9 letters into board

    for i in range(9):
        ans = input("enter v or c: ")
        if ans == "v":
            l = get_vowel()
            board = board+l
        else:
            ans == "c"
            O = get_consonant()
            board = board+O
            
        print(board)   
    #start timer
    run_timer() 
    
    final_answer = input("what is your word:")


    #take input from player 1: what is your word
    #take input from player 2: what is your word

    #check words in valid_words and print who won
    #return points as tuple (player1score, player2score)






if __name__ == "__main__":
    play_letters()
    
