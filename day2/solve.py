def main():
    outcome1 = {
        ('A', 'X'): 4, # d(3) + sel(1)  rock/rock
        ('A', 'Y'): 8, # w(6) + sel(2)  rock/paper
        ('A', 'Z'): 3, # l(0) + sel(3)  rock/scissors
        ('B', 'X'): 1, # l(0) + sel(1)  paper/rock
        ('B', 'Y'): 5, # d(3) + sel(2)  paper/paper
        ('B', 'Z'): 9, # w(6) + sel(3)  paper/scissors
        ('C', 'X'): 7, # w(6) + sel(1)  scissors/rock
        ('C', 'Y'): 2, # l(0) + sel(2)  scissors/paper
        ('C', 'Z'): 6, # d(3) + sel(3)  scissors/scissors
    }

    outcome2 = { # X: lost, Y: draw, Z: won
        ('A', 'X'): 3, # l(0) + sel(3)  rock/scissors
        ('A', 'Y'): 4, # d(3) + sel(1)  rock/rock
        ('A', 'Z'): 8, # w(6) + sel(2)  rock/paper
        ('B', 'X'): 1, # l(0) + sel(1)  paper/rock
        ('B', 'Y'): 5, # d(3) + sel(2)  paper/paper
        ('B', 'Z'): 9, # w(6) + sel(3)  paper/scissors
        ('C', 'X'): 2, # l(0) + sel(2)  scissors/paper
        ('C', 'Y'): 6, # d(3) + sel(3)  scissors/scissors
        ('C', 'Z'): 7, # w(6) + sel(1)  scissors/rock
    }    

    data = parse_file("data.txt")
    score1 = score2 = 0
    for d in data:
        score1 += outcome1[d]
        score2 += outcome2[d]
    print(score1, score2)


def parse_file(fname):
    with open(fname, "r") as file:
        data = file.read().split('\n')
        result = []
        for d in data:
            result.append(tuple(d.split()))
    return result

main()