from CPHMetro import Metro

class Trip(object):
    MyTrip = []
    def __init__(self, name):
        self.Name=name
        self.MetroLines = Metro()

    def PrintLineNames(self):
        for line in self.MetroLines.GetMetroLines():
            print(line.Name)

    def PrintStationsInfo(self, linename):
        for ln in self.MetroLines.GetMetroLines():
            for st in ln.GetStationsList():
                print (st.Name)

                
