import face_recognition
import pickle
import cv2
import os
 
def Face_recog_function():
    dirname = os.path.dirname(__file__)
    #find path of xml file containing haarcascade file
    cascPathface = os.path.join(dirname, "haarcascade_frontalface_alt2.xml")
    # load the harcaascade in the cascade classifier
    faceCascade = cv2.CascadeClassifier(cascPathface)
    # load the known faces and embeddings saved in last file
    
    #Find path to the image you want to detect face and pass it here

    image = cv2.imread(os.path.join(dirname, 'image.png'))
    image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
    file=open(os.path.join(dirname,'face_enc'),"rb")
    data = pickle.loads(file.read())
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #convert image to Greyscale for haarcascade
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # faces = faceCascade.detectMultiScale(gray,
    #                                     scaleFactor=1.1,
    #                                     minNeighbors=5,
    #                                     minSize=(60, 60),
    #                                     flags=cv2.CASCADE_SCALE_IMAGE)
    
    # the facial embeddings for face in input
    encodings = face_recognition.face_encodings(rgb)
    print(len(encodings))
    print(len(data))
    names = []
    # loop over the facial embeddings incase
    # we have multiple embeddings for multiple fcaes
    for encoding in encodings:
        #Compare encodings with encodings in data["encodings"]
        #Matches contain array with boolean values and True for the embeddings it matches closely
        #and False for rest
        matches = face_recognition.compare_faces(data["encodings"],
        encoding)
        #set name =inknown if no encoding matches
        name = "Unknown"
        # check to see if we have found a match
        if True in matches:
            #Find positions at which we get True and store them
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                #Check the names at respective indexes we stored in matchedIdxs
                name = data["names"][i]
                #increase count for the name we got
                counts[name] = counts.get(name, 0) + 1
                #set name which has highest count
                name = max(counts, key=counts.get)
    
    
            # update the list of names
            names.append(name)
        
    print(names)
    if len(names)>0:       
        return max(names, key = names.count)
    return "Unknown"

