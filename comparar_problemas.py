#("!"/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
# 1. INTEGER_ARRAY a
# 2. INTEGER_ARRAY b
#
def compareTriplets(a, b):
# Write your code here
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        a = list(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))
        result = compareTriplets(a, b)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
        fptr.close()
a = random.randint (1, 100)
b = random.randint (1, 100)
lucia = 0
maria = 0
for i in range(3):
    if a[i] > b[i]:
        lucia += 1
    elif a[i] < b[i]:
        maria += 1
    elif a[i] == b[i]:
        pass
int[a] = lucia
int[b] = maria
print (lucia, maria)


    