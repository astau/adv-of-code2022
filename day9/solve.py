def main():
    data = parse_file("data.txt")
    
    # Part 1
    rope = []
    for i in range(2): # 2 knots i.e head=0 and tail=1
        rope.append((0, 0))
    tail_trace = [rope[-1]]
    for d, s in data:
         path = generate_path(rope[0], d, s)
         for p in path:        
            tail_trace.append(move_rope(rope, p))
    print(f"Answer 1: {len(set(tail_trace))}") # 5513

    # Part 2
    rope = []
    for i in range(10): # 10 knots i.e head=0 and tail=9
        rope.append((0, 0))
    tail_trace = [rope[-1]]
    for d, s in data:
         path = generate_path(rope[0], d, s)
         for p in path:        
            tail_trace.append(move_rope(rope, p))
    print(f"Answer 2: {len(set(tail_trace))}") # 2427

def move_rope(rope, p):
    rope[0] = p
    for k in range(1, len(rope)):
        far, newp = is_far(rope[k], rope[k-1])
        if far:
            rope[k] = newp 
        else:
            break
    return rope[-1] # return tail postion for trace

def is_far(frm, to):
    x, y = to[0] - frm[0], to[1] - frm[1]
    is_far = True if abs(x) > 1 or abs(y) > 1 else False
    x = int(x/abs(x)) if abs(x) > 1 else x
    y = int(y/abs(y)) if abs(y) > 1 else y
    return is_far, (frm[0]+x, frm[1]+y) # far flag and new point to bring 'frm' towards 'to'
        
def generate_path(frm, dir, steps):
    pts = []
    x, y = frm
    for s in range(steps):
        match dir:
            case 'L':
                x -= 1
            case 'R':
                x += 1
            case 'U':
                y += 1
            case 'D':
                y -= 1
        pts.append((x, y))
    return pts

def parse_file(fname):
    result = []
    with open(fname, "r") as file:
        rows = file.read().split('\n')
        for row in rows:
            d, s = row.strip().split()
            result.append((d, int(s)))
    return result

if __name__ == "__main__":
    main()