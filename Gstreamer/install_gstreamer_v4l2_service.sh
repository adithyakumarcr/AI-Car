# Create a folder for sh files
FOLDER=/usr/local/sbin/computer
if [ -d "$FOLDER" ]; then
    echo "$FOLDER exists"
else
    sudo mkdir $FOLDER
fi

# copy sh files
sudo cp ./start_v4l2.sh /usr/local/sbin/computer/start_v4l2.sh

# +x for sh files
sudo chmod +x /usr/local/sbin/computer/start_v4l2.sh

# copy service files to systemd
sudo cp ./webcam.service /etc/systemd/system/webcam.service

# reload service daemon
sudo systemctl daemon-reload

# Start the service
# sudo systemctl start gstseekercamera.service

# Enable the service during startup
sudo systemctl enable webcam.service
