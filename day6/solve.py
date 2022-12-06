def main():
    data = parse_file("data.txt")
    
    # Part 1
    ans = marker_index(data, 4)
    print(f"Answer 1: {ans}") # 1855
    ans = marker_index(data, 14)
    print(f"Answer 2: {ans}") # 3256


def marker_index(string, word_length):
    for i in range(len(string)-word_length-1):
        if is_unique_chars(string[i:i+word_length]):
        #if unique_chars(string[i:i+word_length]) == word_length:
            return i + word_length

def unique_chars(word):
    return len([c for c in word if word.count(c) == 1])

def is_unique_chars(word):
    for i in range(len(word)):
        if word[i+1:].count(word[i]) != 0:
            return False
    return True
    

def parse_file(fname):
    with open(fname, "r") as file:
        data = file.read().strip()
    return data

if __name__ == "__main__":
    main()