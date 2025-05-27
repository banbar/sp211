from . import graph
import math

def shortest_path(graph, base_node):
    # Initialize cost and previous dictionaries
    costs = {node_id: math.inf for node_id in graph.nodes}
    visited = {node_id: False for node_id in graph.nodes}
    previous = {node_id: -1 for node_id in graph.nodes}


    costs[base_node] = 0 #initialise the cost to base node
    previous[base_node] = "Origin"

    current_node = base_node
    current_cost = 0

    # Explore neighbours, and the costs & previous
    while False in visited.values():
        neighbours = graph.get_neighbours(current_node)
        # Check the cost - if the cost is lower, update the costs & previous
        for i in range(len(neighbours)):
            if( (current_cost + neighbours[i][1] ) < costs[neighbours[i][0]] ):

                # update
                costs[neighbours[i][0]] = current_cost + neighbours[i][1]
                previous[neighbours[i][0]] = current_node

        # Choose the next node to visit - that having the minimum cost
        visited[current_node] = True
        unvisited_nodes = [node for node in graph.nodes if not visited[node]]
        

        #Update the current node
        if not unvisited_nodes:
            print("No unvisited nodes left — terminating.")
            break  
        
        # Fİnding the min-cost
        min_cost = math.inf
        current_node = None

        for k in unvisited_nodes:
            if costs[k] < min_cost:
                min_cost = costs[k]
                current_node = k

        # 1-line statement:
        # current_node = min(unvisited_nodes, key=lambda node: costs[node])
        current_cost = costs[current_node]

    return (costs, previous)




    
        
