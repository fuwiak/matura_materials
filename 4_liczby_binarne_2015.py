#1
ile = 0
for i in range(1000):
    we=list(input())
    zera=we.count('1')
    if zwera > jedynki:
        ile +=1
    print(ile)

#2
ile2 = 0
ile8 = 0
for i in range(1000):
    we = input().strip()
    if we[-1] == '0':
        ile2 +=1
        if we == '0' or we == '00':
            ile8 +=1
        if len(we) >=3 and we[-2] == we[-3] == '0':
            ile8 += 2
print(ile2,ile8)
#3
N=int(input())
min = 260
maksi = -1
dlugie = []
krotkie = []
wszystkie = []
for i in range(N):
    we = input().strip()
    wszystkie.append(we)
    if len(we) == min:
        krotkie.append(we)
    if len(we) == maksi:
        dlugie.append(we)
    if len(we)<mini:
        mini = len(we
        krotkie = [we]
    if len(we)> maksi:
        maksi = len(we)
        dlugie = [we]
print(wszystkie.index(min(krotkie))+1)
print(wszystkie.index(max(dlugie))+1)
