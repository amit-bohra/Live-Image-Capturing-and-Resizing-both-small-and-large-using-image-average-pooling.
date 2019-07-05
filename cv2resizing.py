import cv2
import numpy as np
v=cv2.VideoCapture(0)
ret,i=v.read()
#i=cv2.imread(r'c.png')
img=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
lx=len(img[:,0])
print(lx)
ly=len(img[0,:])
print(ly)
si=2
pi=64
kx=15
ky=20
cv2.imshow('hello',img)
while(si<=80):
    key=cv2.waitKey(0)
    if key==ord('a'):
        a=np.array([])
        for i in range(0,lx,si):
            for j in range(0,ly,si):
                f=0
                for q in range(0,si):
                    f+=sum(img[i,j:j+si])
                    i+=1
                f=f//(si*si)
                i-=si
                a=np.append(a,f)
        s=a.reshape(lx//si,ly//si)
        simg = s.astype(np.uint8)
        cv2.imshow('no',simg)
        print('size',simg.shape)
        kx=len(simg[:,0])
        ky=len(simg[0,:])
        si*=2
        pi//=2
        print('si',si)
        print('pi',pi)
        
    elif key==ord('s'):
        a=np.array([])
        for i in range(0,kx):
            for w in range(1,pi+1):
                for j in range(0,ky):
                    f=simg[i,j]
                    for r in range(1,pi+1):
                        a=np.append(a,f)
        s=a.reshape(kx*pi,ky*pi)
        simg = s.astype(np.uint8)
        cv2.imshow('no',simg)
        pi*=2
        si//=2
        print('si',si)
        print('pi',pi)
    elif key==ord('q'):
        cv2.destroyAllWindows()
        v.release()
        quit()
    
