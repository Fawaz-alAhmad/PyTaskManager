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

    def prepend(self,description: str, priority:int):

        if self._head is None:
            new_task = Task(description, priority)
            self._head = new_task
            self._tail = new_task
        else:
            new_task = Task(description, priority)
            new_task.setNext(self._head)
            self._head.setPrev(new_task)
            self._head = new_task

    def showHead(self):
        print(self._head._description)
    
    def showTail(self):
        print(self._tail._description)

    def printDll(self):
        current= self._head
        while current:
            print(f"description: {current._description}, priority: {current._priority}, isCompleted: {current._completed}")
            current = current.getNext()

    def pop(self):

        if self.isEmpty():
            return None
        elif self._head is self._tail:
            self._head = self._tail = None
        else:
            before_last = self._tail.getPrev()
            before_last.setNext(None)
            self._tail.setPrev(None)
            task = dict(description=self._tail.getDescription(),priority=self._tail.getPriority(),completed=self._tail.getCompleted())
            self._tail = before_last
            return task

    def removeHead(self):
        pass



ddl = doublyLinkedList()
ddl.append('task1',4)
ddl.append('task2',5)
ddl.append('task1',4)
ddl.append('task3',6)
ddl.prepend('task0',3)
ddl.append('task4',7)
ddl.printDll()
ddl.showHead()
ddl.showTail()
print(ddl.pop())
ddl.printDll()