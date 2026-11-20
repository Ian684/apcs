def solve(words):
    root = {}
    for word in words:
        node = root
        for char in word:
            node = node.setdefault(char, {})
        node['$'] = True
    return root

if __name__ == "__main__":
    print("Exercise: 37_trie")
