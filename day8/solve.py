def main():
    data = parse_file("data.txt")
    tree_map = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            tree_map[(i, j)] = (vis_score(data[i][j], xy_split(data, i, j)))
    
    # Part 1
    vis_count = sum([1 for k in tree_map if tree_map[k][0]])
    print(f"Answer 1: {vis_count}") # 1705

    # Part 2
    max_score = 0
    for k in tree_map:
        max_score = tree_map[k][1] if tree_map[k][1] > max_score else max_score
    print(f"Answer 2: {max_score}") #



# left, right, up, down sides of a given element i, j
def xy_split(data, i, j):
    col = [d[j]for d in data]
    row = data[i]
    return [list(reversed(row[0:j])), row[j+1:], list(reversed(col[0:i])), col[i+1:]]

# visibility flag and score of a given element
def vis_score(d, ll):
    vis = False
    score = 1
    for l in ll:
        v, s = side_vis_score(d, l)
        score *= s if s !=0 else 1
        vis |= v
    return vis, score

# visibility flag and score for an element of a given side
def side_vis_score(d, li):
    sc, l = 0, len(li)
    if l == 0:
        return True, 0
    for x in li:
        if d > x:
            sc += 1
        else:
            break
    return (True, sc) if l == sc else (False, sc+1)

def parse_file(fname):
    result = []
    with open(fname, "r") as file:
        rows = file.read().split('\n')
        for row in rows:
            result.append([int(i) for i in row])
    return result

if __name__ == "__main__":
    main()