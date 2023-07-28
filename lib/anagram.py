# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_words):
        matching_words = []
        for possible_word in possible_words:
            if sorted(list(self.word)) == sorted(list(possible_word)):
                matching_words.append(possible_word)
        return matching_words