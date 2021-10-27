import cv2 as cv
import numpy as np

confThreshold = 0.5
nmsThreshold = 0.5

def getOutputsNames(net):
    layersNames = net.getLayerNames()
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    classIds = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                center_x = int(detection[0] * frameWidth)
                center_y = int(detection[1] * frameHeight)
                width = int(detection[2] * frameWidth)
                height = int(detection[3] * frameHeight)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        color = (255,255,0)
        if classIds[i] == 0:          # Blue if person
            color = (255,0,0)
        elif classIds[i] == 2:        # Green if car  
            color = (0,255,0)
        elif classIds[i] == 7:        # Red if Truck
            color = (0,0,255)
        
        label = '%s:%s' %  (classes[classIds[i]],round(confidences[i]*100))
        cv.putText(frame,label,(left,top-10),cv.FONT_HERSHEY_SIMPLEX,0.3,color,1)
        cv.rectangle(frame, (left, top), (left+width, top+height),color, 2)

classes = []
with open(r"path\\coco.names") as f:
    classes = f.read().rstrip('\n').split('\n')
print(classes)


modelConfiguration = "path\\yolov3.cfg"
weights = "path\\yolov3.weights"
net = cv.dnn.readNetFromDarknet(modelConfiguration,weights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)



cap = cv.VideoCapture("demo_Trim.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    blob = cv.dnn.blobFromImage(frame,1/225,(416,416),[0,0,0],1)
    net.setInput(blob)
    outs = net.forward(getOutputsNames(net))
    postprocess(frame, outs)

    cv.imshow("frame",frame)
    if cv.waitKey(100) == 27:
        break
cap.release()
cv.destroyAllWindows()
    
