def main():
    data = parse_file("data.txt")

    # Part 1
    count = 0
    for d in data:
        if is_sub_range(d[0], d[1]) or is_sub_range(d[1], d[0]):
            count += 1
    print(f"Answer 1: {count}") # 651

    # Part 2
    count = 0
    for d in data:
        if is_overlap_range(d[0], d[1]):
            count += 1
    print(f"Answer 2: {count}")  # 956


def parse_file(fname):
    with open(fname, "r") as file:
        data = file.read().split('\n')
        result = []
        for d in data:
            r1, r2 = d.split(',')
            r1, r2 = r1.split('-'), r2.split('-')
            r1 = range(int(r1[0]), int(r1[1])+1)
            r2 = range(int(r2[0]), int(r2[1])+1)
            result.append((r1, r2))
    return result

def is_sub_range(r1, r2): #if r1 is sub of r2
    if not r1:
        return True
    if not r2:
        return False
    if len(r1) > 1 and r1.step % r2.step:
        return False
    
    return r1.start in r2 and r1[-1] in r2

def is_overlap_range(r1, r2): #if r1 and r2 have at least 1 overlap
    return r1.start in r2 or r2.start in r1

main()