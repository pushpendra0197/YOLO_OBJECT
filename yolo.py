import numpy as np
import pandas as pd
import cv2
from ultralytics import YOLO
import streamlit as st
model=YOLO(r"C:\Users\KINGNICKS-DELL\Downloads\yolov5nu.pt")
st.title("Object Detection by YOLO")
button=st.button("click for camera")
button2=st.button("close camera")
frame_window=st.image([])
detected_objects = []
cam=cv2.VideoCapture(0)
if button:
  while True:
    ret,frame=cam.read()
    frame=cv2.flip(frame,1)
    frame = cv2.resize(frame, (640, 480)) 
    results=model.track(frame,persist=True)
    frame_=results[0].plot()
    Frame=cv2.cvtColor(frame_,cv2.COLOR_BGR2RGB)
    frame_window.image(Frame)
if button2:
  cam.release()









 