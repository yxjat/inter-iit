import cv2

class shapeclassifier:
  def __init__(self):
    pass
  
  def classify(self, cnt):
    shape="unclassified"
    pm=cv2.arcLength(cnt, True)
    approx=cv2.approxPolyDP(cnt, 0.04 *pm, True)

    if(len(approx)==3):
        shape='Triangle'
    elif(len(approx))==4:
        (x,y,w,h)=cv2.boundingRect(approx)
        asprat=w/float(h)
        if (asprat<=1.05 and asprat >=0.95):
            shape='Square'
        else :
            shape='Rectangle'
    elif(len(approx)>5):
        shape='Circle'
    else:
      return len(approx)
    return shape