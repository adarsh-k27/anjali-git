import cv2
import PySimpleGUI as sg
import numpy as np
from keras.models import load_model

model = load_model('model_file_30epochs.h5')
print("model loaded")
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print("detection variable added")
labels_dict = {0: 'Angry', 1: 'Disgust', 2: 'Fear',
               3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprise'}

sg.theme('DarkAmber')

# layout = [[sg.Text('Some text on Row 1')],
#           [sg.Text('Enter something on Row 2'), sg.InputText()],
#           [sg.Button('Ok'), sg.Button('Cancel')]]

First_Cloumn = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FileBrowse()
    ],
    [
        sg.Button('Predict',size=(10,2))
    ]
]

image_viewer_column=[
    [
        sg.Text("choose An image From Left")
    ],
    [
        sg.Text(size=(40,1),key="-TOUT-")
    ]
]

layout = [
   [
       sg.Column(First_Cloumn),
       sg.VSeperator(),
       sg.Column(image_viewer_column),
   ]
]

window = sg.Window('Window Title', layout)

print("layout created")

while True:
    event,values=window.read()
    file_name=""
    if event =="Exit" or event== sg.WIN_CLOSED:
        break
    
    if event=="-FOLDER-":
        file_name=values["-FOLDER-"]
        
    if event=="Predict" and file_name=="" :
        window["-TOUT-"].update("Not Choose anything !!!")
    else:
        break
            
window.close() 

print("file choosed for prediction",file_name)

print("start mage reading")
frame = cv2.imread(file_name)
print("image readed")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# print("gray",gray)
faces = faceDetect.detectMultiScale(gray, 1.3, 5)
# print("face", faces)
for x, y, w, h in faces:
    sub_face_img = gray[y:y+h, x:x+w]
    resized = cv2.resize(sub_face_img, (48, 48))
    normalize = resized/255.0
    # we want to reshabe before go through model
    reshaped = np.reshape(normalize, (1, 48, 48, 1))
    result = model.predict(reshaped)
    label = np.argmax(result, axis=1)[0]
    print(label)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
    cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
    cv2.putText(frame, labels_dict[label], (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

cv2.imshow("Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


