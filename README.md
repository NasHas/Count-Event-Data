# Count-Event-Data
Count event data from video footage of the Da Vinci Surgical System (Da Vinci Robot)

The code is open-source. However, when using the code, please make a reference to our paper and repository.

Instructions:

1) Open Python
2) Copy the code
3) Place the video files you want to analyze in your PythonProjects-folder on you computer
4) Before going to the next step, make sure to take a snapshot of the area of interest. Fx. If you want to look at coagulation, take a snapshot of the coagulation mark, when it is activated. Crop the image, so only that part of the picture is saved. Save the image in you PythonProjects-folder. This image is your target pattern, which the algorithm will find and count whenever activated. You can have up to five target patterns (armswap, clutch, camera-movement and coagulation left, coagulation right). (Note: If you want to register both cut also, six target patterns must be used - this can be added to the source-code in the same manners as the five abovementioned target patterns.)
5) In the code the last line is called 'How to use the count event data function'. In this example, write the name of your video-file and the names of your target patterns, and run the program. You can run multiple lines at the same time.
6) If you want, the code in the middle that has been commented out, can be inserted again, so you can visually see how the code finds the events. A window with the video will appear, and every time an event is activated, fx. when coagulation is used or clutch is used, a red marker will appear around the pattern. After the script has finished, you will get the count of the event in total amount, and also get the total amount of seconds used to process the video. 
While the code is running, you will be able to the status in percent in the window. 

/Hashemi et. al., Acquisition and usage of robotic surgical data for machine learning analysis. Surg Endosc. 2023 Jun 30
