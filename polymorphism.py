from abc import ABC, abstractclassmethod

class UIControl(ABC):
    
    @abstractclassmethod
    def draw(self):
        pass

class DropDownList(UIControl):
    
    def draw(self):
        print("DropDownList")
        
class TextBox(UIControl):
    
    def draw(self):
        print("Textbox")        
        
        
def draw(controls):
    for control in controls:
        control.draw()     

ddl = DropDownList()        
textbox = TextBox()

draw([ddl, textbox])