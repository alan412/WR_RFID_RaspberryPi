from keyboard_alike import reader

reader = reader.Reader(0x08ff, 0x0009, 84, 16, should_reset=False) # From the documentation - the VID and DEVID

reader.initialize()

tags = {'0009909662' : 'Philip Smith',
        '0004406858' : 'Joshua Smith',
        '0009909876' : 'Abigail Smith',
        '0004304910' : 'Dad'}

while(1):
   card = reader.read().strip()    # get the card number
   print "Hi %s! RFID card: %s" % (tags[card],card)

reader.disconnect()
