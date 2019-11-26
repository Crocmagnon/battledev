def get_line():
    variable = input()


def get_line_as_list():
    variable = input().split(" ")


def get_line_as_int():
    variable = int(input())


def get_line_as_ints():
    variable = map(int, input().split(" "))


def get_lines():
    import sys

    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\n"))
