# n = int(input())
# s = list(map(int, input().split(" ")))
# dic = {}
# for x in s:
#     dic[str(x)] = n - x
# for x in s:
#     if str(dic[str(x)]) in dic.keys():
#         print("true")
#         break

n = int(input())
s = list(map(int, input().split(" ")))
dic = {}
for x in s:
    if str(x) in dic.keys():
        if x + x == n:
            print("True")
            quit()
    dic[str(x)] = n - x

for x in s:
    val = dic[str(x)]
    dic.pop(str(x))
    if str(val) in dic.keys():
        print("true")
        break
    dic[str(x)] = n - x
