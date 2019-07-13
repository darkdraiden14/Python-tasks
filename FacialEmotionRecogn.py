# load json and create model
from __future__ import division
print("There will be a screen press 'q' when you want to click the picture")
ch=input("GOT IT : then type Y:")

if ch =='Y':
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.models import model_from_json
    import os
    import numpy as np
    import cv2
    starting camera
    cap=cv2.VideoCapture(0)
    while cap.isOpened():
        status,frame=cap.read()
        cv2.imshow('live',frame)
        if cv2.waitKey(10) & 0xff == ord('q') :
            break
    
    cv2.imwrite("test.jpeg",frame)
    cv2.destroyWindow('live')
    cv2.destroyAllWindows() # this will destroy all windows	
    #	 to close camera
    cap.release()	
    #loading the model
    json_file = open('fer.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("fer.h5")
    print("Loaded model from disk")	
    #setting image resizing parameters
    WIDTH = 48
    HEIGHT = 48
    x=None
    y=None
    labels = ['Angry', 'Sad', 'Fear', 'Joy', 'Sad', 'Surprised/Happy', 'Neutral']
    #loading image
    full_size_image = cv2.imread("test.jpeg")
    print("Image Loaded")
    gray=cv2.cvtColor(full_size_image,cv2.COLOR_RGB2GRAY)
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face.detectMultiScale(gray, 1.3  , 10)
    #detecting faces
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        cv2.normalize(cropped_img, cropped_img, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
        cv2.rectangle(full_size_image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        #predicting the emotion
        yhat= loaded_model.predict(cropped_img)
        cv2.putText(full_size_image, labels[int(np.argmax(yhat))], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
        print("Emotion: "+labels[int(np.argmax(yhat))])
        choice=input("Do you want to listen Something:")
        if choice=='Y' or choice=='y':
            import googlesearch
            released = {"Sad" : 'sad songs youtube',"Joy" : 'rock music youtube',"Angry" : 'angry mood songs youtube',"Surprised/Happy" : 'EDM Songs',"Neutral" : 'evergreen songs youtube',"Fear" : 'hanuman chalisa youtube',}
            #print (released)
            mymood = released.get(labels[int(np.argmax(yhat))], "none")
            mysonglist=[]
            for url in googlesearch.search_videos(mymood,stop=11):
                #url = url.replace("watch","embed")
                mysonglist.append(url)
            songnum = np.random.randint(1,10)
            song_name=mysonglist[songnum] #Open Tab
            import webbrowser
            webbrowser.open(mysonglist[songnum])
        elif choice=='N' or choice=='n':
            print("So you have chosen not too listen anything. So have a good Day Byee")	
        else:
            print("Wrong choice")
else:
	print("Read Instruction Carefully. See ya next time")
