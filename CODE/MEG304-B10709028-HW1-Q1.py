

def Exercise23a():
    i: int = 0
    while (i <= 100):
        if (((i+1) % 10) == 0):
            print(f"{i:>3}")
        else:
            print(f"{i:>3}", end=" ")
        i = i + 1


def Exercise23b():
    i: int = 0
    while (i <= 100):
        if ((i % 7) == 0):
            print(i, end=" ")
        i = i + 1


def Exercise25():
    numberFound: int = 0
    x: int = 11
    while (numberFound < 20):
        if (((x % 5) == 0) and ((x % 7) == 0) and ((x % 11) == 0)):
            if (((numberFound + 1) % 10) == 0):
                print(f"{x:<4}")
            else:
                print(f"{x:<4}", end=" ")
            numberFound = numberFound + 1
        x = x + 1


def Exercise26():
    numberFound: int = 0
    i: int = 10
    while (numberFound < 1):
        if (((i % 7) == 0) and ((i % 8) == 0)
                and ((i % 9) == 0) and ((i % 10) == 0)):
            print(i)
            numberFound = numberFound + 1
        i = i + 1


def Exercise27():
    numberFound: int = 0
    i: int = 103
    print(f"{i:>4}", end=" ")
    while (i != 1):
        numberFound = numberFound + 1
        if ((i % 2) == 0):
            i = i // 2
        elif ((i % 2) == 1):
            i = 3 * i + 1
        
        if (((numberFound + 1) % 8) == 0):
            print(f"{i:>4}")
        else:
            print(f"{i:>4}", end=" ")


if __name__ == "__main__":
    print("\nExercise 2.3(a)\n")
    Exercise23a()
    print("\n\nExercise 2.3(b)\n")
    Exercise23b()
    print("\n\nExercise 2.5\n")
    Exercise25()
    print("\nExercise 2.6\n")
    Exercise26()
    print("\nExercise 2.7\n")
    Exercise27()
