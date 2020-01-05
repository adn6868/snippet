class Node:
    def __init__(self, char):
        self.char = char


class Trie:
    def __init__(self, char=None):
        """
        Initialize your data structure here.
        """
        self.char = char
        self.stack = {}
        self.end = False

    def __str__(self):
        ans = "({}:".format(self.char)
        for i in self.stack.keys():
            ans += str(self.stack[i]) + ","
        return ans + ")"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word == "":
            self.end = True
            return
        if word[0] not in self.stack.keys():
            self.stack[word[0]] = Trie(word[0])
        self.stack[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word == "":
            # return len(self.stack.keys()) == 0
            return self.end
        if word[0] not in self.stack.keys():
            return False
        else:
            return self.stack[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if prefix == "":
            return True
        if prefix[0] not in self.stack.keys():
            return False
        else:
            return self.stack[prefix[0]].startsWith(prefix[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
obj = Trie()
obj.insert("appleProduct")
print(str(obj))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("veryNice")
print(obj.startsWith("very"))
obj.insert("app")
print(obj.search("apple"))
print(obj.startsWith("app"))
