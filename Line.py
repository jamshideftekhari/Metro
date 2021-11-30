from Station import Station
import MetroData

class Line(object):
    LineStations=[]
    def __init__(self, name, color):
        self.Name=name
        self.Color=color
        self.Stations = MetroData.GetStations(name)
        for st in self.Stations:
            self.LineStations.append(Station(st["navn"], st["beskrivelse"], st["fakta"]))
        #self.M3 = {
        #          "S1" : Station("Fredriksberg","Fredriksberg Alle"),
        #          "S2" : Station("AMH","Aksel Møllers Have"),
        #          "S3" : Station("NP","Nuuks Plads")
        #          }
    
    def GetStations(self):
        #s1 = Station("Fredriksberg","Fredriksberg Alle")
        #M3.append(s1)
        return self.Stations

    def GetStationsList(self):
        return self.LineStations

    def PrintM3_obsolite(self):
        for st in self.M3:
            print(self.M3[st].Name + " "+self.M3[st].Address)
        #print(self.M3["S1"].Name + " "+self.M3["S1"].Address)
        

