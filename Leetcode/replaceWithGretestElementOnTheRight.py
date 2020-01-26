def replaceElements(arr: "List[int]") -> "List[int]":
    currentMax = -1
    rv = [currentMax]
    for i in reversed(arr):
        currentMax = max(currentMax, i)
        rv.append(currentMax)
    return rv[::-1][1:]


def test():
    arr = [[17, 18, 5, 4, 6, 1], [], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
    ans = [[18, 6, 6, 6, 1, -1], [], [5, 5, 5, 5, -1], [4, 3, 2, 1, -1]]
    # arr = [[17,18,5,4,6,1]]
    # ans = [[18,6,6,6,1,-1]]
    for i in range(len(arr)):
        assert ans[i] == replaceElements(arr[i]), "Incorrect at iteration %d"%i


test()
