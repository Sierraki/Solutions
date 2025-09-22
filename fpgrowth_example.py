class TreeNode:
    """
    FP树的节点结构
    """
    def __init__(self, name, count, parent):
        self.name = name  # 节点名称
        self.count = count  # 计数
        self.parent = parent  # 父节点
        self.children = {}  # 子节点
        self.link = None  # 节点链表，连接相同名称的节点
        
    def increment(self, count):
        """
        增加节点计数
        """
        self.count += count
        
    def display(self, indent=1):
        """
        显示树结构
        """
        print(' ' * indent, self.name, ' ', self.count)
        for child in self.children.values():
            child.display(indent + 1)


def create_fp_tree(data, min_support):
    """
    构造FP树
    :param data: 原始数据集
    :param min_support: 最小支持度
    :return: FP树和头表
    """
    # 第一次扫描：计算每个项的支持度
    header = {}
    for transaction in data:
        for item in transaction:
            header[item] = header.get(item, 0) + 1
    
    # 过滤不满足最小支持度的项
    header = {item: count for item, count in header.items() if count >= min_support}
    
    # 如果没有满足条件的项，返回空
    freq_items = set(header.keys())
    if len(freq_items) == 0:
        return None, None
    
    # 初始化头表链接
    for item in header:
        header[item] = [header[item], None]
    
    # 创建根节点
    fp_tree = TreeNode('Null', 1, None)
    
    # 第二次扫描：构造FP树
    for transaction in data:
        # 只保留在频繁项中的元素，并按支持度降序排列
        local_items = {}
        for item in transaction:
            if item in freq_items:
                local_items[item] = header[item][0]
        
        if len(local_items) > 0:
            # 按支持度降序排序
            ordered_items = [item[0] for item in sorted(local_items.items(), 
                                                       key=lambda x: (-x[1], x[0]))]
            # 更新树
            update_tree(ordered_items, fp_tree, header, 1)
    
    return fp_tree, header


def update_tree(items, tree, header, count):
    """
    更新FP树
    :param items: 排序后的项列表
    :param tree: 当前树节点
    :param header: 头表
    :param count: 计数
    """
    # 如果第一个项已作为子节点存在，则增加计数
    if items[0] in tree.children:
        tree.children[items[0]].increment(count)
    else:
        # 否则创建新节点
        tree.children[items[0]] = TreeNode(items[0], count, tree)
        
        # 更新头表链接
        if header[items[0]][1] is None:
            header[items[0]][1] = tree.children[items[0]]
        else:
            update_header(header[items[0]][1], tree.children[items[0]])
    
    # 递归处理剩余项
    if len(items) > 1:
        update_tree(items[1:], tree.children[items[0]], header, count)


def update_header(start_node, target_node):
    """
    更新头表链接
    """
    while start_node.link is not None:
        start_node = start_node.link
    start_node.link = target_node


def load_simple_data():
    """
    加载简单示例数据
    """
    simple_data = [
        ['r', 'z', 'h', 'j', 'p'],
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
        ['z'],
        ['r', 'x', 'n', 'o', 's'],
        ['y', 'r', 'x', 'z', 'q', 't', 'p'],
        ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']
    ]
    return simple_data


if __name__ == '__main__':
    # 加载数据
    data = load_simple_data()
    print("原始数据集:")
    for i, transaction in enumerate(data):
        print(f"事务 {i+1}: {transaction}")
    
    # 构造FP树
    min_support = 3
    print(f"\n最小支持度: {min_support}")
    fp_tree, header = create_fp_tree(data, min_support)
    
    # 显示结果
    if fp_tree is not None:
        print("\nFP树结构:")
        fp_tree.display()
        
        print("\n头表:")
        for item, (count, node) in header.items():
            print(f"{item}: 支持度={count}")
    else:
        print("没有满足最小支持度的频繁项")