from abc import ABC, abstractclassmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    
    def __init__(self):
        self.opened = False
    
    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")    
        self.opened = True
        
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")  
        self.opened = False  
    
    @abstractclassmethod 
    def read(self):
        pass    
        
class FileStream(Stream):
    def read(self):
        print("reading from a file.")    
            
class NetworkStream(Stream):
    def read(self):
        print("reading from a network.")        
        
        
stream = FileStream()        