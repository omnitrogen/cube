# cube

![alt tag](https://www.grubiks.com/images/rc.png)

TIPE project: build a machine that can solve a Rubik's cube.

Steps: 

* take a pic and detect colors on each face of the cube (with a lib like OpenCV)

	* _the Raspberry Pi is connected to the GoPro over wifi_

	* _the GoPro take a pic and save it_

    * _the ColorFinder class take a pic as an input:_

    ![alt tag](https://github.com/omnitrogen/cube/blob/opencv-color-detection/cube4.png)
    
    * _then it crop the image at size of the cube_

    ![alt tag](https://github.com/omnitrogen/cube/blob/opencv-color-detection/crop.png)

    * _then it reduces the number of colors to 6 colors = color quantization (using K-means clustering)_

    ![alt tag](https://github.com/omnitrogen/cube/blob/opencv-color-detection/crop_quantization.png)

    * _then it compares every color to its nearest color from the 6 rubiks cube color and output a list of each square color_
    
    
* move stepper motors (NEMA 17HS4401) with GPIO pins on a raspberry pi and/or Arduino chip (controlled by a DRV8825 Stepper Motor Pilote Module) 

* create a GUI to control all these things (Tkinter) :rainbow:


