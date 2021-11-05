""" Worked with Kishan and William"""
#class SentenceIterator:
#    def __init__(self, words):
#        self.words = words
#        self.index = 0
#
#    def __next__(self):
#        try:
#            word = self.words[self.index]
#        except IndexError:
#            raise StopIteration()
#        self.index += 1
#        return word
#
#    def __iter__(self):
#        return self
import reprlib

class Sentence: # An iterable
    def __init__(self, text):
        self.text = text
        self.words = text.split()

    def __iter__(self):
        for word in self.words:
            yield word
            
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

if __name__ == "__main__":
    sent = Sentence("Hi Fabian, this is the answer for PP10")
    for word in sent:
        print(word)

