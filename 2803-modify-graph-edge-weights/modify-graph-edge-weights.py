
import heapq

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        nbs = {i: [] for i in range(n)}
        for edge in edges:
            s, t, w = edge
            nbs[s].append((t, w))
            nbs[t].append((s, w))

        min_dists_to_source = get_min_dists_to_source(nbs, source)
        if min_dists_to_source[destination] > target:
            return []

        new_weights = {}

        visited = set()
        q = [(0, destination)]
        while len(q) > 0:
            d, node = heapq.heappop(q)
            if node in visited:
                continue
            visited.add(node)
            # print(f"Found node {node} at a distance {d} from destination.")

            if node == source:
                if d != target:
                    return []
                break

            for nb, w in nbs[node]:
                if w == -1:
                    key = (min(node, nb), max(node, nb))
                    if key not in new_weights:
                        new_w = max(1, target - d - min_dists_to_source[nb])
                        new_weights[key] = new_w
                    w = new_weights[key]
                heapq.heappush(q, (d+w, nb))
        
        # if distance_to_target is None:  # disconnected
        new_edges = []
        for edge in edges:
            s, t, w = edge
            if w == -1:
                key = (min(s, t), max(s, t))
                w = new_weights.get(key, 1)
            new_edges.append([s, t, w])
        return new_edges


def get_min_dists_to_source(nbs, source):
    min_distances = {}
    q = [(0, source)]
    while len(q) > 0:
        d, node = heapq.heappop(q)
        if node in min_distances.keys():
            continue

        # print(f"Found node {node} at a distance {d}.")
        min_distances[node] = d

        for nb, edge_w in nbs[node]:
            if edge_w == -1:
                edge_w = 1
            heapq.heappush(q, (d+edge_w, nb))
    return min_distances