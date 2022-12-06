def main():
    head, steps = parse_file("data.txt")
    h0, h1, h2 = head.copy(), head.copy(), head.copy()
    sto = form_stack(h0) # orginal
    st1 = form_stack(h1) # For part 1
    st2 = form_stack(h2) # For part 1
    for s in steps:
        ls = s.strip().split()
        fr, to, mv = ls[3].strip(), ls[5].strip(), int(ls[1].strip())
        # Part 1
        for i in range(mv):
            st1[to].append(st1[fr].pop())
        #Part 2
        st2[to].extend(st2[fr][-mv:])
        del st2[fr][-mv:]

    p1 = ''
    for k in st1:
        p1 += st1[k][-1].lstrip('[').rstrip(']')
    print(f"Answer 1: {p1}") # TLFGBZHCN

    p2 = ''
    for k in st2:
        p2 += st2[k][-1].lstrip('[').rstrip(']')
    print(f"Answer 2: {p2}") #     

def form_stack(head):
    if len(head) < 2:
        raise ValueError
    # Count number of stacks
    result = {}
    header = [x.strip() for x in head.pop().split()]
    for c in header:
        result[c] = []
    stack_sz = len(result)

    # Fill stacks
    while True:
        try:
            row = str_parts(head.pop(), stack_sz)
            for k in result:
                s = row[int(k)-1].strip()
                if len(s) > 0:
                    result[k].append(s)
        except IndexError:
            break    
    return result

# Split string into chunks using given length
def str_chunks(s, l):
    return [s[0+i:l+i] for i in range(0, len(s), l)]

# Split string into parts using given parts counts
def str_parts(s, p):
    return str_chunks(s, int(len(s)/p))

def parse_file(fname):
    with open(fname, "r") as file:
        stack = []
        steps = []
        is_step = False
        for ln in file:
            ln = ln.replace('\n', ' ')
            l = len(ln.strip())
            if l == 0:
                is_step = True
                continue
            if not is_step:
                stack.append(ln)
            if is_step:
                steps.append(ln)
    return stack, steps

if __name__ == "__main__":
    main()