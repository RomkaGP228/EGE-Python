file = open('files for 9/9_84345.txt', mode='r').readlines()
data = list(map(lambda x: x.split(), file))
count = 0
for i in data:
    line = list(map(int, i))
    chet = [line[2 - 1], line[4 - 1], line[6 - 1]]
    nechet = [line[1 - 1], line[3 - 1], line[5 - 1], line[7 - 1]]
    if len(set(line)) == 6 and max(nechet) > max(chet):
        count += 1
print(count)