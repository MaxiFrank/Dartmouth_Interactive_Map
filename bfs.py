from collections import deque
# from load_graph import load_graph


# Starting breadth first search
def bfs (start_vertex, goal_vertex):
    q = deque()
    path = []
    backpointer = {}
    q.append(start_vertex)

    # need to set the backpointer back to none so that the loop will stop
    backpointer[start_vertex] = None

    while q != None:
        # identifies the first vertex as the item to check for adjacent vertices
        first_vertex = q.popleft()
        if first_vertex == goal_vertex:
            # starts at goals vertex, and traces back path to start vertex, which will not have a backpointer
            while first_vertex != None:
                # add the first vertex to the path list
                path.append(first_vertex)
                # returns none when the backpointer of start vertex is checked
                first_vertex = backpointer[first_vertex]
            return path

        else:
            for item in first_vertex.adjacent_vertices:
                if item not in backpointer:
                    # check if item (D) is in dictionary, gives the backpointer (B) to item (D)
                    backpointer[item] = first_vertex
                    # appends item (D) to the end of queue to be checked for shortest path
                    q.append(item)

    return None

# test
# list_all_vertices = load_graph("dartmouth_graph.txt")
#
# path = bfs(list_all_vertices["1953 Commons"], list_all_vertices["Sudikoff"])
#
# for object in path:
#     print(object)

