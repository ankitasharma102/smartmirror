python3 /home/pi/smartmirror/server.py &
sleep 5
chromium-browser --kiosk http://0.0.0.0:5000
