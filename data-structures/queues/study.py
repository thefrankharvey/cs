from collections import deque
from typing import List

queue = deque()

def handleQueue(instruction: str) -> List:
    if instruction == "peek":
        # print out the first item in queue if it is not empty
        # print warning message if queue is empty
        print(queue[0]) if queue else print("Queue is empty!")
    elif instruction == "pop":
        # check if queue is empty
        if queue:
            # pop the first item in queue
            queue.popleft()
        else:
            # print message if queue is empty
            print("Queue is empty!")
    elif "add" in instruction[:3]:
        # check if queue is empty
        data = instruction[instruction.find(" ")+1:]
        queue.append(data)

    return queue


print(handleQueue("add yo"))
print(handleQueue("add buddy"))
print(handleQueue("add hey"))
print(handleQueue("peek"))
print(handleQueue("pop"))
print(handleQueue("peek"))