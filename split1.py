import re
hand = open('spl.txt')
need = list()
for line in hand:
    z = line.split(" ")[2]
    print z
    need.append(z)
print need

open("one.txt", 'wb').write(str(need))
#this is i will delete
#this is master