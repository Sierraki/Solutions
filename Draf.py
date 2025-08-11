from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        将一个二叉搜索树（BST）转换为一个右倾斜的、递增顺序的搜索树。
        该方法使用中序遍历，并直接在遍历过程中重新链接节点。

        Args:
            root (Optional[TreeNode]): 输入的二叉搜索树的根节点。

        Returns:
            Optional[TreeNode]: 转换后树的根节点。
        """
        # 使用一个虚拟头节点来简化代码，它将指向新树的根。
        dummy = TreeNode()
        # pre 指针用于追踪中序遍历中的上一个节点，初始指向虚拟头节点。
        pre = dummy

        def inorder(node: Optional[TreeNode]):
            nonlocal pre
            if not node:
                return

            # 1. 递归遍历左子树。
            inorder(node.left)

            # 2. 处理当前节点（中序遍历的核心）。
            # 移除当前节点的左子节点，因为新树中没有左子节点。
            node.left = None
            # 将上一个节点的右子节点指向当前节点。
            pre.right = node
            # 更新 pre 指针，使其指向当前节点，为下一个节点做准备。
            pre = node

            # 3. 递归遍历右子树。
            inorder(node.right)

        # 开始中序遍历
        inorder(root)

        # 返回虚拟头节点的右子节点，它就是新树的根。
        return dummy.right
