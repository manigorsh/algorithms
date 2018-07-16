from collections import deque

def bfs(start, final):
    counter = 0
    search_queue = deque()
    search_queue.append(start)
    searched = []
    parents = {}
    parents[start] = None

    while search_queue:
        counter += 1
        vert = search_queue.popleft()
        print(vert)
        if not vert in searched:
            if vert == final:
                print("final is reached")
                p = vert
                while p != None:
                    print(p)
                    p = parents[p]
                print(counter)
                return True
            else:
                neighb = [item for item in neighbours(vert, final) if item not in searched]
                for n in neighb:
                    parents[n] = vert
                search_queue.extend(neighb)
                searched.append(vert)
    return False

def neighbours(vertex, final):
    if abs(final[0] - vertex[0]) < 4 and abs(final[1] - vertex[1]) < 4 or final[0] == vertex[0]or final[1] == vertex[1]:
        return [(vertex[0] + x, vertex[1] + y) for x in [-2, -1, 1, 2] for y in [-2, -1, 1, 2] if abs(x) != abs(y) and vertex[0] + x >= 0 and vertex[0] + x <= 1000 and vertex[1] + y >= 0 and vertex[1] + y <= 1000]
    elif final[0] > vertex[0] and final[1] >= vertex[1]:
        #return [(vertex[0] + x, vertex[1] + y) for x in [1, 2] for y in [1, 2] if abs(x) != abs(y) and vertex[0] + x >= 0 and vertex[0] + x <= 1000 and vertex[1] + y >= 0 and vertex[1] + y <= 1000]
        return [(vertex[0] + x, vertex[1] + y) for x in [1] for y in [2] if abs(x) != abs(y) and vertex[0] + x >= 0 and vertex[0] + x <= 1000 and vertex[1] + y >= 0 and vertex[1] + y <= 1000]
    elif final[0] <= vertex[0] and final[1] > vertex[1]:
        #return [(vertex[0] + x, vertex[1] + y) for x in [-2, -1] for y in [1, 2] if abs(x) != abs(y) and vertex[0] + x >= 0 and vertex[0] + x <= 1000 and vertex[1] + y >= 0 and vertex[1] + y <= 1000]
        return [(vertex[0] + x, vertex[1] + y) for x in [-2] for y in [1] if abs(x) != abs(y) and vertex[0] + x >= 0 and vertex[0] + x <= 1000 and vertex[1] + y >= 0 and vertex[1] + y <= 1000]
    elif final[0] <= vertex[0] and final[1] < vertex[1]:
        #return [(vertex[0] + x, vertex[1] + y) for x in [-2, -1] for y in [-2, -1] if abs(x) != abs(y) and vertex[0] + x >= 0 and vertex[0] + x <= 1000 and vertex[1] + y >= 0 and vertex[1] + y <= 1000]
        return [(vertex[0] + x, vertex[1] + y) for x in [-1] for y in [-2] if abs(x) != abs(y) and vertex[0] + x >= 0 and vertex[0] + x <= 1000 and vertex[1] + y >= 0 and vertex[1] + y <= 1000]
    elif final[0] > vertex[0] and final[1] <= vertex[1]:
        #return [(vertex[0] + x, vertex[1] + y) for x in [1, 2] for y in [-2, -1] if abs(x) != abs(y) and vertex[0] + x >= 0 and vertex[0] + x <= 1000 and vertex[1] + y >= 0 and vertex[1] + y <= 1000]
        return [(vertex[0] + x, vertex[1] + y) for x in [2] for y in [-1] if abs(x) != abs(y) and vertex[0] + x >= 0 and vertex[0] + x <= 1000 and vertex[1] + y >= 0 and vertex[1] + y <= 1000]

def main():
    start = (0, 0)
    final = (1000, 1000)
    bfs(start, final)

if __name__ == "__main__":
    main()