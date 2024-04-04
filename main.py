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

    def markAsIncomplete(self):
        self._completed = False


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

    def deleteTaskByDescription(self,description:str):

        task_to_delete = self.findTaskByDescription(description)

        if task_to_delete:
            if task_to_delete is self._head:
                self.removeHead()
            elif task_to_delete is self._tail:
                self.pop()
            else:
                prev_task = task_to_delete.getPrev()
                next_task = task_to_delete.getNext()
                prev_task.setNext(next_task)
                next_task.setPrev(prev_task)
                task_to_delete.setPrev(None)
                task_to_delete.setNext(None)
                return task_to_delete
            
        else:
            print( 'task not found!')
    
    def removeDuplicates(self):

        if self.isEmpty():
            return None
        
        seen_tasks = set()
        current = self._head
        while current:
            description = current.getDescription()
            if description in seen_tasks:
                next_task = current.getNext()
                self.deleteTaskByDescription(description)
                current = next_task
            else:
                seen_tasks.add(description)
                current = current.getNext()

    def __countTasksR(self, task: Task, count=0):
        if not task:
            return count
        return self.__countTasksR(task.getNext(), count + 1)

    def countTasks(self):
        return self.__countTasksR(self._head)

    def findTaskByDescription(self, description: str) -> Task | None:

        if self.isEmpty():
            return None

        pointer = self._head
        position = 0
        while (pointer.getDescription() != description and pointer.getNext()):
            pointer = pointer.getNext()
            position += 1

        if pointer.getDescription() != description :
            return None
        # return (pointer,position) #it's possible to return a tuple and access the function return by indexing
        return pointer

    def retrieveSearchedTaskData(self,description:str):

        pointer = self.findTaskByDescription(description)
        # position = self.findTaskByDescription(description)[1]
        result = dict(description=pointer.getDescription(),
                        priority=pointer.getPriority(),
                        completed=pointer.getCompleted()) #position=position,
        return result

    def MarkTaskAsComplete(self, description: str):

        if self.findTaskByDescription(description):
            task = self.findTaskByDescription(description)
            task.markAsCompleted()
        return    
        
    def addTaskByPriority(self, description: str, priority: int) -> None:

        task = Task(description, priority)

        if self.isEmpty():
            self._head = task
            self._tail = task
            return

        if priority > self._head.getPriority():
            task.setNext(self._head)
            self._head.setPrev(task)
            self._head = task
            return

        if priority < self._tail.getPriority():
            self._tail.setNext(task)
            task.setPrev(self._tail)
            self._tail = task
            return

        current = self._head
        while current.getNext() and current.getNext().getPriority() >= priority:
            current = current.getNext()

        next_task = current.getNext()
        current.setNext(task)
        task.setPrev(current)
        if next_task:
            next_task.setPrev(task)
        else:
            self._tail = task
        task.setNext(next_task)

    










################################## ^
dll = doublyLinkedList()
# dll.prepend('task1', 1)
# dll.append('task2', 2)
# dll.append('task3', 3)
# dll.prepend('task0', 0)
# dll.append('task4', 4)
# dll.append('task4', 4)
# dll.printDll()
# dll.showHead()
# dll.showTail()
# print(dll.removeHead())
# print(dll.pop())
# print(dll.countTasks())
# print(dll.findTaskByDescription('task2'))
# print(dll.retrieveSearchedTaskData('task2'))
# dll.MarkTaskAsComplete('task3')
# dll.deleteTaskByDescription('task1')
# dll.deleteTaskByDescription('task0')
# dll.deleteTaskByDescription('task2')
# dll.deleteTaskByDescription('task3')
# dll.deleteTaskByDescription('task4')
# dll.deleteTaskByDescription('task0')

dll.addTaskByPriority('task5',1)
dll.addTaskByPriority('task4',2)
dll.addTaskByPriority('task3',3)
dll.addTaskByPriority('task2',4)
dll.addTaskByPriority('task1',5)

dll.removeDuplicates()
dll.printDll()
