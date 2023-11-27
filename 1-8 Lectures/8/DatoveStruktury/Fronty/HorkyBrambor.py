from collections import deque

def horky_brambor(seznam_hracu, k):
    fronta = deque(seznam_hracu)
    kola = 1

    while len(fronta) > 1:
        for _ in range(k - 1):
            fronta.append(fronta.popleft())

        vypadly = fronta.popleft()
        print(f"{vypadly} vypadl v {kola}. kole")

        kola += 1

    vitez = fronta.pop()
    print(f"{vitez} vyhrál!")

# Příklad použití:
seznam_hracu = ["Alice", "Bob", "Charlie", "David", "Eva"]
k = 7
horky_brambor(seznam_hracu, k)
