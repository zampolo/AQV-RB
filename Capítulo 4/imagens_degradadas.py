import dicom
import StringIO
from pgmagick import Image as Im
import matplotlib.pyplot as plt
import windowing
import numpy as np
from PIL import Image 

windType = 'bone' # window type (bone or soft)
def wind(windType):
    if windType == 'soft':
        l,w = 40,80 # soft tissue (radiant viewer) 40,68 (Nando)
    else:
        l,w = 300, 1500 #  bone (radiant viewer) 570,3200 (Nando)
    return l,w

arquivo = open('arquivo.txt', 'w')
arquivo.write('Imagemoriginal;Imagemteste;' + '\n')

windType = ['bone', 'soft']
for j in windType:
    l,w = wind(j) 
    for i in xrange(0, 3):
        
        ds = dicom.read_file(str(i)+".dcm")
        pix = ds.pixel_array
        new_soft = windowing.window(pix, w, l)
        plt.imsave('Orig_'+str(i)+'_'+j+'.png', new_soft, cmap = plt.cm.gray)
        img = Im('Orig_'+str(i)+'_'+j+'.png')
        jp2 = [10,20,30,40,50,60,70,80,90]
        for k in jp2:
            img.quality(k)
            img.write('Test_'+str(i)+'_'+str(k)+'_'+j+'.jp2')
            arquivo.write('Orig_'+str(i)+'_'+j+'.png' + ';' + 'Test_'+str(i)+'_'+str(k)+'_jp2_'+j+'.png' + '\n')
            im = Image.open('Test_'+str(i)+'_'+str(k)+'_'+j+'.jp2')
            plt.imsave('Test_'+str(i)+'_'+str(k)+'_jp2_'+j+'.png', im, cmap = plt.cm.gray)
        jpg = [10,20,30,40,50,60,70,80,90]
        for k in jpg:
            img.quality(k)
            img.write('Test_'+str(i)+'_'+str(k)+'_'+j+'.jpg')
            arquivo.write('Orig_'+str(i)+'_'+j+'.png' + ';' + 'Test_'+str(i)+'_'+str(k)+'_jpg_'+j+'.png' + '\n')
            im = Image.open('Test_'+str(i)+'_'+str(k)+'_'+j+'.jpg')
            plt.imsave('Test_'+str(i)+'_'+str(k)+'_jpg_'+j+'.png', im, cmap = plt.cm.gray)
        
arquivo.close()
