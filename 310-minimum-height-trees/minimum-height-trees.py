class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        adj_list = defaultdict(list)
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)

        leaves = [node for node in range(n) if len(adj_list[node]) == 1]

        remaining_nodes = n

        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)

            new_leaves = []

            # Remove current leaf nodes and update their neighbors
            for leaf in leaves:
                neighbor = adj_list[leaf][0]
                adj_list[neighbor].remove(leaf)

                # If the neighbor becomes a leaf node, add it to the new leaves list
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # Update the current leaf nodes for the next iteration
            leaves = new_leaves

        # At this point, the remaining nodes are the centers of the minimum height trees
        return leaves