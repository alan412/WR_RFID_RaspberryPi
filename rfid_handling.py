from keyboard_alike import reader
import datetime
import csv
from phant import Phant

class members(object):
    def __init__(self, filename):
        self.students = {}
        self.readFile(filename)
        
    def readFile(self, filename):
        self.students = {}
        with open(filename, 'r') as csvfile:
     	    csvreader = csv.reader(csvfile, delimiter=',')
     	    for row in csvreader:
     		    self.students[row[0]] = {'rfid': row[0], 'name': row[1], 'isHere': False}

    def getGreeting(self, idString):
        if idString in self.students:
            name = self.students[idString]['name']
            if(self.students[idString]['isHere']):
                return "Hi, " + name;
            else:
                return "Bye, " + name;
        else:
            return "Unknown: " + idString
            
    def getName(self, idString):
        if idString in self.students:
            return self.students[idString]['name']
        else:
    		return 'Unknown'

    def toggleHere(self, idString):
        if idString in self.students: 
            self.students[idString]['isHere'] = (self.students[idString]['isHere'] == False)   # Toggle
            
    def writePresent(self, filename):
        any = False;
        f = open(filename, 'w');
        for id in self.students:
            if(self.students[id]['isHere']):
                if(any):
                    f.write(", ");
                f.write(self.students[id]['name']);
                any = True;
        if(any == False):
            f.write("None");
        f.close()
        
class RFIDHandling(object):
    def __init__(self, fileBase = "/home/pi/rfid/web/", location = "Hopewell"):
        self.reader = reader.Reader(0x08ff, 0x0009, 84, 16, should_reset=False) # From the documentation - the VID and DEVID
        self.reader.initialize();
        self.location = location;
        self.fileBase = fileBase;
        self.members = members(self.fileBase + "users.csv")
        #self.p = Phant('yAYZ9aJ98Kiyz4XNm5NW', 'location', 'id', 'name', 'time', private_key='4Wqom46m9niK2k8pzxp4')
        
    def logAccess(self, id, name):
        time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        #self.p.log(location, id, name, time)
        f = open(self.fileBase + "logaccess.csv",'a')
        f.write("{idStr},{nameStr},{datetime}\n".format(idStr=id,nameStr=name,datetime=time))
        f.close()
    def blockingRead(self):
        card = self.reader.read().strip()    # get the card number
        self.members.toggleHere(card);
        self.logAccess(card, self.members.getName(card));
        self.members.writePresent(self.fileBase + "users.txt")
        return self.members.getGreeting(card);
    def close(self):
        self.reader.disconnect()
        

if __name__ == '__main__':
    rfid = RFIDHandling()
    while(1):
        print rfid.blockingRead();
    rfid.close()
    