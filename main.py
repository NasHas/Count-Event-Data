
#Counting of Event Data from video file.

#Count Event Data
import cv2
import time

def count_event_data(Video: "video.mp4", targetPattern1: "image.png",targetPattern2,targetPattern3,targetPattern4,targetPattern5, frame_list1,frame_list2,frame_list3,frame_list4,frame_list5) ->"prints count of item":


    # Load the video file
    cap = cv2.VideoCapture(Video) # e.g. 'video.mp4'

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # Load the pattern image
    pattern_img1 = cv2.imread(targetPattern1) # e.g. "image.png"
    pattern_img2 = cv2.imread(targetPattern2)  # e.g. "image.png"
    pattern_img3 = cv2.imread(targetPattern3)  # e.g. "image.png"
    pattern_img4 = cv2.imread(targetPattern4)  # e.g. "image.png"
    pattern_img5 = cv2.imread(targetPattern5)  # e.g. "image.png"

    # Convert the pattern image to grayscale
    pattern_gray1 = cv2.cvtColor(pattern_img1, cv2.COLOR_BGR2GRAY)
    pattern_gray2 = cv2.cvtColor(pattern_img2, cv2.COLOR_BGR2GRAY)
    pattern_gray3 = cv2.cvtColor(pattern_img3, cv2.COLOR_BGR2GRAY)
    pattern_gray4 = cv2.cvtColor(pattern_img4, cv2.COLOR_BGR2GRAY)
    pattern_gray5 = cv2.cvtColor(pattern_img5, cv2.COLOR_BGR2GRAY)

    # # # Get the width and height of the pattern image
    # pattern_w1, pattern_h1 = pattern_gray1.shape[::-1]
    # pattern_w2, pattern_h2 = pattern_gray2.shape[::-1]
    # pattern_w3, pattern_h3 = pattern_gray3.shape[::-1]
    # pattern_w4, pattern_h4 = pattern_gray4.shape[::-1]
    # pattern_w5, pattern_h5 = pattern_gray5.shape[::-1]

    # # Initialize the video writer for the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (640, 480))

    # Loop through each frame in the video
    frame_num = 0
    desired_progress = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            # Convert the frame to grayscale
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Perform template matching
            res1 = cv2.matchTemplate(frame_gray, pattern_gray1, cv2.TM_CCOEFF_NORMED)
            res2 = cv2.matchTemplate(frame_gray, pattern_gray2, cv2.TM_CCOEFF_NORMED)
            res3 = cv2.matchTemplate(frame_gray, pattern_gray3, cv2.TM_CCOEFF_NORMED)
            res4 = cv2.matchTemplate(frame_gray, pattern_gray4, cv2.TM_CCOEFF_NORMED)
            res5 = cv2.matchTemplate(frame_gray, pattern_gray5, cv2.TM_CCOEFF_NORMED)

            # Define a threshold for the match score
            threshold = 0.98
            threshold2 = 0.95

            # Get the location of the match
            loc1 = cv2.minMaxLoc(res1)
            loc2 = cv2.minMaxLoc(res2)
            loc3 = cv2.minMaxLoc(res3)
            loc4 = cv2.minMaxLoc(res4)
            loc5 = cv2.minMaxLoc(res5)

            #list for finding first macth
            frame_list1.append(loc1[1])
            frame_list2.append(loc2[1])
            frame_list3.append(loc3[1])
            frame_list4.append(loc4[1])
            frame_list5.append(loc5[1])

            # if loc1[1] >= threshold:
            # Draw a rectangle around the match
            #            top_left = loc1[3]
            #            bottom_right = (top_left[0] + pattern_w1, top_left[1] + pattern_h1)
            #            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

            # if loc2[1] >= threshold:
            #Draw a rectangle around the match
            #            top_left = loc2[3]
            #            bottom_right = (top_left[0] + pattern_w2, top_left[1] + pattern_h2)
            #            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

            # if loc3[1] >= threshold:
            #Draw a rectangle around the match
            #            top_left = loc3[3]
            #            bottom_right = (top_left[0] + pattern_w3, top_left[1] + pattern_h3)
            #            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

            # if loc4[1] >= threshold:
            #Draw a rectangle around the match
            #            top_left = loc4[3]
            #            bottom_right = (top_left[0] + pattern_w4, top_left[1] + pattern_h4)
            #            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

            # if loc5[1] >= threshold:
            #Draw a rectangle around the match
            #            top_left = loc5[3]
            #            bottom_right = (top_left[0] + pattern_w5, top_left[1] + pattern_h5)
            #            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

            #Write the frame to the output video
            #            out.write(frame)

            #Display the frame
            # resized_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            # cv2.imshow('frame', resized_frame)

            #Exit the loop if 'q' key is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                 break
            #
            frame_num += 1
            progress = (frame_num / total_frames) * 100
            if progress in desired_progress or progress == 100:
                 print("Progress in percent:", progress)
        else:
            break
    # Release the video capture and close the windows
    cap.release()
    #out.release()
    cv2.destroyAllWindows()

    # Create marked array of stars, where the item value is >= than threshold.
    marked_list1 = ['*' if item >= threshold else item for item in frame_list1]
    marked_list2 = ['*' if item >= threshold else item for item in frame_list2]
    marked_list3 = ['*' if item >= threshold2 else item for item in frame_list3]
    marked_list4 = ['*' if item >= threshold2 else item for item in frame_list4]
    marked_list5 = ['*' if item >= threshold2 else item for item in frame_list5]

    # Finding counts
    find_count(marked_list1,targetPattern1)
    find_count(marked_list2,targetPattern2)
    find_count(marked_list3,targetPattern3)
    find_count(marked_list4,targetPattern4)
    find_count(marked_list5,targetPattern5)


def find_count(marked_list,targetPattern):
    # Count the first appearence of star-item.
    count_item = 0
    last_char = None
    for i, char in enumerate(marked_list):
        if char == '*':
            if last_char != '*':
                count_item += 1
        last_char = char
    # Print the number of changepoints detected
    print(f"Number of count:",targetPattern, count_item)

############### How to use the count event data function ###############
# First example

# Timer for measure time of execution
start_time = time.time()
#Start the list to store the location of the pattern in each frame
frame_list1 = []
frame_list2 = []
frame_list3 = []
frame_list4 = []
frame_list5 = []
count_event_data("Video.mp4","TargetPattern1.png", "TargetPattern2.png", "TargetPattern3.png", "TargetPattern4.png", "TargetPattern5.png", frame_list1, frame_list2, frame_list3, frame_list4, frame_list5)

#In the Video.mp4, the name of your video-file should be inserted. In the TargetPattern1-5.png the name of your target pattern images should be inserted.

end_time = time.time()
execution_time = end_time - start_time

print("Execution Time:", execution_time, "seconds")


# Second example - can be initialized simultaneously. You can have as many examples as you like.

# Timer for measure time of execution
start_time = time.time()
#Start the list to store the location of the pattern in each frame
frame_list1 = []
frame_list2 = []
frame_list3 = []
frame_list4 = []
frame_list5 = []
count_event_data("Video.mp4","TargetPattern1.png", "TargetPattern2.png", "TargetPattern3.png", "TargetPattern4.png", "TargetPattern5.png", frame_list1, frame_list2, frame_list3, frame_list4, frame_list5)

end_time = time.time()
execution_time = end_time - start_time

print("Execution Time:", execution_time, "seconds")