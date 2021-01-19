import random
from phrasehunter.phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("Winner winner chicken dinner"), Phrase("Howdy Partner"), 
                   Phrase("There is a snake in my boot"), Phrase("Are we there yet"),
                   Phrase("In a while crocodile")]
        self.active_phrase = None
        self.guesses = []
    
    
    def start(self, phrase):
        phrase.display(phrase.phrase, None)
        guess = self.get_guess()
        while True:
            if phrase.display(phrase.phrase, guess) == 1:
                self.missed += 1
                print("You have guessed {} out of 5 lives remaining.\n".format(5 - self.missed))
                if self.missed == 5:
                    return self.game_over()
            else:
                print()
                print(phrase.display(phrase.phrase, guess))
                print()
                if phrase.check_complete() == True:
                    return self.game_over()
            guess = self.get_guess()
            
        return phrase
    
        
    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrases)
        return self.active_phrase
        
        
    def welcome(self):
        use_phrase = self.get_random_phrase()
        print("Welcome to Phrase Hunter!")
        while True:    
            #make sure there isn't an error
            participate = input("Would you like to play? (Y/N): ")
            print()
            try:
                if participate.lower() != "y" and participate.lower() != "n":
                    raise ValueError("Pleaes type Y or N only.")
            except ValueError as err:
                print("{}".format(err))
                print("Please try again.\n")
            else:
                if participate.lower() == "y":
                    return self.start(use_phrase)
                else:
                    break
        
        
    def get_guess(self):
        while True:
            guess = input("Guess a letter: ")
            guess = guess.lower()
            try:
                if len(guess) > 1:
                    raise ValueError("Sorry! Please only select one letter at a time.")            
            except ValueError as err:
                print("{}".format(err))
                print("Please try again.\n")
            
            else:
                if self.guesses.count(guess) > 0:
                    print("You can't pick the same letter! Try again.")
                    self.guesses.append(guess)
                    return guess
                else:
                    self.guesses.append(guess)
                    return guess
        
        
    def game_over(self):
        if self.missed == 5:
            print("Too many misses! Game Over.")
        else:
            print("You're a winner (chicken dinner)!")
