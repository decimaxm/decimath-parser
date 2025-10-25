from nary_tree import UnorderedNaryTree, Node

def test_6_ary_tree():
    # --- Level 2 (leaves, smallest numbers) ---
    n1  = Node(36)
    n2  = Node(35)
    n3  = Node(34)
    n4  = Node(33)
    n5  = Node(32)
    n6  = Node(31)
    n7  = Node(30)
    n8  = Node(29)
    n9  = Node(28)
    n10 = Node(27)
    n11 = Node(26)
    n12 = Node(25)
    n13 = Node(24)
    n14 = Node(23)
    n15 = Node(22)
    n16 = Node(21)
    n17 = Node(20)
    n18 = Node(19)
    n19 = Node(18)
    n20 = Node(17)
    n21 = Node(16)
    n22 = Node(15)
    n23 = Node(14)
    n24 = Node(13)
    n25 = Node(12)
    n26 = Node(11)
    n27 = Node(10)
    n28 = Node(9)
    n29 = Node(8)
    n30 = Node(7)
    n31 = Node(6)
    n32 = Node(5)
    n33 = Node(4)
    n34 = Node(3)
    n35 = Node(2)
    n36 = Node(1)

    # --- Level 1 ---
    n37 = Node(42, [n1, n2, n3, n4, n5, n6])
    n38 = Node(41, [n7, n8, n9, n10, n11, n12])
    n39 = Node(40, [n13, n14, n15, n16, n17, n18])
    n40 = Node(39, [n19, n20, n21, n22, n23, n24])
    n41 = Node(38, [n25, n26, n27, n28, n29, n30])
    n42 = Node(37, [n31, n32, n33, n34, n35, n36])

    # --- Level 0 (root) ---
    super_root = Node(48, [n37, n38, n39, n40, n41, n42])

    # --- Build and print ---
    tree = UnorderedNaryTree(super_root, n=6)
    tree.print_tree()

def test_5_ary_tree():
    # --- Level 2 (leaves, smallest numbers) ---
    n1  = Node(25)
    n2  = Node(24)
    n3  = Node(23)
    n4  = Node(22)
    n5  = Node(21)
    n6  = Node(20)
    n7  = Node(19)
    n8  = Node(18)
    n9  = Node(17)
    n10 = Node(16)
    n11 = Node(15)
    n12 = Node(14)
    n13 = Node(13)
    n14 = Node(12)
    n15 = Node(11)
    n16 = Node(10)
    n17 = Node(9)
    n18 = Node(8)
    n19 = Node(7)
    n20 = Node(6)
    n21 = Node(5)
    n22 = Node(4)
    n23 = Node(3)
    n24 = Node(2)
    n25 = Node(1)

    # --- Level 1 ---
    n26 = Node(30, [n1, n2, n3, n4, n5])
    n27 = Node(29, [n6, n7, n8, n9, n10])
    n28 = Node(28)#, [n11, n12, n13, n14, n15])
    n29 = Node(27, [n16, n17, n18])#, n19, n20])
    n30 = Node(26, [n21, n22, n23, n24, n25])

    # --- Level 0 (root) ---
    super_root = Node(35, [n26, n27, n28, n29, n30])

    # --- Build and print ---
    tree = UnorderedNaryTree(super_root, n=5)
    tree.print_tree()

def test_quaternary_tree():
    # --- Level 2 (leaves, smallest numbers) ---
    n1  = Node(16)
    n2  = Node(15)
    n3  = Node(14)
    n4  = Node(13)
    n5  = Node(12)
    n6  = Node(11)
    n7  = Node(10)
    n8  = Node(9)
    n9  = Node(8)
    n10 = Node(7)
    n11 = Node(6)
    n12 = Node(5)
    n13 = Node(4)
    n14 = Node(3)
    n15 = Node(2)
    n16 = Node(1)

    # --- Level 1 ---
    n17 = Node(20, [n1, n2, n3, n4])
    n18 = Node(19, [n5, n6, n7, n8])
    n19 = Node(18)#, [n9, n10, n11, n12])
    n20 = Node(17, [n13, n14, n15, n16])

    # --- Level 0 (root) ---
    super_root = Node(24, [n17, n18, n19, n20])

    # --- Build and print ---
    tree = UnorderedNaryTree(super_root, n=4)
    tree.print_tree()

def test_ternary_tree():
    # --- Level 3 (leaves, smallest numbers) ---
    n1  = Node(73)
    n2  = Node(72)
    n3  = Node(71)
    n4  = Node(70)
    n5  = Node(69)
    n6  = Node(68)
    n7  = Node(67)
    n8  = Node(66)
    n9  = Node(65)
    n10 = Node(64)
    n11 = Node(63)
    n12 = Node(62)
    n13 = Node(61)
    n14 = Node(60)
    n15 = Node(59)
    n16 = Node(58)
    n17 = Node(57)
    n18 = Node(56)
    n19 = Node(55)
    n20 = Node(54)
    n21 = Node(53)
    n22 = Node(52)
    n23 = Node(51)
    n24 = Node(50)
    n25 = Node(49)
    n26 = Node(48)
    n27 = Node(47)
    
    # --- Level 2 ---
    n28 = Node(96, [n1, n2, n3])
    n29 = Node(95, [n4, n5, n6])
    n30 = Node(94, [n7, n8, n9])
    n31 = Node(93, [n10, n11, n12])
    n32 = Node(92, [n13, n14, n15])
    n33 = Node(91, [n16, n17, n18])
    n34 = Node(90)#, [n19, n20, n21])
    n35 = Node(89, [n22, n23, n24])
    n36 = Node(88, [n25, n26, n27])
    
    # --- Level 1 ---
    n37 = Node(99, [n28, n29, n30])
    #n38 = Node(98, [n31, n32, n33])
    n38 = Node(98, [n31, n32])#, n33])
    n39 = Node(97, [n34, n35, n36])
    
    # --- Level 0 (root) ---
    super_root = Node(100, [n37, n38, n39])
    
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


test_binary_tree()
test_ternary_tree()
test_quaternary_tree()
test_5_ary_tree()
test_6_ary_tree()

