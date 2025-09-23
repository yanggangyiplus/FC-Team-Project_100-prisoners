import random

def play_random(n):
    pardoned = 0
    for _ in range(n):
        boxes = list(range(100))
        random.shuffle(boxes)
        success = True
        for prisoner in range(100):
            found = False
            for attempt in random.sample(range(100), 50):
                if boxes[attempt] == prisoner:
                    found = True
                    break
            if not found:
                success = False
                break
        if success:
            pardoned += 1
    return pardoned / n * 100

def play_optimal(n):
    pardoned = 0
    for _ in range(n):
        boxes = list(range(100))
        random.shuffle(boxes)
        success = True
        for prisoner in range(100):
            found = False
            reveal = prisoner
            for _ in range(50):
                if boxes[reveal] == prisoner:
                    found = True
                    break
                reveal = boxes[reveal]
            if not found:
                success = False
                break
        if success:
            pardoned += 1
    return pardoned / n * 100

if __name__ == "__main__":
    n = 100_000
    print('Simulation count:', n)
    print(f"Random play wins: {play_random(n):.2f}%")
    print(f"Optimal play wins: {play_optimal(n):.2f}%")


