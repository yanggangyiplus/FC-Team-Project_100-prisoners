import random

def play_random(n):
    # using 0-99 instead of ranges 1-100
    pardoned = 0
    in_drawer = list(range(100))
    sampler = list(range(100))
    for _round in range(n):
        random.shuffle(in_drawer)
        found = False
        for prisoner in range(100):
            found = False
            for reveal in random.sample(sampler, 50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / n * 100   # %

if __name__ == '__main__':
    n = 100_000
    print(" Simulation count:", n)
    print(f" Random play wins: {play_random(n):4.1f}% of simulations")
