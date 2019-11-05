# -*- coding: utf-8 -*-
# windowing.py
#
# Author: Luana Gonçalves, and Ronaldo F. Zampolo
#
# 2017, Feb. 7
#

import numpy as np
import matplotlib.pyplot  as plt
import scipy
import dicom

def window(pix, w, l):
# image transform to better analyse specific anatomical features
#
# window(pix, w, l)
# inputs:
#   pix: original image (np.array)
#   w: window width (int)
#   l: window center (int)
#
# output:
#   new: transformed image (np.array)
#
# 2017, Feb. 7
#
    s, h = pix.shape
    a = l-(w/2.0)
    b = l+(w/2.0)
    new = np.empty(pix.shape)
    for i in range(s):
        for j in range(h):
            if pix[i,j]>b:
                new[i,j] = 255
            elif pix[i,j]<a:
                new[i,j] = 0
            else:
                new[i,j] = ((pix[i,j] - a)/(b-a))*255.0
    return new
    
# Function test
#ds = dicom.read_file('9.dcm') # read a dicom file
#pix = ds.pixel_array          # dicom pixels are stored in a variable
'''
# typical w,l values obtained from radiantviewer.com/dicom-viewer-manual.html/change_brightness_contrast.html
windType = 'soft' # window type (bone or soft)
if windType == 'soft':
    l,w = 40,80 # soft tissue (radiant viewer) 40,68 (Nando)
else:
    l,w = 300, 1500 #  bone (radiant viewer) 570,3200 (Nando)

# Presenting some data for verification
print('=============== Verification data ===================')
print('Minimum pixel value: ', pix.min() )
print('Maximum pixel value: ', pix.max() )
print('Window parameters (L,W): ', l, w )
print('Lowest Window value: ', l-w/2.0 )
print('Highest Window value: ', l+w/2.0 )

#n = window(pix,w,l) # window function call

# Presenting original image
plt.figure(1)
plt.imshow(pix, plt.cm.bone, vmin = pix.min(), vmax=pix.max())
plt.title('Original image')

# Presenting processed image
plt.figure(2)
plt.imshow(n, plt.cm.bone, vmin = 0, vmax=255)
plt.title('Transformed image')

plt.show()
'''
