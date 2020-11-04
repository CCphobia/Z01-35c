from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator

def buildParseTree(expression):
    expression_list = expression.split()
    stack = Stack()
    Tree = BinaryTree('')
    stack.push(Tree)
    currentTree = Tree

    for i in expression_list:
        if i == '(':
            currentTree.insertLeft('')
            stack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            stack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = stack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(float(i))
                parent = stack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return Tree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

equation = input("Enter equation, remember about brackets:\n")
pt = buildParseTree(equation)
pt.inorder()
print(evaluate(pt))
