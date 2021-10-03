# Problem Set 4B
# Name: Luis Tallavo

import string

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

def get_story_string():
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        self.message = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message

    def get_valid_words(self):
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        cipher = {}
        for i in range(65, 91):
            if (i + shift <= 90):
                cipher[chr(i)] = chr(i + shift)
            else:
                cipher[chr(i)] = chr(i + shift - 26)
        for i in range(97, 123):
            if (i + shift <= 122):
                cipher[chr(i)] = chr(i + shift)
            else:
                cipher[chr(i)] = chr(i + shift - 26)
        return cipher
        
    def apply_shift(self, shift):
        self.message_text = ''
        cipherdict = self.build_shift_dict(shift)
        for i in self.message:
            if i.isalpha():
                self.message_text = self.message_text + cipherdict[i]
            else:
                self.message_text = self.message_text + i
        return self.message_text

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        return self.shift

    def get_encryption_dict(self):
        copydict = self.encryption_dict.copy()
        return copydict

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)
        self.message_text = text

    def decrypt_message(self):
        realwords = 0
        tempwordcounter = 0
        shift = 0

        for i in range (26):
            ciphertext = self.apply_shift(i)
            message = ciphertext.split()
            for j in message:
                if is_word(self.valid_words, j):
                    tempwordcounter = tempwordcounter + 1
            if tempwordcounter > realwords:
                realwords = tempwordcounter
                shift = i
            tempwordcounter = 0
        
        return (shift, self.apply_shift(shift))

if __name__ == '__main__':

    plaintext = PlaintextMessage("This is a test for the cipher! Let's hope it works", 16)
    print("Expected Output: Jxyi yi q juij veh jxu syfxuh! Buj'i xefu yj mehai")
    print('Actual Output:', plaintext.get_message_text_encrypted())

    ciphertext = CiphertextMessage("Jxyi yi q juij veh jxu syfxuh! Buj'i xefu yj mehai")
    print('Expected Output:', (10, "This is a test for the cipher! Let's hope it works"))
    print('Actual Output:', ciphertext.decrypt_message())

    Storytext = CiphertextMessage(get_story_string())
    print('Decrypted Story:', Storytext.decrypt_message())
