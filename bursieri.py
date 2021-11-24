m = input().split(" ")
ln = []
lm = []
le = []
nr = 0
ok = 0


def medie(l):
    k = 0
    for i in range(len(l)):
        k = k + int(l[i])
    med = float(k / len(l))
    return med


n = int(m[0])
o = int(m[1])

for i in range(n):
    nume = input()
    note = input().split(" ")
    me = medie(note)
    lm.append(me)
    le.append(nume)
maxx = max(lm)
for p in range(len(lm)):
    if lm[p] == maxx:
        ok = p
    elif lm[p] > 8 and nr < int(m[2]):
        nr += 1

print("^{} ".format(nr))
print("{} {:0.2f}\s*$ ".format(le[ok], maxx))