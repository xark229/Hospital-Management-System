import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import datetime
import numpy as np
import cv2

cred = credentials.Certificate("hospital-management-firebase.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://hospital-management-781ec-default-rtdb.firebaseio.com/",
    'storageBucket': "hospital-management-781ec.appspot.com"
})

ref = db.reference('Paitent')
bed = db.reference('Bed')
dis =db.reference('Discharge')



def add_details():
    data={}
    c=countActive()+countInActive()
    while True:
        id=str(3456*10+c)
        name=input("Enter paitent name")
        date_of_admission=datetime.date.today()
        desease=input("enter deisease ")
        dr=input("Enter doctor appointed")
        b = bed.get()
        for i in range(len(b)):
            if b[i] == "Empty":
                bed_ind=i
                bed.child(str(i)).set("Full")
                break
        myDict={"Name":name,"desease":desease,"date_of_admission":str(date_of_admission),"Doctor_Engaged":dr,"bed":bed_ind}
        temp={id:myDict}
        a=input("DO YOU Want to save Y/N")
        if a=='y' or a=='Y':
            ref.child(id).set(myDict)
        else:
            pass
        d=input("DO YOU WANT TO ADD MORE Y/N")
        if d=='n' or d=='N':
            break
        else:
            pass
        c=c+1

def addBed():
    for i in range(10):
        bed.child(str(i)).set("Empty")


def update(k):
    dict = ref.child(k).get()
    for dic, val in dict.items():
        print(dic, ": ", val)
    cat=input("Select key to be updated")
    val=input("Enter new value")
    ref.child(k).child(cat).set(val)

def discharge(k):
    bd=ref.child(k).get()
    bed.child(bd['bed']).set("Empty")
    day_dis=datetime.date.today()
    dod={"date_of_discahrge":str(day_dis),"days_stayed":(datetime.date.fromisoformat(bd['date_of_admission'])-datetime.date.today()).days}
    bd.update(dod)
    dis.child(k).set(bd)
    ref.child(k).delete()


def countActive():
    pat=ref.get()
    return len(pat)
def countInActive():
    d=dis.get()
    return len(d)

def uploadPrescription(folderPath):
    pathList=os.listdir(folderPath)
    for path in pathList:
        fileName = f'{folderPath}/{path}'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)

def downloadPres(k):
    bucket = storage.bucket()
    blob = bucket.get_blob(f'Prescription/{k}.jpg')
    array = np.frombuffer(blob.download_as_string(), np.uint8)
    imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
    cv2.imshow("pres",imgStudent)
    cv2.waitKey(0)

def get_details(k):
    dat=ref.child(str(k)).get()
    for key,val in dat.items():
        print(key," :",val)

def get_engaged_doctor(doctor):
    datr = ref.get()
    for key, val in datr.items():
        if val['Doctor_Engaged']==doctor:
            print (key," ",val['Name'])



