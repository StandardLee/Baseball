from random import randint

# 랜덤으로 생성된 3개의 숫자를 중복 없이 하나씩 numbers 리스트에 append 해주세요!
def generate_numbers():
    numbers = []
    return numbers


# 콘솔에서 숫자를 하나씩 받아 중복 없이, 0~9의 수를 3번 new_guess리스트에 하나씩 append해주세요!
def take_guess():
    new_guess = []
    return new_guess

# guesses로 받은 리스트와 solution의 리스트에 중복되는 숫자가 있는지 그리고 인덱스까지 같은 숫자가 있는지 판별해주세요!
# 인덱스까지 같다면 strike를 1 추가, 인덱스는 다르지만 리스트에 있다면 ball을 1 추가!
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break

print("축하합니다. {}번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다.".format(tries))
