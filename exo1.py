import sys


def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\n"))

    lengths = {}
    for line in lines[1:]:
        name, length = line.split()
        length = int(length)
        lengths[length] = name

    print(lengths[sorted(lengths.keys())[0]])


if __name__ == "__main__":
    main()
