def levelOrder( root ):
    # Code here
    level_order = []
    level_order_data = []
    level_order.append(root)
    level_order_data.append(root.data)
    node = root
    while  len(level_order)!=0:
        node = level_order[0]
        if node.left:
            left_data = node.left.data
            level_order.append(node.left)
            level_order_data.append(left_data)
        if node.right:
            right_data = node.right.data
            level_order.append(node.right)
            level_order_data.append(right_data)
        level_order.pop(0)
        
        
    return level_order_data
    
