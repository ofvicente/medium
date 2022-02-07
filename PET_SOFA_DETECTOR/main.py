import cv2
import time
import matplotlib.pyplot as plt
from IPython.display import clear_output
from imageai.Detection import ObjectDetection
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import shutil
from datetime import datetime
from ezviz_functions import *
from config import *

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path +"/models/" , "yolo.h5"))
detector.loadModel()


def main():

    video_reader = cv2.VideoCapture(cam_url)    
    count = 0 
    en_sofa = False

    while True:

        #try:

            t = time.localtime(time.time())
            success, frame = video_reader.read() 

            if(success and t.tm_sec%DELAY_SECONDS==0):          
                
                detections = detector.detectObjectsFromImage(input_image=frame, input_type="stream", output_image_path=os.path.join(execution_path , file_image))

                if(launch_alarm(detections)):  

                    if(not en_sofa):
                    
                        now = datetime.now()
                        dt_string = now.strftime("%d_%m_%Y %H_%M_%S")
                        en_sofa = True
                        count += 1
                        send_mail(os.path.join(execution_path , file_image))
                        shutil.copyfile(os.path.join(execution_path , file_image), execution_path +"/detections/captura_"+str(dt_string)+".jpg")

                else: #rearmamos la alarma cuando se baja del sofá para no mandar infinitas alarmas consecutivas
                    en_sofa = False  

            elif(not success) :
                video_reader = cv2.VideoCapture(cam_url) #reiniciamos por estabilidad
        
        #except: pass


if __name__ == "__main__":
    main()