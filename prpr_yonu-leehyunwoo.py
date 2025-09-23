import random

def play_random(n: int) -> float:
    """
    #랜덤 전략: 죄수들이 무작위로 50개의 상자를 열어보는 경우
    :param n: #시뮬레이션 반복 횟수
    :return: #성공 확률 (%)
    """
    pardoned = 0  # 성공 횟수 카운트
    in_drawer = list(range(100))

    for _ in range(n):
        random.shuffle(in_drawer)  # 상자 섞기
        found = True  # 전체 성공 여부

        # 100명의 죄수 각각 시도
        for prisoner in range(100):
            # 무작위로 상자 50개 선택
            reveal_boxes = random.sample(range(100), 50)
            success = False

            for reveal in reveal_boxes:
                card = in_drawer[reveal]
                if card == prisoner:  # 자기 번호 찾으면 성공
                    success = True
                    break

            if not success:  # 한 명이라도 실패하면 전체 실패
                found = False
                break

        if found:
            pardoned += 1

    return (pardoned / n) * 100


def play_optimal(n: int) -> float:
    """
    #최적 전략: 각 죄수가 자신의 번호부터 시작해서 사이클을 따라가는 경우
    :param n: #시뮬레이션 반복 횟수
    :return: #성공 확률 (%)
    """
    pardoned = 0
    in_drawer = list(range(100))

    for _ in range(n):
        random.shuffle(in_drawer)
        found = True

        for prisoner in range(100):
            reveal = prisoner
            success = False

            for _ in range(50):
                card = in_drawer[reveal]
                if card == prisoner:
                    success = True
                    break
                reveal = card  # 다음 상자는 방금 본 카드 번호 위치

            if not success:
                found = False
                break

        if found:
            pardoned += 1

    return (pardoned / n) * 100


# 실행 예시
n = 100_000
print(f"Simulation count: {n}")
print(f"Random play wins: {play_random(n):.1f}% of simulations")
print(f"Optimal play wins: {play_optimal(n):.1f}% of simulations")

