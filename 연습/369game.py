# 369 게임
def count_369(number):
    count = 0
    for ch in str(number):
        i = int(ch)
        if i in [3, 6, 9]:
            count += 1

    return count

print("369 게임")
for i in range(100):
    if i == 0:
        continue
    # 숫자에 3, 6, 9가 몇 개 있는가?
    count = count_369(i)
    if count == 0:
        print(i)
    else:
        print("짝"*count)



