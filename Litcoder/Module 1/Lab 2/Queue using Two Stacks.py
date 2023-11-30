class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue operation
        self.stack2 = []  # For dequeue operation

    def enqueue(self, x):
        # Push all elements from stack2 to stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        # Push the new element to stack1
        self.stack1.append(x)

    def dequeue(self):
        # If both stacks are empty, the queue is empty
        if not self.stack1 and not self.stack2:
            return None

        # Push all elements from stack1 to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # Pop and return the front element from stack2
        return self.stack2.pop()

    def print_front(self):
        # If both stacks are empty, the queue is empty
        if not self.stack1 and not self.stack2:
            return None

        # Push all elements from stack1 to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # Return the front element without removing it
        return self.stack2[-1]


# Exercise-1
input_1 = input()
commands_1 = input_1.split(',')
queue_1 = QueueUsingTwoStacks()
for command in commands_1:
    if command.startswith("1"):
        _, x = command.split()
        queue_1.enqueue(int(x))
    elif command == "2":
        queue_1.dequeue()
    elif command == "3":
        result = queue_1.print_front()
        if result is not None:
            print(result)