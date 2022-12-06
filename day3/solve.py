def main():
    data = parse_file("data.txt")

    # Part 1
    weights = []
    for d in data:
        l = int(len(d)/2)
        chars = find_common_chars([d[:l], d[l:]])
        weights.append(char_weight(chars[0][0]))
    print("Answer 1:", sum(weights)) # 7817

    # Part 2
    weights = []
    for i in range(0, len(data), 3):
        chars = find_common_chars(data[i:i+3])
        weights.append(char_weight(chars[0]))
    print("Answer 2:", sum(weights)) # 2444

    
def parse_file(fname):
    with open(fname, "r") as file:
        data = file.read().split('\n')
        result = []
        for d in data:
            result.append(d.strip())
    return result

def find_common_chars(s_list):
    if len(s_list) > 2:
        lst = s_list[2:]
        lst.append(find_common_chars(s_list[:2]))
        return find_common_chars(lst)
    elif len(s_list) == 2:
        return ''.join([c for c in s_list[0] if c in s_list[1]])

def char_weight(c):
    c = ord(c)
    if 96 < c < 127:
        return c - 96
    elif 64 < c < 91:
        return c - 64 + 26
    else:
        return -1


main()