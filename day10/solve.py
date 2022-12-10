def main():
    data = parse_file("data.txt")
    
    # Part 1
    signal = []
    x = 1
    for ins in data:
        if ins == "noop":
            signal.append(x)
        else:
            signal.append(x)
            signal.append(x)
            x = x + ins[1]
    
    sig_strength = 0
    for i in range(19, len(signal), 40):
        sig_strength += signal[i] * (i + 1)
    print(f"Answer 1: {sig_strength}") # 13680

    # Part 2
    for i in range(len(signal)):
        if i % 40 == 0:
            print()
        px = "#" if abs(signal[i]-(i % 40)) < 2 else "." # instead of dot (.), space (" ") makes the answer clear
        print(px, end="")
    print()
    # Answer: PZGPKPEB

def parse_file(fname):
    result = []
    with open(fname, "r") as file:
        rows = file.read().split('\n')
        for row in rows:
            op, *x = row.strip().split()
            if len(x) > 0:
                result.append((op, int(x[0])))
            else:
                result.append(op)
    return result

if __name__ == "__main__":
    main()