'''
programmer:Ryan Tan
requirement of homework:
1、segment
2、compute the width of the block

3、calculate the area of the block

'''

import numpy as np
import cv2

#function for verify if the points is in the left edge
def checkall(img2,x1,y1):
 a=0 
 for p in img2[y1,x1+1:x1+122]:
   if p == 255:
      a=1
      break
   if p== 0:
      a=3
 if a==1:
   return False
 else :
   return True

#function for verify if the points is in the right edge
def checkall2(img2,x3,y3):
 a=0 
 for p in img2[y3,x3-122:x3-1]:
   if p == 255:
      a=1
      break
   if p== 0:
      a=3
 if a==1:
   return False
 else :
   return True


img = cv2.imread('source.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,10,300)
#selct the region of two egde
img2=canny[0:1200,540:860]

y=0
x=0
p=0
x2=161

#build a black mask to draw the segement edge
mask = np.zeros((1200,320),np.uint8)

#the list follow is to store the points we need
T=[]
J=[]
T1=[]
J1=[]

#the loop can compute the left edge points and right edge points 
for q in range(0,1200):
  
 for i in img2[y,0:160]:
  
  if i==255 and checkall(img2,x,y):
   mask[y,x]=255
   T.append(y)
   J.append(x)
   break
  x=x+1

 for i in img2[y,161:320]:  
  if i==255 and checkall2(img2,x2,y):
   mask[y,x2]=255
   T1.append(y)
   J1.append(x2)
   break
  x2=x2+1
 x2=161
 x=0
 y=y+1

#using numpy discrete integral algorithm to compute area of the block 
area=((np.trapz(J1,T1))-(np.trapz(J,T)))
print('the block  area is:',area)

X=np.ravel(x2)
Y=np.ravel(x)

maxWidth=np.max(X-Y)
print('the max width:',maxWidth)


cv2.imshow('segment',canny)
cv2.imshow('segment2',mask)
cv2.waitKey(0)

