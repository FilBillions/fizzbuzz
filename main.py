import sys
def main():
    if len(sys.argv) <= 2:
        print("Usage: python3 main.py <starting integer> <ending integer> --- not enough inputs")
        sys.exit(1)
    elif len(sys.argv) >= 4:
        print("Usage: python3 main.py <starting integer> <ending integer> --- too many inputs")
        sys.exit(1)

    for x in range(int(sys.argv[1]), int(sys.argv[2])):
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        print(x)


main()
