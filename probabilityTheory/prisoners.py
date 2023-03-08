import random
import sys
import matplotlib.pyplot as plt
import numpy as np

def maxLoopLength(perm):
    n = len(perm)
    maxLength = 0
    vis = [0]*n
    for i in range(n):
        currentNum = i
        if not vis[currentNum]:
            count = 0
            while not vis[currentNum]:
                vis[currentNum] = 1
                currentNum = perm[currentNum]
                count += 1
            maxLength = max(maxLength, count)
    return maxLength

def prisoners(perm, selfNum):
    currentNum = selfNum
    for i in range(50):
        if(perm[currentNum]==selfNum):
            return 1
        currentNum = perm[currentNum]
    else:
        return 0


n = int(sys.argv[1])
count = 0
maxLength = np.array([0]*100)
for _ in range(n):
    perm = list(range(100))
    random.shuffle(perm)
    maxLength[maxLoopLength(perm)-1] += 1
    for i in range(100):
        if not prisoners(perm, i):
            break
    else:
        count += 1

prob = count/n
print(f"Probability of all prisoners surviving: {prob}")

plt.bar(list(range(1, 52)), maxLength[:51]*100/n, color='b')
plt.bar(list(range(52, 101)), maxLength[51:]*100/n, color="orange")
plt.xlabel("Longest loop Size")
plt.ylabel("Probability")
plt.title(f"Probability vs Longest Loop Size for {n} tries")
# plt.plot(list(range(100)), maxLength/n, color='black')
plt.savefig(f"{n} tries")
plt.show()