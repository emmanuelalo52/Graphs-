from collections import deque
def breadth_first(graph,root):
    visited_vertices=list()
    graph_queue=deque([root])
    visited_vertices.append(root)
    node=root
    while len(graph_queue)>0:
        node=graph_queue.popleft()
        adj_nodes=graph[node]
        remaning_elements=set(adj_nodes).difference(visited_vertices)
        if len(remaning_elements)>0:
            for elem in sorted(remaning_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)
    return visited_vertices