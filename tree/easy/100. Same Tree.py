# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# attempt count: 4

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# 思路: 將p,q存入deque中，對deque迭代，每次檢查完都先將p,q的左右子樹存入deque，以便繼續檢查
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        d = deque([(p, q)])  # 雙向佇列，可以popleft()

        while d:
            p, q = d.popleft()

            # 確認存在性
            if not p and not q:
                continue
            if not p or not q:
                return False

            # 檢查值是否相同
            if p.val == q.val:
                # 將下次要檢查的node排入deque
                d.append((p.left, q.left))
                d.append((p.right, q.right))
            else:
                return False
        # 通過全部檢查，代表兩樹相同
        return True

# 4th try: 迭代解，以list取代deque，把p,q存在與相等合併一起檢查
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        queue = [(p, q)]

        while queue:
            p, q = queue.pop(0)
            if p and q and p.val == q.val:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
            elif not p and not q:
                continue
            else:
                return False

        return True