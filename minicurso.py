# Bibliotecas necessárias para progrmação
import cv2
import numpy as np
  
# Capturando o vídeo para utilizar
cap = cv2.VideoCapture('sample.mp4')
  
# Mostrando o vídeo em loop
while (cap.isOpened()):
  
    # Isolando os quadros
    ret, frame = cap.read()
    frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,
                         interpolation = cv2.INTER_CUBIC)
    
    #pegando uma subparte do frame
    #frame2 = frame[150:260 , 0:540]
    
    #criando nosso propróprio filtro
    #kernel = np.array(([[-1, 2,- 1], [-2, 4, -2], [-1, 2, -1]]), np.float32)
    #frameteste = cv2.filter2D(frame, -1, kernel)
    
    
    # Display the resulting frame
    cv2.imshow('Original', frame)
    #cv2.imshow('Frame2', frame2)
    #cv2.imshow('NossoFiltro', frameteste)
  
    # conversion of BGR to grayscale is necessary to apply this operation
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
  
    # adaptive thresholding to use different threshold 
    # values on different regions of the frame.
    Thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                           cv2.THRESH_BINARY_INV, 11, 2)
    gaussianblur = cv2.GaussianBlur(frame, (5, 5), 0) 
    edge_detect = cv2.Canny(frame, 100, 200)
    BIT = cv2.bitwise_not(frame, frame, mask = mask)
    cv2.imshow('BIT', BIT)
    cv2.imshow('Edge detect', edge_detect)
    cv2.imshow('gblur', gaussianblur)
    cv2.imshow('Thresh', Thresh)
    # define q as the exit button
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
  
# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv2.destroyAllWindows()