import cv2


def sample_frames(video_path, num_frames=5):
    """
    Samples a specified number of equidistant frames from a given .avi video file.
    
    video_path (str): Path to the .avi video file.
    num_frames (int, optional): Number of frames to sample. Defaults to 5.

    Returns:
    list: A list containing the sampled frames as images.

    Example:
    sampled_frames = sample_frames("path_to_video.avi", 5)
    """
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Error opening video file {video_path}")

    # Get total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the interval to sample frames
    interval = total_frames // num_frames

    # List to store sampled frames
    sampled_frames = []

    for i in range(num_frames):
        # Set the current frame position
        frame_position = i * interval
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_position)

        # Read the frame
        ret, frame = cap.read()

        if ret:
            # Save the frame to the list
            sampled_frames.append(frame)
        else:
            # Handle the case where frame couldn't be read
            print(f"Error reading frame at position {frame_position}")

    # Release the video capture object
    cap.release()

    return sampled_frames