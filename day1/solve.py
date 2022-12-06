def main():
    data = parse_file("data.txt") # get the data in dictionary key: elf number starting at 1 and values: list of calories

    data = {k: sum(v) for k, v in data.items()} # dictionary values are reduced to sum(list)
    data = {k: v for k, v in sorted(data.items(), key=lambda it: it[1])} # highest sum of calories at the end

    data_list = list(data.items())
    
    # Max calories
    elf, cals = data_list[-1]
    print(f"Elf:{elf} - Cals:{cals}")

    # Top 3 calories
    top3 = data_list[-3:]
    print()
    print(f"Elf:{top3[0][0]} - Cals:{top3[0][1]}")
    print(f"Elf:{top3[1][0]} - Cals:{top3[1][1]}")
    print(f"Elf:{top3[2][0]} - Cals:{top3[2][1]}")
    print(f"Total Cals: {top3[0][1] + top3[1][1] + top3[2][1]}")

def parse_file(fname):
    with open(fname, "r") as file:
        data = file.read().split('\n')
        result = {}
        cals = []
        key = 1
        for d in data:
            if d == '':
                result[key] = cals
                key += 1
                cals = []
            else:
                cals.append(int(d))
    return result

main()