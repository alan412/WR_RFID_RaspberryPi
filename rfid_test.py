from keyboard_alike import reader
import datetime
from phant import Phant

tags = {'0009909662' : 'Philip Smith',
        '0004406858' : 'Joshua Smith',
        '0009909876' : 'Abigail Smith',
        '0003567797' : 'Linda Whipker'}
p = Phant('yAYZ9aJ98Kiyz4XNm5NW', 'location', 'id', 'name', 'time', private_key='4Wqom46m9niK2k8pzxp4')

def getName(idString):
	with open('/home/pi/rfid/web/users.txt', 'r') as file:
		for line in file:
			row = line.split(', ');
			if (row[0] == idString):
				return row[1];
	return 'Unknown'
		
	

def logAccess(id):
  name = getName(id)
  time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
  p.log("Hopewell", id, name, time)
  f = open('/home/pi/rfid/access_log.txt','a')
  f.write("{idStr},{nameStr},{datetime}\n".format(idStr=id,nameStr=name,datetime=time))
  f.close()

reader = reader.Reader(0x08ff, 0x0009, 84, 16, should_reset=False) # From the documentation - the VID and DEVID

reader.initialize()

while(1):
   card = reader.read().strip()    # get the card number
   f = open('/home/pi/rfid/web/message.txt', 'w')
   f.write("Hi {name}".format(name=getName(card))) 
   f.close()
   logAccess(card)

reader.disconnect()
