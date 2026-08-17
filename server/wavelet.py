#wavelet transformation to extract impoirtant information for the computer 
#to understand the images
import cv2
import numpy as np
import pywt

def w2d(img, mode='haar', level=3):
    imArray = img
    #Datatype conversions
    #convert from clor to gray scale
    imArray= cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)
    #convert to float
    imArray=np.float32(imArray)
    imArray/=255;
    #compute coefficients
    coeffs=pywt.wavedec2(imArray, mode, level=level)

    #process Coefficients
    coeffs_H=list(coeffs)
    coeffs_H[0]*=0;
    #reconstruction
    imArray_H=pywt.waverec2(coeffs_H, mode);
    imArray_H *=255;
    imArray_H= np.uint8(imArray_H)
    return imArray_H
    