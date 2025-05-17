import sys

input = sys.stdin.readline


class Trie:
    class Node:
        def __init__(self):
            self.child = [-1] * 26
            self.f = False
            self.Z = set()

    def __init__(self):
        self.nodes = [self.Node()]
        self.Z = set()

    # s is the added str, i is idx of added string (not prefix)
    def add(self, s, i, is_Y):
        k = 0
        for c in s:
            c = ord(c) - ord("a")
            node = self.nodes[k]
            if node.child[c] == -1:
                node.child[c] = len(self.nodes)
                self.nodes.append(self.Node())
            if is_Y:
                node.Z.add(i)
                if node.f:
                    self.Z.add(i)
            k = node.child[c]
        if is_Y:
            node = self.nodes[k]
            node.Z.add(i)
            if node.f:
                self.Z.add(i)
        else:
            node = self.nodes[k]
            node.f = True
            self.Z |= node.Z
            node.Z.clear()


Q = int(input())
trie = Trie()
Y = 0
for i in range(Q):
    T, S = input().rstrip().split()
    trie.add(S, i, T == "2")
    if T == "2":
        Y += 1
    print(Y - len(trie.Z))
