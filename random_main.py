import random

season = ['봄', '여름', '가을', '겨울']
r = random.choice(season)
print(r)


for i in range(10):
    r = random.randrange(1, 7, 2)
    print(r)
print("----")

random.shuffle(season)
print(season)

lotto = range(1, 45 + 1)
print(lotto)
print(random.sample(lotto, 6))

