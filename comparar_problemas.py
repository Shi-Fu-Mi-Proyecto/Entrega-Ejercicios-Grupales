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

a = [ random.randint(1, 100) for i in range(3)]
b = [ random.randint(1, 100) for i in range(3)]
lucia = 0
carlos = 0

for i in range(3):
    if a[i] > b[i]:
        lucia += 1
    elif a[i] < b[i]:
        carlos += 1
    elif a[i] == b[i]:
        pass
print ("puntuacion de Lucia es: " , lucia, "puntuacion de Carlos es: " ,carlos)
if carlos < lucia:
    print ("Lucia es la ganadora")
elif carlos > lucia:
    print ("Carlos es el ganador")



    