class Task:

    __current_id= 0

    def __init__(self,description,priority):
        Task.__current_id += 1

        self._task_id: int = Task.__current_id
        self._description : str = description
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
    
    def setNext(self,task):
        self._next = task
    
    def setPrev(self,task):
        self._prev = task

    def markAsCompleted(self):
        self._completed = True        
    