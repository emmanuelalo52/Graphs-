def depth_first(graph,root):
    visited_vertices=list()
    graph_stack=list()
    graph_stack.append(root)
    node=root
    while len(graph_stack)>0:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes=graph[node]
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
        if len(graph_stack)>0:
            node=graph_stack[-1]
            continue
        else:
            element_remaining=set(adj_nodes).difference(set(visited_vertices))
        first_adj_node=sorted(element_remaining)[0]
        graph_stack.append(first_adj_node)
        node=first_adj_node
    return visited_vertices