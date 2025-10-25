from nary_tree import UnorderedNaryTree, Node

def test_ternary_tree():
    # --- Leaves ---
    n1  = Node(1)
    n2  = Node(2)
    n3  = Node(3)
    n4  = Node(4)
    n5  = Node(5)
    n6  = Node(6)
    n7  = Node(7)
    n8  = Node(8)
    n9  = Node(9)
    n10 = Node(10)
    n11 = Node(11)
    n12 = Node(12)
    n13 = Node(13)
    n14 = Node(14)
    n15 = Node(15)
    n16 = Node(16)
    n17 = Node(17)
    n18 = Node(18)
    n19 = Node(19)
    n20 = Node(20)
    n21 = Node(21)
    n22 = Node(22)
    n23 = Node(23)
    n24 = Node(24)
    n25 = Node(25)
    n26 = Node(26)
    n27 = Node(27)
    n27b = Node("27b")

    # --- Level 3 (parents of leaves) ---
    # Each node can have up to 3 children (ternary tree)
    n28 = Node(28, [n1, n2, n3])
    n29 = Node(29, [n4])                         # single child
    n30 = Node(30, [n5, n6, n7])
    n31 = Node(31, [n8, n9])                     # two children
    n32 = Node(32, [n10, n11, n12])
    n33 = Node(33, [n13, n14, n15])
    n34 = Node(34, [n16, n17, n18])
    n35 = Node(35, [n19, n20])                   # two children
    n36 = Node(36, [n21, n22, n23])
    n37 = Node(37, [n24, n25, n26])
    n38 = Node(38, [n27, n27b])                  # two children, one string value

    # --- Level 2 ---
    # Combine previous level nodes, not all perfectly balanced
    n39 = Node(39, [n28, n29, n30])
    n40 = Node(40, [n31, n32])                   # two children
    n41 = Node(41, [n33])                        # single child
    n42 = Node(42, [n34, n35, n36])
    n43 = Node(43, [n37, n38])                   # two children

    # --- Level 1 (roots) ---
    root_a = Node(90, [n39, n40, n41])           # three children
    root_b = Node(91, [n42])                     # single child
    root_c = Node(92, [n43, Node(93), Node(94)]) # mixed: two subtrees + one-leaf nodes

    # --- Level 0 (super-root) ---
    super_root = Node(200, [root_a, root_b, root_c])

    # --- Build and print ---
    tree = UnorderedNaryTree(super_root, n=3)
    tree.print_tree()

def test_binary_tree():
    # leaves
    n1  = Node(1)
    n2  = Node(2)
    n3  = Node(3)
    n4  = Node(4)
    n5  = Node(5)
    n6  = Node(6)
    n7  = Node(7)
    n8  = Node(8)
    n9  = Node(9)
    n10 = Node(10)
    n11 = Node(11)
    n12 = Node(12)
    n13 = Node(13)
    n14 = Node(14)
    n15 = Node(15)
    n15b = Node("15b")

    # level 3
    n16 = Node(16, [n1, n2])
    n17 = Node(17)#, [n3, n4])
    n18 = Node(18, [n5, n6])
    n19 = Node(19, [n7, n8])
    #n19 = Node(19, [n7])
    n20 = Node(20, [n9, n10])
    n21 = Node(21, [n11, n12])
    n22 = Node(22, [n13, n14])
    n23 = Node(23, [n15, n15b]) 

    # level 2
    n24 = Node(24, [n16, n17])
    n25 = Node(25, [n18, n19])
    n26 = Node(26)#, [n20, n21])
    #n26 = Node(26, [n20, n21])
    #n26 = Node(26, [n20])
    n27 = Node(27, [n22, n23])
    #n27 = Node(27, [n22])

    # level 1 (roots)
    root = Node(99, [n24, n25])
    right_root = Node(100, [n26, n27])

    # level 0 (super-root)
    super_root = Node(200, [root, right_root])
    # build the 3
    tree = UnorderedNaryTree(super_root)
    tree.print_tree()


test_ternary_tree()
test_binary_tree()

