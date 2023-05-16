# Count-Event-Data
Count event data from video footage of the Da Vinci Surgical System (Da Vinci Robot)

The code is open-source. However, when using the code, please make a reference to our paper and repository.

Instructions:

1) Open Python
2) Copy the code
3) Place the video files you want to analyze in your PythonProjects-folder on you computer
4) Before going to the next step, make sure to take a snapshot of the area of interest. Fx. If you want to look at coagulation, take a snapshot of the coagulation mark, when it is activated. Crop the image, so it is only that part of the picture. Save the image in you PythonProjects-folder. This image is your target pattern, which the algorithm will find and count whenever activated.
5) In the code the last line is called 'How to use the count event data function'. In this example, write the name of your video-file and the name of your target pattern, and run the program. You can run multiple lines at the same time.
6) You will get a window with the video, and every time the event is activated, fx. coagulation is used, or clutch is used, a red marker will appear around the pattern. After the script has finished, you will get the count of the event in total amount. 

/Hashemi et al. 2023
