def find_children():
    graph = {
        'A': ['B','C,', 'D'],
        'B': ['E','F'],
        'C': ['E']
    }

    for key in graph:
        print(key, "-", graph[key])

find_children()