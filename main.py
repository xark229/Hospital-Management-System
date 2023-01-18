import DBMS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


print("------------------------Hospital Management-----------------------")

print("a) Add Bed")
print("b) Add paitent")
print("c) Upload Prescription")
print("d) Update Paitent Details")
print("e) Search paitent ")
print("f) Search paitents Treated by Doctor")
print("g) Download paitent prescription")
print("h) Discharge Paitent")
print("i) Exit")

while True:
    a=input("Enter choices ")
    if a=='a':
        n=int(input("Enter number of beds"))
        DBMS.addBed(n)
    elif a=='b':
        DBMS.add_details()
    elif a=='c':
        folder=input("Enter Folder Path")
        DBMS.uploadPrescription(folder)
    elif a=='d':
        key=input("Enter Patient Id")
        DBMS.update(key)
    elif a=='e':
        key=str(input("Enter Patient Id"))
        DBMS.get_details(key)
    elif a=='f':
        doc=input("Enter the Doctors name")
        DBMS.get_engaged_doctor(doc)
    elif a=='g':
        key=str(input("Enter Patient Id"))
        DBMS.downloadPres(key)
    elif a=='h':
        key=str(input("Enter Patient Id"))
        DBMS.discharge(key)
    elif a=='i':
        print("Thank you...")
        exit(0)
    else:
        print("UnKown Choice ")
        print("Please try again" )


