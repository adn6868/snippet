def wordBreak(s: str, wordDict: [str]) -> bool:
    stack = []
    final = len(wordDict)
    base = s
    while len(stack) <= final:
        for word in wordDict:
            if word in s:
                s = "".join(s.split(word))
            else:
                stack.append(word)
            print(stack)
        print(s)
        if s == "":
            return True
        s = base
        stack, wordDict = wordDict, stack

    return False


s = "leetcode"

wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))
