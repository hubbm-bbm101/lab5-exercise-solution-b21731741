N = int(input("N:"))
evenSum = 0
oddSum = 0
count = 0
for i in range(1,N+1):
    if i % 2 == 0:
        evenSum = evenSum + i
        count += 1
    else:
        oddSum += i
avgEven = evenSum / count
print("Average:", avgEven)
print("Sum:", oddSum)
