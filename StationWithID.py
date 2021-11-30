class StationWithId(object):
    def __init__(self,id,name, desc,fakta):
        self.Id=id
        self.Name=name
        self.Description=desc
        self.Fakta=fakta
    def GetStationName(self):
        return self.Name
    def ToString(self):
        return "ID: "+ str(self.Id) + " Name: " +self.Name + "\r\n Description: " + self.Description + "\r\n Fakta: " + self.Fakta + "\r\n "