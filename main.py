class Iterator:
    def __init__(self, word):
        self.word = word
        self.vowels = "aeiouAEIOU"
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.word):
            if self.word[self.i] in self.vowels:
                result = self.word[self.i]
                self.i += 1
                return result
            self.i += 1
        raise StopIteration


words = "hello world"
vowels = Iterator(words)
for vowel in vowels:
    print(vowel)
