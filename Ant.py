# 개미수열
# 1
# 11
# 12
# 1121
# 122111

def to_ant(string_ant):
    ant = ""
    number = string_ant[0]
    count = 0
    for item in string_ant:
        if item == number:
            count+=1
        else:
            ant += number
            ant += str(count)
            number = item
            count = 1
    ant += number
    ant += str(count)

    return ant

result = ["1"]
for iter in range(10):
    s = to_ant(result[len(result)-1])
    result.append(s)

for item in result:
    print(item)