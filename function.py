import random

#처음 시작
n = random.randint(1, 6)
print('결과: ', n)
n = random.randint(1, 6)
print('결과: ', n)
n = random.randint(1, 6)
print('결과: ', n)
n = random.randint(1, 6)
print('결과: ', n)
n = random.randint(1, 6)
print('결과: ', n)
n = random.randint(1, 6)
print('결과: ', n)

def rolling_dice(pip):
    n = random.randint(1, pip)
    print(pip, "면 주사위 굴린 결과: ",n)

rolling_dice(10)

def fn(a, b=[]):
    b.append(a)
    print(b)

fn(3)
fn(5)
fn(10)



def min(*numbers):
    min_value = numbers[0]
    for number in numbers:
        if min_value > number:
            min_value = number
    return min_value
result = min(1, 3,5,-1)
print(result)

def min_max(*args):
    min = args[0]
    max = args[0]
    for number in args:
        if min > number:
            min = number
        if max < number:
            max = number
    return min, max

a, b = min_max(10,9,20,3,-2,50)
print('min: ', a, 'max: ', b)