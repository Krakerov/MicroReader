import cv2

#Screenshot_2
def nothing(x):
	pass


def img2txt(f, img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, binar = cv2.threshold(img, 225, 255, cv2.THRESH_BINARY_INV)
    res =  cv2.resize(binar, (128,64), interpolation=cv2.INTER_LINEAR) 
    string = '$$$'
    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j]:
                #print(i)
                #print(str(j) + '\n')
                stri = str(100 + i)[1:]
                strj = str(1000 + j)[1:]
                string += strj + stri
    string += '$'
    f.write(string)
    cv2.imshow('test', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def preimg(name):
    
    if name[1]!=':':
        img = cv2.imread(name + '.png')
    else:
        img = cv2.imread(name)

    (h, l) = img.shape[:2]
    print(h,l)
    cv2.namedWindow('Track')   
    cv2.createTrackbar('Hight',"Track", 1, 10, nothing)
    cv2.createTrackbar('Len',"Track", 1, 10, nothing)
    PH = 0
    PL = 0
    while True:
        if name[1]!=':':
            img = cv2.imread(name + '.png')
        else:
            img = cv2.imread(name)
        #img = cv2.imread(name + '.png')
        H = int(cv2.getTrackbarPos('Hight',"Track"))
        L = int(cv2.getTrackbarPos('Len',"Track"))
        for i in range(H):
            cv2.line(img, (0, int(h/H*(i+1))), (l, int(h/H*(i+1))), (0, 255, 0), 2)
        for i in range(L):
            cv2.line(img, (int(l/L*(i+1)), 0), (int(l/L*(i+1)), h), (0, 255, 0), 2)
        if PH !=H or PL!=L:
            print(str(int(h/H))+' '+str(int(l/L)))
            PH = H
            PL = L
        cv2.imshow('Orig', img)
        
        k = cv2.waitKey(500) & 0xFF
        if k == 27:
            break
    
    #img = cv2.imread(name + '.png')
    
    print("Начало создания")
    f = open(name + '.txt','w')
    for i in range(H):
        for j in range(L):
            newimg = img[int(i*h/H):int((i+1)*h/H), int(j*l/L):int((j+1)*l/L)]
            img2txt(f,newimg)
    f.close()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


while True:
    a = input("img2txt: ")
    if a[:3] != "xyi":
        preimg(a)
    else:
        break
