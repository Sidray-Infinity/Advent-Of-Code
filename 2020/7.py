from collections import defaultdict

def hasGold(graph, x):
    if "shiny gold" in graph[x]:
        return True
    if "other bags" in graph[x]:
        return False

    return any([hasGold(graph, c) for c in graph[x]])

def countBags(graph, x):
    sum_ = 0
    for e in x:
        sum_ += e[0]
        if graph[e[1]][0][0] == 0:
            continue
        
        sum_ += e[0] * countBags(graph, graph[e[1]])

    return sum_

if __name__ == "__main__":
    rules = open("7.txt").read().split('\n')
    graph = {}
    for r in rules:
        parent, children = r.split('contain')[0][:-5].strip(), r.split('contain')[1].strip().split(', ') 
        graph[parent] = set([' '.join(c.split(' ')[1:3]).split('.')[0] for c in children])

    count = 0
    for bag in graph.keys():
        if hasGold(graph, bag):
            count += 1
    print('Part1:', count)

    graph = defaultdict(list)
    for r in rules:
        parent, children = r.split('contain')[0][:-5].strip(), r.split('contain')[1].strip().split(', ') 
        for c in children:
            num, cbags = c.split(' ', 1)
            if num == "no":
                graph[parent].append((0, ""))
            else:
                graph[parent].append((int(num), ' '.join(cbags.split('.')[0].split(' ')[0:2])))
    
    count = countBags(graph, graph['shiny gold'])
    print('Part2:', count)
