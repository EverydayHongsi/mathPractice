
# range(1, 1000) 는 1~999 다. 하나 앞에까지. [:5] 이런거에서도 마찬가지.

result = 0
for a in range(1, 1000):
    if a % 3 == 0 or a % 5 == 0 :
        result += a
        print(a)
print(result)
