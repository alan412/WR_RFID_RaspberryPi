from keyboard_alike import reader
import datetime
import csv
from phant import Phant

p = Phant('yAYZ9aJ98Kiyz4XNm5NW', 'location', 'id', 'name', 'time', private_key='4Wqom46m9niK2k8pzxp4')

def getName(idString):
	try:
		person[idString]['isHere'] = person[idString]['isHere'] == False
		return person[idString]['name']
	except:
		return 'Unknown'

def logAccess(id, name):
  time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
  #p.log("Hopewell", id, name, time)
  f = open('/home/pi/rfid/access_log.txt','a')
  f.write("{idStr},{nameStr},{datetime}\n".format(idStr=id,nameStr=name,datetime=time))
  f.close()

person = {}

with open('/home/pi/rfid/web/users.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:
		person[row[0]] = {'rfid': row[0], 'name': row[1], 'isHere': row[2] == 'True'}

reader = reader.Reader(0x08ff, 0x0009, 84, 16, should_reset=False) # From the documentation - the VID and DEVID

reader.initialize()

while(1):
   card = reader.read().strip()    # get the card number
   name = getName(card);
   print('\n' + name);
   print(person);
   f = open('/home/pi/rfid/web/message.txt', 'w')
   f.write("Hi {name}".format(name=name))
   f.close()
   logAccess(card, name)

reader.disconnect()
