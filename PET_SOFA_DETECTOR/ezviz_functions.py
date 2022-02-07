import yagmail
from config import *

def launch_alarm(detections): 
    
    lista = [pet, "couch"]
    
    if(all(x in [x["name"] for x in detections] for x in lista)):
        print(detections)
        pet_coord = [x["box_points"] for x in detections if x["name"]==lista[0]]
        couch_coord = [x["box_points"] for x in detections if x["name"]==lista[1]]        
        if((couch_coord[0][3] > pet_coord[0][3]) and (couch_coord[0][0] < pet_coord[0][0])and (couch_coord[0][2] > pet_coord[0][2])): #si está por encima el perro del bajo del sofá, es que está subido
            print ("ALARRMM ALAARRMM!!!")
            return True
        else:
            print("Ojo, merodeando")
            return False

def send_mail(path_image):

    user = yagmail.SMTP(user=usermail, \
                           password=passmail)
    user.send(to='tumail@gmail.com', \
         subject='Alerta Mascota en Sofá!', \
         contents= [yagmail.inline(path_image)])