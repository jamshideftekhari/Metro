from Line import Line 
class Metro(object):
    MetroLines=[]
    def __init__(self):
        M3 = Line("M3", "Red")
        self.MetroLines.append(M3)

    def GetMetroLines(self):
        return self.MetroLines

    def GetMetroLine(self,name):
        if name == "M3":
            value = self.MetroLines[0]
        return value

