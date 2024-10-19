# narrowing.py
from typing import TypeGuard, TypeIs

type Tree = list[Tree | int]

def is_tree_312(obj: object) -> TypeGuard[Tree]:
    return isinstance(obj, list)

def get_left_leaf_value_312(tree_or_leaf: Tree | int) -> int:
    if is_tree_312(tree_or_leaf):
        return get_left_leaf_value_312(tree_or_leaf[0])

    return tree_or_leaf # With TypeGuard: tree_or_leaf is still Tree | int

def is_tree(obj: object) -> TypeIs[Tree]:
    return isinstance(obj, list)

def get_left_leaf_value(tree_or_leaf: Tree | int) -> int:
    if is_tree(tree_or_leaf):
        return get_left_leaf_value(tree_or_leaf[0])

    return tree_or_leaf

print(get_left_leaf_value([[[[3, 13], 12], 11], 10]))
