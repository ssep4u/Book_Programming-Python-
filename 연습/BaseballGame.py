#야구 게임
# make 정답
# 사용자 입력받자
# strike, ball 판정
# 정답 길이와 strike가 같다면 끝
import random

def make_answer():
    l = list(range(10))
    l.remove(0)
    random.shuffle(l)
    # answer = "".join(str(ch) for ch in l[:3])
    answer = l[:3]
    return answer


def play(input_string):
    strike = 0
    ball = 0
    for i, number in enumerate(answer):
        try:``
            search_index = input_string.index(str(number))
        except ValueError as identifier:
            # strike, ball없으면
            continue
            
        if search_index == i:
            strike += 1
        else:
            ball += 1

    return strike, ball


answer = make_answer()
while (True):
    input_string = input()
    (strike, ball) = play(input_string)
    print("strike: {}\tball: {}".format(strike, ball))
    if len(input_string) == strike:
        print("정답입니다.")
        break
