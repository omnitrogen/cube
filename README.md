# cube

![alt tag](https://www.grubiks.com/images/rc.png)

TIPE project: build a machine that can solve a Rubik's cube.

TODO:

* detect colors on each face of the cube (with a lib like OpenCV)

    _the program take a pic as an input:_

    ![alt tag](https://github.com/omnitrogen/cube/blob/opencv-color-detection/cube4.png)
    
    _then it crop the image at size of the cube_

    ![alt tag](https://github.com/omnitrogen/cube/blob/opencv-color-detection/crop.png)

    _then it reduces the number of colors = color quantization (using K-means clustering)_

    ![alt tag](https://github.com/omnitrogen/cube/blob/opencv-color-detection/crop_quantization.png)

    _TODO: apply color tresholding to guess the color of each cube_
    
    
* move stepper motors (NEMA 17HS4401) with GPIO pins on a raspberry pi and/or Arduino chip (controlled by a DRV8825 Stepper Motor Pilote Module) 

* create a GUI to control all these things (Tkinter) :rainbow:


