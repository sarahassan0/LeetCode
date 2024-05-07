class Word:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.dict = Word()
        

    def addWord(self, word: str) -> None:
        cur_dict = self.dict

        for char in word:
            if char not in cur_dict.children:
                cur_dict.children[char] = Word()
            cur_dict = cur_dict.children[char]
        cur_dict.end_of_word = True

    def search(self, word: str, cur_dict=None) -> bool:
        if not cur_dict:
            cur_dict = self.dict

        for i in range(len(word)):
            if word[i] == '.':
                for child in cur_dict.children.values():
                    if self.search(word[i+1:], child):
                        return True
                
                return False
            elif word[i] not in cur_dict.children:
                return False
            cur_dict = cur_dict.children[word[i]] 
        return cur_dict.end_of_word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)