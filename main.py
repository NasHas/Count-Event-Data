import cv2


def count_event_data(Video: "video.mp4", targetPattern: "image.png") ->"prints count of item":
    """

    :param Video:  e.g. 'video.mp4'
    :param targetPattern: e.g. "image.png"
    """

    # Load the video file
    cap = cv2.VideoCapture(Video) # e.g. 'video.mp4'
    # Load the pattern image
    pattern_img = cv2.imread(targetPattern) # e.g. "image.png"
    # Convert the pattern image to grayscale
    pattern_gray = cv2.cvtColor(pattern_img, cv2.COLOR_BGR2GRAY)
    # Get the width and height of the pattern image
    pattern_w, pattern_h = pattern_gray.shape[::-1]
    # Initialize the video writer for the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (640, 480))
    # Initialize the list to store the location of the pattern in each frame
    frame_list = []
    # Loop through each frame in the video
    frame_num = 0
    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            # Convert the frame to grayscale
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Perform template matching
            res = cv2.matchTemplate(frame_gray, pattern_gray, cv2.TM_CCOEFF_NORMED)

            # Define a threshold for the match score
            threshold = 0.9

            # Get the location of the match
            loc = cv2.minMaxLoc(res)
            frame_list.append(loc[1])
            if loc[1] >= threshold:
                # Draw a rectangle around the match
                top_left = loc[3]
                bottom_right = (top_left[0] + pattern_w, top_left[1] + pattern_h)
                cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

            # Write the frame to the output video
            out.write(frame)

            # Display the frame
            # cv2.imshow('frame', frame)

            # Exit the loop if 'q' key is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

            frame_num += 1
        else:
            break
    # Release the video capture and close the windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    # Release the video writer
    out.release()
    # Destroy all windows
    cv2.destroyAllWindows()
    # Create marked array of stars, where the item value is >= than threshold.
    marked_list = ['*' if item >= threshold else item for item in frame_list]
    # Count the first appearence of star-item.
    count_item = 0
    last_char = None
    for i, char in enumerate(marked_list):
        if char == '*':
            if last_char != '*':
                count_item += 1
        last_char = char
    # Print the number of changepoints detected
    print("Number of coagulation:", count_item)

#How to use the count event data function
count_event_data("Dag 2 Knud lymfe 2.mp4","targetPattern.png")

#Second example
count_event_data("Dag 2 Knud lymfe 2.mp4","targetPattern (2).png")