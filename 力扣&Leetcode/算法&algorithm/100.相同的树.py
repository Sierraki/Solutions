class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def fun(root: TreeNode, res: list):
            if not root:
                res.append("none")
                return
            res.append(root.val)
            fun(root.left, res)
            fun(root.right, res)

        res_p = []
        res_q = []
        fun(p, res_p)
        fun(q, res_q)
        return res_p == res_q
