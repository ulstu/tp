from functools import reduce
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def math_eval(tree):
    if not isinstance(tree, list):
        return tree
    op = ops[tree.pop(0)]
    return reduce(op, map(math_eval, tree))

if __name__ == '__main__':
	print(math_eval(["+", ["*", 4, 5], 5]))