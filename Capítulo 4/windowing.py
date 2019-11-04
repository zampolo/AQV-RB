import pydicom
import numpy as np
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from cv2 import imread, imwrite
import cv2

arquivo = open('arquivo.txt', 'r')
ct = arquivo.read()
aa = ct.split('\n')
aa = aa[:-1]
aa = aa[1:len(aa)]
arquivo.close()

file_name = open('file_name.txt', 'w')
file_name.write('Imagemoriginal;Imagemteste;shift' + '\n')
def wind(windType):
    if windType == 'soft':
        l,w = 40,80 # soft tissue (radiant viewer) 40,68 (Nando)
    else:
        l,w = 300, 1500 #  bone (radiant viewer) 570,3200 (Nando)
    return l,w

def window(pix, w, l):
    
    s, h = pix.shape
    a = l-(w/2.0)
    b = l+(w/2.0)
    new = np.copy(pix)
    for i in range(s):
        for j in range(h):
            if pix[i,j]>b:
                new[i,j] = (65536.0)
            elif pix[i,j]<a:
                new[i,j] = 0
            else:
                new[i,j] = ((pix[i,j] - a)/(b-a))*(65536.0)
    return new

windType = 'soft'
l,w = wind(windType)

for i in xrange(0,len(aa)):
    line = aa[i].split(';')
    image_pil = Image.open(line[1])
    image = np.array(image_pil)
    shift = float(line[2])
    new_image = image-shift
    win = ['soft','bone']
    for j in win:
        name = line[1].split('.')
        l,w = wind(str(j))
        image_win = window(new_image,w,l)
        image_int = np.trunc(image_win)
        image_int = image_int.astype('int32')
        image_windowing = Image.fromarray(image_int)
        image_windowing.save(str(name[0])+'_'+str(j)+'.png')
        file_name.write(str(line[0])+';'+ str(name[0])+'_'+str(j)+'.png'+';'+str(shift)+'\n')
