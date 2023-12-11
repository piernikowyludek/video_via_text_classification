import cv2
import os
from pathlib import Path


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

def save_frames(frames, folder_path, video_path):
    """
    Saves a list of images to a specified folder.

    :param frames: List of images (as NumPy arrays).
    :param folder_path: Path to the folder where images will be saved.
    """
    # Create the folder if it doesn't exist
    category = video_path.split('/')[-2]
    video_name = video_path.split('/')[-1].with_suffix('')
    folder_path = Path(folder_path) / category / video_name
    folder_path.mkdir(parents=True, exist_ok=True)

    image_paths = []
    # Save each image in the specified folder
    for i, image in enumerate(frames):
        image_path = folder_path / f'image_{i}.jpg'
        cv2.imwrite(image_path, image)
        image_paths.append(image_path)
    return image_paths