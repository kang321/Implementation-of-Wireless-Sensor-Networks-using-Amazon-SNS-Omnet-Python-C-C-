from datetime import datetime
from multiprocessing.connection import wait
import cv2
import face_recognition
import boto3
import time
client = boto3.client(
        "sns",
        aws_access_key_id="AKIA4RQ3GJPEXOIOF4FF",
        aws_secret_access_key="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",
        region_name="ca-central-1"
    )

    # datetime object containing current date and time
now = datetime.now()
    # dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
def smoke_sensor():
    # Smoke Sensor -> Ideal LEL value is less than 20
    smoke_s1 = int(input('LEL value from Controller 1: '))
    smoke_s2 = int(input('LEL value from Controller 2: '))
    smoke_s3 = int(input('LEL value from Controller 3: '))

    if (smoke_s1>= 20 & smoke_s2 >=20) | (smoke_s2>= 20 & smoke_s3 >=20) | (smoke_s3>= 20 & smoke_s1 >=20) :
        print('Warning: Smoke Detected')
        ### need to write AWS code
        msg = dt_string +'\n'+ "Warning! Smoke Limit Exceeded in your house " 
        client.publish(
        PhoneNumber="+12269788073",
        Message= msg
        )
        time.sleep(1)
    else:
        print('No Smoke detected in the area!')
        time.sleep(1)
def temp_sensor():
    temp_s1 = int(input('Temperature value from the sensor: '))
    if(temp_s1 > 25):
        print('Warning: Too hot, turning on the AC')
        ### need to write AWS code
        msg = dt_string +'\n'+ "Warning! House is too hot, Please turn on the Air Conditioner switch" 
        client.publish(
        PhoneNumber="+12269788073",
        Message= msg
        )
        time.sleep(1)
    elif(temp_s1 < 16):
        print('Warning: Too cold, turning on the Heater')
        ### need to write AWS code
        msg = dt_string +'\n'+ "Warning! House is too cold, Please turn on the Heater switch" 
        client.publish(
        PhoneNumber="+12269788073",
        Message= msg
        )
        time.sleep(1)
    else:
        print('No action required, ideal temperature at house!')
        time.sleep(1)
def humidity_sensor():
    # Humidity Sensor -> Ideal range is 30 to 50%
    humidity_s1 = int(input('Humidity value from the sensor: '))
    if(humidity_s1 < 30):
        print('Warning: Humidity range not appropriate')
        ### need to write AWS code
        msg = dt_string +'\n'+ "Warning! Humidity is low, Please turn on the humidifier" 
        client.publish(
        PhoneNumber="+12269788073",
        Message= msg
        )
        time.sleep(1)
    else:
        print('No action required, humidity levels are proper!')
        time.sleep(1)
def co2_sensor():
    # Carbondioxide (CO2) Sensor -> Ideal value is below 800ppm
    co2_s1 = int(input('PPM value from the CO2 sensor: '))

    if(co2_s1 > 800):
        print('Warning: CO2 levels are high')
        ### need to write AWS code
        msg = dt_string +'\n'+ "Warning! CO2 levels exceeded in the house. Please evacuate or open the windows" 
        client.publish(
        PhoneNumber="+12269788073",
        Message= msg
        )
        time.sleep(1)
    else:
        print('No action required, ideal CO2 at house!')
        time.sleep(1)
def face_recog():

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("unknown_person.jpg",frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    #comparing the images
    img1 = face_recognition.load_image_file("Picture_new.jpg")
    img2 = face_recognition.load_image_file("unknown_person.jpg")
    img1_enc = face_recognition.face_encodings(img1)[0]
    img2_enc = face_recognition.face_encodings(img2)[0]
    result = face_recognition.compare_faces([img1_enc],img2_enc)
    if result[0] == True:
        print("Access Granted")

        time.sleep(1)
    else:
        print("Security Breach")
        msg = dt_string +'\n'+ "Warning! Unidentified person is trying to enter your house" 
        client.publish(
        PhoneNumber="+12269788073",
        Message= msg
        )
        time.sleep(1)
def main ():
    flag = 0
    while flag !=6:
        print("\nPlease select one of the following features:")
        print("1. Smoke Detector \n2.Temperature Sensor \n3. Humidity Sensor \n4. Co2 Sensor \n5. Face Recognition \n6. Exit")
        flag = int(input())
        match flag:
            case 1: smoke_sensor()
            case 2: temp_sensor()
            case 3:humidity_sensor()
            case 4:co2_sensor()
            case 5: face_recog()
            case 6: print("Thank you")
main()

