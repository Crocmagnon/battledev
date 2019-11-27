import sys

ROCK = "rock"
SPICE = "spice"


def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\n"))

    number_of_rocks, number_of_spices_types, capacity = map(int, lines[0].split())
    rocks = []
    spices = []
    for line in lines[1 : number_of_rocks + 1]:
        value, weight = map(int, line.split())
        rocks.append(
            {
                "type": ROCK,
                "total_value": value,
                "weight": weight,
                "cost_per_gram": value / weight,
            }
        )
    for line in lines[number_of_rocks + 1 :]:
        cost_per_gram, weight = map(int, line.split())
        spices.append(
            {
                "type": SPICE,
                "total_value": cost_per_gram * weight,
                "weight": weight,
                "cost_per_gram": cost_per_gram,
            }
        )
    items = []
    items.extend(rocks)
    items.extend(spices)
    items.sort(key=lambda x: x["cost_per_gram"], reverse=True)

    cash_prize = 0
    for item in items:
        if item["type"] == ROCK and capacity - item["weight"] >= 0:
            cash_prize += item["total_value"]
            capacity -= item["weight"]
        elif item["type"] == SPICE:
            taking = min(capacity, item["weight"])
            cash_prize += item["cost_per_gram"] * taking
            capacity -= taking
        if capacity == 0:
            print(cash_prize)
            return
    print(cash_prize)
    return


if __name__ == "__main__":
    main()
