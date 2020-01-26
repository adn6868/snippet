def longestCommonPrefix(strs: "List[str]") -> str:
    if len(strs) == 0:
        return ""
    maxRvLen = min(len(x) for x in strs)
    rv = ""
    for i in range(maxRvLen):
        rv += strs[0][i]
        for w in strs:
            if w[i] != rv[-1]:
                return rv[:-1]
    return rv


def test():
    inn = [
        [],
        [""],
        ["car", "set", "apaint"],
        ["flow", "flower", "flour"],
        ["fat", "fat", "fat"],
    ]
    out = ["", "", "", "flo", "fat"]
    for i in range(len(inn)):
        assert out[i] == longestCommonPrefix(inn[i]), "incorrect at %d" % i


test()
