class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
        self.phrase = self.phrase.lower()
        self.blank_list = []
    
    #Need to return the phrase with the _ and the letters guessed correctly
    def display(self, phrase, guess):
        if guess == None:
            for i in phrase:
                if i == " ":
                    self.blank_list.append(" ")
                else:
                    self.blank_list.append("_ ")
            blank_str = ""
            blank_str = blank_str.join(self.blank_list)
            print(blank_str)
            return self.blank_list
        else:
            if self.check_letter(phrase, guess) == True:
                old_pos = 0
                for letter in phrase:
                    if letter == guess:
                        position = phrase.find(letter, old_pos)
                        self.blank_list[position] = guess
                        old_pos = position + 1
                check_str = ""
                return(check_str.join(self.blank_list))
            else:
                return 1
            
    def check_letter(self, phrase, guess):
        if phrase.find(guess) >= 0:
            return True
        else:
            print("Sorry, {} is not in the phrase.".format(guess))
            return False
        
    def check_complete(self):
        check_str = ""
        if self.phrase == check_str.join(self.blank_list):
            return True
