class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, str_):
        node = self.root

        for c in str_:
            if c not in node.children:
                node.children[c] = TrieNode()
            
            node = node.children[c]
        node.isWord = True

    # def search(self, str_):
    #     node = self.root

    #     for i, c in enumerate(str_):
    #         if c not in node.children:
    #             if node.isWord : 
    #                 return 1
    #             else:
    #                 return 0
    #         else:
    #             node = node.children[c]
    #         if i == len(str_) - 1 and not node.isWord:
    #             return 0
    #     return 1

    def search(self, str_):
        node = self.root

        for c in str_:
            if c in node.children:
                node = node.children[c]
            elif node.isWord:
                return 1
            else:
                return 0     
        # to cover this case if the word len > pref len => words = ['i'], pref = "ikwjoty"
        return 1 if node.isWord else 0  


class Solution:

    def prefixCount(self, words: List[str], pref: str) -> int:

        count = 0
        trie = Trie()    
        trie.insert(pref)

        for word in words:
            count += trie.search(word)

        return count


       
