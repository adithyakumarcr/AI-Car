#!/bin/sh
# Start the gstreamer
gst-launch-1.0 -v v4l2src device=/dev/video1 ! 'video/x-raw,width=1280,height=720' ! nvvidconv ! "video/x-raw(memory:NVMM),width=852,height=480,format=(string)I420" ! omxh264enc profile=8 control_rate=2 insert-sps-pps=1 iframeinterval=2 ! 'video/x-h264,stream-format=avc,bitrate=400000' ! rtph264pay ! 'application/x-rtp,payload=96' ! udpsink host=192.168.10.2 port=8554 async=false
