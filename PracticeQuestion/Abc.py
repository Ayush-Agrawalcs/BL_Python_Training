from abc import ABC,abstractmethod

class remote(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def change_channel(self,st):
        pass

class channel(remote):
    def __init__(self):
        super().__init__()
    
    def change_channel(self,st):
        if st=='1':
            print("CN")
        elif st=='2':
            print("Discovery Land")
        elif st=='3':
            print("sony sab")

re=channel()
while True:
    s=input("Enter the name")
    re.change_channel(s)





