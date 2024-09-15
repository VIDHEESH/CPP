class Node:
  def __init__(self,data):
    self.data=data
    self.right=None
    self.left=None
class Solution:
  def btodll(self,root):
    def inorder(root):
      if root.left:
        pred=root.left
        while pred.right:
          pred=pred.right
        inorder(root.left)
        pred.right=root
        root.left=pred
      if root.right:
        succ=root.right
        while succ.left:
          succ=succ.left
        inorder(root.right)
        root.right=succ
        succ.left=root
    if root is None:
      return root
    head=root
    while head.left:
      head=head.left
    inorder(root)
    return head
