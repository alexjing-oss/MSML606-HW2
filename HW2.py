#NO EXTERNAL SOURCES USED
import csv
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HomeWork2:

    # Problem 1: Construct an expression tree (Binary Tree) from a postfix expression
    # input -> list of strings (e.g., [3,4,+,2,*])
    # this is parsed from p1_construct_tree.csv (check it out for clarification)

    # there are no duplicate numeric values in the input
    # support basic operators: +, -, *, /

    # output -> the root node of the expression tree. Here: [*,+,2,3,4,None,None]
    # Tree Node with * as root node, the tree should be as follows
    #         *
    #        / \
    #       +   2
    #      / \
    #     3   4

    

    def treeString(self, root):

        if root.left:
            return f"{root.val}:({self.treeString(root.left)},{self.treeString(root.right)})"
        else:
            return root.val
        
    def constructBinaryTree(self, input) -> TreeNode:
        #Since Postorder, Last element is the root. If current element is operator, should have two children. If curr is a number, should be a leaf
        input_rev = [x for x in reversed(input)]
        root, lst = self.constructBinaryTree_Aux(input_rev)
        print(lst)
        #Elements left in list -> Error
        if len(lst) != 0:
            print("invalid input")
            return None
        print(self.treeString(root))
        self.prefixNotationPrint(root)
        self.infixNotationPrint(root)
        self.postfixNotationPrint(root)
        return root
    #Recursive helper, returns Current Node and remaining list
    def constructBinaryTree_Aux(self, lst):
        root = TreeNode(lst[0])
        if not root.val.isdigit():
            #Operator doesnt have 2 children
            if len(lst) < 3:
                print("invalid input")
                exit()
            root.right, lst = self.constructBinaryTree_Aux(lst[1::])
            root.left, lst = self.constructBinaryTree_Aux(lst)
            return (root, lst)
        else:
            return(root,lst[1::])



    # Problem 2.1: Use pre-order traversal (root, left, right) to generate prefix notation
    # return an array of elements of a prefix expression
    # expected output for the tree from problem 1 is [*,+,3,4,2]
    # you can see the examples in p2_traversals.csv

    def prefixNotationPrint(self, head: TreeNode) -> list:
        lst = self.prefixNotationPrint_aux(head)
        print(lst)
        return lst


    def prefixNotationPrint_aux(self, curr: TreeNode):
        returnLst = []
        returnLst.append(curr.val)
        #Leaf
        if curr.val.isdigit():
            return returnLst
        #Operator
        else:
            return returnLst + self.prefixNotationPrint_aux(curr.left) + self.prefixNotationPrint_aux(curr.right)
            
        


    # Problem 2.2: Use in-order traversal (left, root, right) for infix notation with appropriate parentheses.
    # return an array of elements of an infix expression
    # expected output for the tree from problem 1 is [(,(,3,+,4,),*,2,)]
    # you can see the examples in p2_traversals.csv

    # don't forget to add parentheses to maintain correct sequence
    # even the outermost expression should be wrapped
    # treat parentheses as individual elements in the returned list (see output)

    #Effectively same as prefix
    def infixNotationPrint(self, head: TreeNode) -> list:
        lst = self.infixNotationPrint_aux(head)
        print(lst)
        return lst
    def infixNotationPrint_aux(self, curr: TreeNode):
        returnLst = []
        returnLst.append(curr.val)
        #Leaf
        if curr.val.isdigit():
            return returnLst
        #Operator
        else:
            return ["("] + self.infixNotationPrint_aux(curr.left) + returnLst +  self.infixNotationPrint_aux(curr.right) + [")"]
            

    # Problem 2.3: Use post-order traversal (left, right, root) to generate postfix notation.
    # return an array of elements of a postfix expression
    # expected output for the tree from problem 1 is [3,4,+,2,*]
    # you can see the examples in p2_traversals.csv

    def postfixNotationPrint(self, head: TreeNode) -> list:
        lst = self.postfixNotationPrint_aux(head)
        print(lst)
        return lst
    def postfixNotationPrint_aux(self, curr: TreeNode):
        returnLst = []
        returnLst.append(curr.val)
        #Leaf
        if curr.val.isdigit():
            return returnLst
        #Operator
        else:
            return self.postfixNotationPrint_aux(curr.left)  +  self.postfixNotationPrint_aux(curr.right) + returnLst
            



class Stack:
    # Implement your stack using either an array or a list
    # (i.e., implement the functions based on the Stack ADT we covered in class)
    # You may use Python's list structure as the underlying storage.
    # While you can use .append() to add elements, please ensure the implementation strictly follows the logic we discussed in class
    # (e.g., manually managing the "top" of the stack
    
    # Use your own stack implementation to solve problem 3

    def __init__(self):
        # TODO: initialize the stack

        self.lst = []

    
    def push(self,val):
        self.lst.append(val)

    def pop(self):
        val = self.lst[-1]
        self.lst = self.lst[0:-1:]
        return val
    def empty(self):
        return len(self.lst) == 0
    def peek(self):
        return self.lst[-1]
    def peek_n(self,n):
        return self.lst[-1:-n-1:-1]
    def size(self):
        return len(self.lst)

    # Problem 3: Write code to evaluate a postfix expression using stack and return the integer value
    # Use stack which you implemented above for this problem

    # input -> a postfix expression string. E.g.: "5 1 2 + 4 * + 3 -"
    # see the examples of test entries in p3_eval_postfix.csv
    # output -> integer value after evaluating the string. Here: 14

    # integers are positive and negative
    # support basic operators: +, -, *, /
    # handle division by zero appropriately

    # DO NOT USE EVAL function for evaluating the expression

    #Keep adding elements until we see two numbers in a row, then evaluate. 
    def evaluatePostfix(self, exp: str) -> int:

        vals = [int(x) if x.isdigit() else x for x in reversed(exp.split(" ")) ]
        print(vals)
        stack = Stack()
        stack.push(vals[0])
        vals = vals[1::]

        #Continue until stack is empty, vals should be empty after looping
        while(not stack.empty()):
            print(stack.lst)
            #One Element and is int
            if stack.size() == 1 and isinstance(stack.peek(),int):
                if len(vals) != 0:
                    print("invalid input")
                    return None
                else:
                    return stack.pop()
            #Stack is Number, Number, Operator
            elif all(isinstance(element, expected_type) for element, expected_type in zip(stack.peek_n(3), [int,int,str])):
                num_1 = stack.pop()
                num_2 = stack.pop()
                operator = stack.pop()
                if operator == "+":
                    stack.push(num_1 + num_2)
                if operator == "-":
                    stack.push(num_1 - num_2)
                if operator == "*":
                    stack.push(num_1 * num_2)
                if operator == "/":
                    if num_2 == 0:
                        raise ZeroDivisionError
                    else:
                        stack.push(num_1 // num_2)


            elif len(vals)>0:
                stack.push(vals[0])
                vals = vals[1::]
            else:
                print("invalid input")
        
            

    





# Main Function. Do not edit the code below
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)

        assert output == postfix, f"P1 Test {i} failed: tree structure incorrect"
        print(f"P1 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    with open('p2_traversals.csv', 'r') as f:
        testcases = list(csv.reader(f))

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)

        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"

        print(f"P2 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 3")
    testcases = []
    try:
        with open('p3_eval_postfix.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                testcases.append(row)
    except FileNotFoundError:
        print("p3_eval_postfix.csv not found")

    for idx, row in enumerate(testcases, start=1):
        expr, expected = row

        try:
            s = Stack()
            result = s.evaluatePostfix(expr)
            if expected == "DIVZERO":
                print(f"Test {idx} failed (expected division by zero)")
            else:
                expected = int(expected)
                assert result == expected, f"Test {idx} failed: {result} != {expected}"
                print(f"Test case {idx} passed")

        except ZeroDivisionError:
            assert expected == "DIVZERO", f"Test {idx} unexpected division by zero"
            print(f"Test case {idx} passed (division by zero handled)")