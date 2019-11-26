import sys


def assign_cable(cables):
    for i, available in enumerate(cables):
        if available == 1:
            cables[i] = 0
            return i + 1
    return False


def restore_cable(cables, cable):
    cables[cable] = 1


def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\n"))

    number_of_cables, number_of_requests = map(int, lines[0].split())
    cables = []
    requests = []
    for _ in range(number_of_cables):
        cables.append(1)
    for line in lines[1:]:
        start, end = map(int, line.split())
        requests.append({"start": start, "end": end, "cable": None})

    assignations = []

    for time in range(2501):
        for request in requests:
            if time == request["end"]:
                restore_cable(cables, request["cable"])
        for request in requests:
            if time == request["start"]:
                cable = assign_cable(cables)
                if cable is False:
                    print("pas possible")
                    return
                else:
                    request["cable"] = cable
                    assignations.append(cable)

    print(" ".join(map(str, assignations)))


if __name__ == "__main__":
    main()
