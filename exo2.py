import sys


def main():
    lines = []
    for line in sys.stdin:
        lines.append(int(line.rstrip("\n")))

    smallest = min(lines)
    dropped = 0
    for line in lines:
        dropped += line - smallest
    print(dropped)


if __name__ == "__main__":
    main()
