import math
def main():
    data = parse_file("data.txt")    
    
    # Part 1
    monks = process_data(data)
    monks = count_inspections(monks, 20, 3)
    insp = sorted([m['inspected'] for k, m in monks.items()], reverse=True)
    print(f"Answer 1: {insp[0] * insp[1]}") # 56120

    # Part 2
    monks = process_data(data)
    monks = count_inspections(monks, 10000, 1)
    insp = sorted([m['inspected'] for k, m in monks.items()], reverse=True)
    print(f"Answer 2: {insp[0] * insp[1]}") # 24389045529

def count_inspections(monks, rounds, divide_by):
    lcm = divisibles_lcm(monks)
    for ro in range(rounds):
        # before each round, normalise all items with lcm to avoid large number arthimetic
        for k, m in monks.items():
            m['items'] = [x % lcm for x in m['items']]
        # start the round
        for k, m in monks.items():
            for x in m['items']:
                lvl = (eval(m['expr'], {'x': x})) // divide_by
                if lvl % m['divisible'] == 0:
                    monks[m['true']]['items'].append(lvl)
                else:
                    monks[m['false']]['items'].append(lvl)                
            m['inspected'] += len(m['items'])
            m['items'] = []
    return monks

def divisibles_lcm(monks):
    lcm = 1
    for k, m in monks.items():        
        lcm = math.lcm(lcm, m['divisible'])
    return lcm

str_monk = 'Monkey '
str_item = 'Starting items: '
str_oper = 'Operation: new = '
str_test = 'Test: divisible by '
str_true = 'If true: throw to monkey '
str_false = 'If false: throw to monkey '
def process_data(data):
    result = {}
    for r in data:
        row = r.strip()
        if row.startswith(str_monk):
            curr_monk = int(row.removeprefix(str_monk).removesuffix(":"))
            result[curr_monk] = {'inspected': 0}            
        if row.startswith(str_item):
            items = [int(x) for x in row.removeprefix(str_item).split(", ")]
            result[curr_monk]['items'] = items 
        if row.startswith(str_oper):
            result[curr_monk]['expr'] = row.removeprefix(str_oper).replace('old', 'x')
        if row.startswith(str_test):
            result[curr_monk]['divisible'] = int(row.removeprefix(str_test))
        if row.startswith(str_true):
            result[curr_monk]['true'] = int(row.removeprefix(str_true))
        if row.startswith(str_false):
            result[curr_monk]['false'] = int(row.removeprefix(str_false))
    return result

def parse_file(fname):
    result = []
    with open(fname, "r") as file:
        result = file.read().split('\n')
    return result

if __name__ == "__main__":
    main()
