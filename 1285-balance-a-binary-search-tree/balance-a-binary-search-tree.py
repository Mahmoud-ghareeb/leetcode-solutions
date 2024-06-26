# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def extract_values(root):
            
            v = []
            def dfs(node):
                if not node: return 0
                v.append(node.val)

                dfs(node.left)
                dfs(node.right)
            dfs(root)

            return sorted(v)

        nodes = extract_values(root)

        def build_bst(nodes):
            
            def place_node(node, parent, d):
                if not node:
                    if d == 'l':
                        parent.left = candidate
                    else:
                        parent.right = candidate
                    return


                if node.val > candidate.val:
                    place_node(node.left, node, 'l')
                else:
                    place_node(node.right, node, 'r')

            s_nodes = []
            def sort_nodes(s, e):
                if s >= e:
                    return

                c = nodes[s:e]
                n = len(c)
                if n == 0:
                    return

                if n%2 == 0:
                    idx = len(c)//2 -1
                else:
                    idx = len(c)//2

                s_nodes.append(c[idx])

                sort_nodes(s, s + idx)
                sort_nodes(s + idx + 1, e)


            sort_nodes(0, len(nodes))


            head = TreeNode(s_nodes[0])
            for n in s_nodes[1:]:
                candidate = TreeNode(n)
                place_node(head, None, None)

            return head

        return build_bst(nodes)
            

        