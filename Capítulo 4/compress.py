import pydicom
import numpy as np
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from cv2 import imread, imwrite
import cv2

arquivo = open('arquivo.txt', 'w')
arquivo.write('Imagemoriginal;Imagemteste;shift' + '\n')
for i in xrange(0, 10):
    #carregar imagem dicom
    ds = pydicom.dcmread(str(i)+'.dcm')
    array = ds.pixel_array

    #shift para valores positivos
    shift = np.abs(np.min(array))
    array_png = array + shift

    #salvar em png
    image = Image.fromarray(array_png)
    image.save(str(i)+'.png')
    jp2 = [10,20,30,50]
    for j in jp2:
        arquivo.write(str(i)+'.png'+';'+str(i)+'_'+str(j)+'.jp2'+';'+str(shift)+'\n')
arquivo.close()
