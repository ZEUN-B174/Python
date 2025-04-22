f = open("country.txt", "r")

list1 = []
while True:
    line = f.readline().strip()
    if not line: break
    list1.append(line)

f.close()
print(list1)