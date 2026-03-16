class Task:
    def __init__(self,task):
        self.task=task

class TaskManager:
    def __init__(self):
        self.list=[]
    def add_task(self,task):
        if task not in self.list:
            self.list.append(task.task)
        else:
            print("task is already in list")
    
    def remove_task(self,task):
        if task in self.list:
            self.list.remove(task)
        else:
            print("task is already in list")
    
    def update_task(self,task,tas):
        if task in self.list:
            ind=self.list.index(task)
            self.list[ind]=tas
        else:
            print("Update the task")
    
    def display(self):
        for t in self.list:
            print(t)

tas=TaskManager()
while(True):
    print("1. Add new Task")
    print("2. Remove_task")
    print("3. Update task")
    print("4. display")
    choice=int(input("Enter the value"))
    if choice==1:
        task=input("Enter the task")
        ta=Task(task)
        tas.add_task(ta)
    elif choice==2:
        ta=input("Enter the task")
        tas.remove_task(ta)
    elif choice==3:
         ta=input("Enter the task")
         tasl=input("Enter tyhe input")
         tas.update_task(ta,tasl)
    elif choice==4:
        tas.display()
    

    