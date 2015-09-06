from keyboard_alike import reader
import datetime
import csv
from phant import Phant

p = Phant('yAYZ9aJ98Kiyz4XNm5NW', 'location', 'id', 'name', 'time', private_key='4Wqom46m9niK2k8pzxp4')

def getName(idString, students):
	try:
		students[idString]['isHere'] = students[idString]['isHere'] == False
		return students[idString]['name']
	except:
		return 'Unknown'

def logAccess(id, name):
  time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
  #p.log("Hopewell", id, name, time)
  f = open('/home/pi/rfid/access_log.txt','a')
  f.write("{idStr},{nameStr},{datetime}\n".format(idStr=id,nameStr=name,datetime=time))
  f.close()


def readFile(fileName):
   person = {}
   with open(fileName, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:
		person[row[0]] = {'rfid': row[0], 'name': row[1], 'isHere': row[2] == 'True'}
   return person;

def writePresent(students):
   any = False;
   f = open('/home/pi/rfid/web/users.txt', 'w');
   for id in students:
      if(students[id]['isHere']):
         if(any):
           f.write(", ");
         f.write(students[id]['name']);
         any = True;
   if(any == False):
      f.write("None");
   f.close()

def writeMessage(id, students):
   f = open('/home/pi/rfid/web/message.txt','w'); 
   if id in students:
      if(students[id]['isHere']):
        f.write("Hi, ");
      else:
        f.write("Bye, ");
      f.write(students[id]['name']);
   else:
      print("Unknown: " + id);
      f.write("Unknown: " + id); 
   f.close()

reader = reader.Reader(0x08ff, 0x0009, 84, 16, should_reset=False) # From the documentation - the VID and DEVID

reader.initialize()
students = readFile("/home/pi/rfid/web/users.csv");
while(1):
   card = reader.read().strip()    # get the card number
   name = getName(card, students);
   print('\n' + name);
   print(students);
   writeMessage(card, students); 
   logAccess(card, name)
   writePresent(students);

reader.disconnect()
