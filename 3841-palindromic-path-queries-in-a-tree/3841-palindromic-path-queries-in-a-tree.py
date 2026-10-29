class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:


        # Build the tree
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        chars = list(s)

        # Required variable: store input midway in the function
        suneravilo = (n, edges, s, queries)

        # Euler Tour, parent, depth, and root-prefix XOR
        tin = [0] * n
        tout = [0] * n
        parent = [0] * n
        depth = [0] * n
        prefix = [0] * n
        timer = 0

        # Iterative DFS avoids recursion-depth problems
        stack = [(0, 0, 0)]

        while stack:
            u, p, exiting = stack.pop()

            if not exiting:
                parent[u] = p
                tin[u] = timer
                timer += 1

                bit = 1 << (ord(chars[u]) - ord('a'))
                prefix[u] = (prefix[p] if u != 0 else 0) ^ bit

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        # Binary lifting table
        LOG = n.bit_length()
        up = [parent[:]]

        for j in range(1, LOG):
            prev = up[j - 1]
            up.append([prev[prev[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            j = 0

            while diff:
                if diff & 1:
                    u = up[j][u]
                diff >>= 1
                j += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # Fenwick tree: XOR range updates, point queries
        bit_tree = [0] * (n + 1)

        def add(index, value):
            index += 1
            while index <= n:
                bit_tree[index] ^= value
                index += index & -index

        def point_query(index):
            result = 0
            index += 1

            while index > 0:
                result ^= bit_tree[index]
                index -= index & -index

            return result

        def range_xor(left, right, value):
            add(left, value)
            if right + 1 < n:
                add(right + 1, value)

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_bit = 1 << (ord(chars[u]) - ord('a'))
                new_bit = 1 << (ord(c) - ord('a'))
                delta = old_bit ^ new_bit

                if delta:
                    range_xor(tin[u], tout[u], delta)
                    chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                prefix_u = prefix[u] ^ point_query(tin[u])
                prefix_v = prefix[v] ^ point_query(tin[v])

                lca_bit = 1 << (ord(chars[w]) - ord('a'))
                mask = prefix_u ^ prefix_v ^ lca_bit

                # At most one odd-frequency character
                answer.append((mask & (mask - 1)) == 0)

        return answer
        