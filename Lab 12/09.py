import copy
import types


class Stack:
    def __str__(self):
        return "Stack: " + str(self.__items)

    def __len__(self):
        return len(self.__items)

    def clear(self):
        self.__items = []

    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.__items:
            raise IndexError("ERROR: The stack is empty!")
        return self.__items.pop()

    def peek(self):
        if not self.__items:
            raise IndexError("ERROR: The stack is empty!")
        return self.__items[len(self.__items) - 1]

    def push_list(self, a_list):
        self.__items.extend(a_list)

    def multi_pop(self, number):
        if self.__len__() < number:
            return False
        else:
            for i in range(number):
                self.pop()
            return True

    def copy(self):
        new_items = copy.deepcopy(self.__items)
        new_stack = Stack()
        new_stack.push_list(new_items)
        return new_stack

    def __eq__(self, other):
        if not isinstance(other, Stack):
            return False
        elif self.__len__() != other.__len__():
            return False
        else:
            for i in range(self.__len__()):
                if self.__items[i] != other.__items[i]:
                    return False
            return True

def compute(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 // number2


# A dictionary mapping each operator symbol to its corresponding arity
OPERATOR_ARITY = {
    '+': 2,
    '-': 2,
    '*': 2,
    '/': 2,
    '%': 2,
    '^': 2
}

# A dictionary mapping each operator symbol to its corresponding precedence level
PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '%': 2,
    '^': 3
}


def evaluate_postfix(postfix_list):
    stack = Stack()
    for token in postfix_list:
        if token.isdigit():
            stack.push(int(token))
        elif token == '^':
            top2 = stack.pop()
            top1 = stack.pop()
            stack.push(top1 ** top2)
        elif token == '%':
            top2 = stack.pop()
            top1 = stack.pop()
            stack.push(top1 % top2)
        else:  # +, -, *, /
            top2 = stack.pop()
            top1 = stack.pop()
            if token == '+':
                stack.push(top1 + top2)
            elif token == '-':
                stack.push(top1 - top2)
            elif token == '*':
                stack.push(top1 * top2)
            elif token == '/':
                stack.push(top1 // top2)
            else:
                raise ValueError('Invalid operator:', token)

    return stack.pop()

print(evaluate_postfix(['2', '4', '3', '*', '^']))
