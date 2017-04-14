import re
hand = open('spl.txt')
need = list()
for line in hand:
    z = line.split(" ")[0]
    need.append(z)
print need

open("one.txt", 'wb').write(str(need))
