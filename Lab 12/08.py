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


# Write a function called balanced_brackets(text) which takes a string as a parameter, and returns a boolean. The function checks that any parentheses or angled brackets in the string, that is: '(', '<', ' )' and '>', are correctly balanced. The function should return True if the parameter string is balanced, and False otherwise.
def balanced_brackets(text):
    """
 Checks if the parentheses and angled brackets in a string are balanced.

 Args:
   text: The string to check.

 Returns:
   True if the parentheses and angled brackets in the string are balanced, and False otherwise.
 """

    # Create a stack to store the opening brackets.
    stack = Stack()

    # Iterate over the characters in the string.
    for char in text:
        # If the character is an opening bracket, push it onto the stack.
        if char in "([{<":
            stack.push(char)

        # If the character is a closing bracket, pop the top element from the stack and compare it to the closing bracket.
        elif char in ")]}>":
            if stack.is_empty():
                return False
            if char == ")" and stack.peek() != "(":
                return False
            if char == "]" and stack.peek() != "[":
                return False
            if char == "}" and stack.peek() != "{":
                return False
            if char == ">" and stack.peek() != "<":
                return False
            stack.pop()

    # If the stack is empty, then all of the brackets are balanced.
    return stack.is_empty()


print(balanced_brackets('(<x>)(())()'))
print(balanced_brackets('x(y)z'))
print(balanced_brackets('(<x)>(())()'))
print(balanced_brackets('x<y)(>z'))