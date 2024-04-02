class Task:

    __current_id = 0

    def __init__(self, description, priority):
        Task.__current_id += 1

        self._task_id: int = Task.__current_id
        self._description: str = description
        self._priority: int = priority
        self._completed: bool = False
        self._next: Task | None = None
        self._prev: Task | None = None

    def getDescription(self):
        return self._description

    def getId(self):
        return self._task_id

    def getPriority(self):
        return self._priority

    def getCompleted(self):
        return self._completed

    def getNext(self):
        return self._next

    def getPrev(self):
        return self._prev

    def setNext(self, task):
        self._next = task

    def setPrev(self, task):
        self._prev = task

    def markAsCompleted(self):
        self._completed = True


class doublyLinkedList:

    def __init__(self):

        self._head: Task | None = None
        self._tail: Task | None = None

    def isEmpty(self):
        return self._head == None

    def showHead(self):
        if self._head:
            print(self._head._description)
        else:
            print('empty')

    def showTail(self):
        if self._tail:
            print(self._tail._description)
        else:
            print('empty')

    def printDll(self):
        current = self._head
        while current:
            print(f"description: {current.getDescription()}, priority: {current.getPriority(
            )}, id: {current.getId()} ,isCompleted: {current.getCompleted()}")
            current = current.getNext()

    def append(self, description: str, priority: int):

        if self._head is None:
            new_task = Task(description, priority)
            self._head = new_task
            self._tail = new_task
        else:
            new_task = Task(description, priority)
            self._tail.setNext(new_task)
            new_task.setPrev(self._tail)
            self._tail = new_task

    def prepend(self, description: str, priority: int):

        if self._head is None:
            new_task = Task(description, priority)
            self._head = new_task
            self._tail = new_task
        else:
            new_task = Task(description, priority)
            new_task.setNext(self._head)
            self._head.setPrev(new_task)
            self._head = new_task

    def pop(self):

        if self.isEmpty():
            return None
        elif self._head is self._tail:
            task = dict(id=self._tail.getId(),
                        description=self._tail.getDescription(),
                        priority=self._tail.getPriority(),
                        completed=self._tail.getCompleted())
            self._head = self._tail = None
            return task
        else:
            before_last = self._tail.getPrev()
            before_last.setNext(None)
            self._tail.setPrev(None)
            task = dict(id=self._tail.getId(),
                        description=self._tail.getDescription(),
                        priority=self._tail.getPriority(),
                        completed=self._tail.getCompleted())
            self._tail = before_last
            return task

    def removeHead(self):
        if self.isEmpty():
            return None
        elif self._head is self._tail:
            task = dict(id=self._head.getId(),
                        description=self._head.getDescription(),
                        priority=self._head.getPriority(),
                        completed=self._head.getCompleted())
            self._head = self._tail = None
            return task
        else:
            second = self._head.getNext()
            self._head.setNext(None)
            second.setPrev(None)
            task = dict(id=self._head.getId(),
                        description=self._head.getDescription(),
                        priority=self._head.getPriority(),
                        completed=self._head.getCompleted())
            self._head = second
            return task

    def __countTasksR(self, task: Task, count=0):
        if not task:
            return count
        return self.__countTasksR(task.getNext(), count + 1)

    def countTasks(self):
        return self.__countTasksR(self._head)

    def findTaskById(self, id: int):

        if self.isEmpty():
            return -1

        pointer = self._head
        position = 0
        while (pointer.getId() != id and pointer.getNext()):
            pointer = pointer.getNext()
            position += 1

        if pointer.getId() != id :
            return -1
        result = dict(position=position,
                        description=pointer.getDescription(),
                        priority=pointer.getPriority(),
                        completed=pointer.getCompleted())
        return result
# ^
dll = doublyLinkedList()
dll.prepend('task1', 1)
dll.append('task2', 2)
dll.append('task3', 3)
dll.prepend('task0', 0)
dll.append('task4', 4)
dll.printDll()
# dll.showHead()
# dll.showTail()
# print(dll.removeHead())
# print(dll.pop())
# dll.printDll()
print(dll.countTasks())
print(dll.findTaskById(4))
