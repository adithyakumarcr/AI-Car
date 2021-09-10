# Create a folder for sh files
FOLDER=/usr/local/sbin/computer
if [ -d "$FOLDER" ]; then
    echo "$FOLDER exists"
else
    sudo mkdir $FOLDER
fi

# copy sh files
sudo cp ./start_csi.sh /usr/local/sbin/computer/start_csi.sh

# +x for sh files
sudo chmod +x /usr/local/sbin/computer/start_csi.sh

# copy service files to systemd
sudo cp ./csi.service /etc/systemd/system/csi.service

# reload service daemon
sudo systemctl daemon-reload

# Start the service
# sudo systemctl start csi.service

# Enable the service during startup
sudo systemctl enable csi.service
