# Delay to give a chance to get out
echo "Will start in 2 seconds"
sleep 2
python rfid_webapp.py &
xinit ./fullscreen
