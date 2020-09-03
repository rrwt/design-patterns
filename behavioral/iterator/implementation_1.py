"""
Implement BFS and DFS of a binary search tree
"""
from abc import ABCMeta, abstractmethod
from collections import deque
from typing import Optional


class Iterator(metaclass=ABCMeta):
    def __init__(self, root_node: "TreeInterface.Node") -> None:
        self.root_node = root_node
        self.iterator = self._iterate(self.root_node)

    @abstractmethod
    def _iterate(self, cur_node: "TreeInterface.Node"):
        pass

    def next(self):
        return next(self.iterator)


class InorderIterator(Iterator):
    def _iterate(self, cur_node: "TreeInterface.Node"):
        if cur_node.left:
            yield from self._iterate(cur_node.left)

        yield cur_node

        if cur_node.right:
            yield from self._iterate(cur_node.right)


class PreorderIterator(Iterator):
    def _iterate(self, cur_node: "TreeInterface.Node") -> "TreeInterface.Node":
        yield cur_node

        if cur_node.left:
            yield from self._iterate(cur_node.left)

        if cur_node.right:
            yield from self._iterate(cur_node.right)


class PostorderIterator(Iterator):
    def _iterate(self, cur_node: "TreeInterface.Node") -> "TreeInterface.Node":
        if cur_node.left:
            yield from self._iterate(cur_node.left)

        if cur_node.right:
            yield from self._iterate(cur_node.right)

        yield cur_node


class BFSIterator(Iterator):
    def _iterate(self, cur_node: "TreeInterface.Node") -> "TreeInterface.Node":
        if not cur_node:
            cur_node = self.root_node

        queue = deque()
        queue.append(cur_node)

        while queue:
            cur_node = queue.popleft()
            yield cur_node

            if cur_node.left:
                queue.append(cur_node.left)

            if cur_node.right:
                queue.append(cur_node.right)


class TreeInterface(metaclass=ABCMeta):
    class Node:
        def __init__(self, data: int) -> None:
            self.data = data
            self.left = None
            self.right = None

    @abstractmethod
    def create_inorder_iterator(self) -> Iterator:
        pass

    @abstractmethod
    def create_preorder_iterator(self) -> Iterator:
        pass

    @abstractmethod
    def create_postorder_iterator(self) -> Iterator:
        pass

    @abstractmethod
    def create_bfs_iterator(self) -> Iterator:
        pass


class BSTree(TreeInterface):
    def __init__(self) -> None:
        self.root = None

    def _insert(
        self, parent: TreeInterface.Node, node: TreeInterface.Node
    ) -> TreeInterface.Node:
        if not parent:
            return node
        if parent.data > node.data:
            parent.left = self._insert(parent.left, node)
        else:
            parent.right = self._insert(parent.right, node)

        return parent

    def insert(self, data: int) -> None:
        node = BSTree.Node(data)

        if not self.root:
            self.root = node
        else:
            self._insert(self.root, node)

    def create_inorder_iterator(self) -> InorderIterator:
        return InorderIterator(self.root)

    def create_preorder_iterator(self) -> PreorderIterator:
        return PreorderIterator(self.root)

    def create_postorder_iterator(self) -> PostorderIterator:
        return PostorderIterator(self.root)

    def create_bfs_iterator(self) -> BFSIterator:
        return BFSIterator(self.root)


if __name__ == "__main__":
    tree = BSTree()
    tree.insert(10)
    tree.insert(4)
    tree.insert(2)
    tree.insert(7)
    tree.insert(16)
    tree.insert(12)
    tree.insert(20)

    print("Inorder traversal")
    iterator = tree.create_inorder_iterator()

    try:
        while item := iterator.next():
            print(item.data, end=" ")
    except StopIteration:
        print()

    print("Preorder traversal")
    iterator = tree.create_preorder_iterator()

    try:
        while item := iterator.next():
            print(item.data, end=" ")
    except StopIteration:
        print()

    print("Postorder traversal")
    iterator = tree.create_postorder_iterator()

    try:
        while item := iterator.next():
            print(item.data, end=" ")
    except StopIteration:
        print()

    print("Breadth First traversal")
    iterator = tree.create_bfs_iterator()

    try:
        while item := iterator.next():
            print(item.data, end=" ")
    except StopIteration:
        print()
