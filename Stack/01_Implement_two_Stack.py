class TwoStacks:
    def __init__(self, n):
        """
        Initialize two stacks in an array of size n.
        """
        self.size = n
        self.arr = [None] * n  # Shared array for both stacks
        self.top1 = -1  # Top for Stack 1 (starts from left)
        self.top2 = n  # Top for Stack 2 (starts from right)

    def push1(self, x):
        """
        Pushes x to Stack 1.
        """
        if self.top1 + 1 < self.top2:  # Check space availability
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow for Stack 1")

    def push2(self, x):
        """
        Pushes x to Stack 2.
        """
        if self.top1 + 1 < self.top2:  # Check space availability
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow for Stack 2")

    def pop1(self):
        """
        Pops an element from Stack 1.
        """
        if self.top1 >= 0:
            popped_element = self.arr[self.top1]
            self.top1 -= 1
            return popped_element
        else:
            print("Stack Underflow for Stack 1")
            return None

    def pop2(self):
        """
        Pops an element from Stack 2.
        """
        if self.top2 < self.size:
            popped_element = self.arr[self.top2]
            self.top2 += 1
            return popped_element
        else:
            print("Stack Underflow for Stack 2")
            return None

# Example Usage
stacks = TwoStacks(10)
stacks.push1(1)
stacks.push1(2)
stacks.push1(3)
stacks.push2(10)
stacks.push2(9)
stacks.push2(8)

print(stacks.pop1())  # Output: 3
print(stacks.pop2())  # Output: 8
print(stacks.pop1())  # Output: 2
print(stacks.pop2())  # Output: 9
