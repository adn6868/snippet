def orderlyQueue(S: str, K: int) -> str:
    if K >= 2:
        return "".join(sorted(S))
    else:
        best = S
        for _ in range(len(S)):
            S = S[-1] + S[:-1]
            # print(S)
            best = min(S, best)
        return best


S1 = "cbadaaad"
K1 = 1

S2 = "baaca"
K2 = 3

S3 = "abchsgcziisudfhasdfgxxg"
K3 = 3

print(orderlyQueue(S1, K1))
print(orderlyQueue(S2, K2))
print(orderlyQueue(S3, K3))
