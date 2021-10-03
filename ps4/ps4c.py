# Problem Set 4C
# Name: Luis Tallavo

import string
from ps4a import get_permutations

def load_words(file_name):
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

WORDLIST_FILENAME = 'words.txt'

VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME) 
    
    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        valid_words_copy = self.valid_words.copy()
        return valid_words_copy
                
    def build_transpose_dict(self, vowels_permutation):
        transposedict = {}
        for i in range (65, 91):
            if chr(i).lower() in vowels_permutation.lower():
                if i == 65:
                    transposedict[chr(i)] = vowels_permutation[0]
                elif i == 69:
                    transposedict[chr(i)] = vowels_permutation[1]
                elif i == 73:
                    transposedict[chr(i)] = vowels_permutation[2]
                elif i == 79:
                    transposedict[chr(i)] = vowels_permutation[3]
                elif i == 85:
                    transposedict[chr(i)] = vowels_permutation[4]
            else:
                transposedict[chr(i)] = chr(i)


        for i in range (97, 123):
            if chr(i).lower() in vowels_permutation.lower():
                if i == 97:
                    transposedict[chr(i)] = vowels_permutation[0]
                elif i == 101:
                    transposedict[chr(i)] = vowels_permutation[1]
                elif i == 105:
                    transposedict[chr(i)] = vowels_permutation[2]
                elif i == 111:
                    transposedict[chr(i)] = vowels_permutation[3]
                elif i == 117:
                    transposedict[chr(i)] = vowels_permutation[4]
            else:
                transposedict[chr(i)] = chr(i)


        return transposedict
    
    def apply_transpose(self, transpose_dict):
        encodedmessage = ''
        message = self.message_text.split()
        for i in message:
            encodedword = ''
            for j in i:
                if j.isalpha():
                    encodedword = encodedword + transpose_dict[j]
                else:
                    encodedword = encodedword + j
            encodedmessage = encodedmessage + encodedword + ' '
        return encodedmessage     

        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        permutations = get_permutations(VOWELS_LOWER)
        message = self.message_text.split()
        score = 0
        tempscore = 0
        tempword = ''
        permutation = ''
        decryptedmsg = ''
        tempdecryptedmsg = ''
        
        for i in permutations:
            transposedict = self.build_transpose_dict(i)
            newmsg = ''
            for word in message:
                for letter in word:
                    if letter.isalpha():
                        tempword = tempword + transposedict[letter]
                    else:
                        tempword = tempword + letter
                tempdecryptedmsg = tempdecryptedmsg + tempword + ' '
                if is_word(self.valid_words, tempword):
                    tempscore = tempscore + 1
                tempword = ''
            if tempscore > score:
                score = tempscore
                permutation = i
                decryptedmsg = tempdecryptedmsg
            tempscore = 0
            tempdecryptedmsg = ''
        return (permutation, decryptedmsg.strip())
                    
    

if __name__ == '__main__':
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
