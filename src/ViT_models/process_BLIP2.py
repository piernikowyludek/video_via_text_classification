import torch
import argparse
import pandas as pd
from tqdm import tqdm
from transformers import Blip2Processor, Blip2ForConditionalGeneration

from src.utils.video_utils import sample_frames, save_frames


def run_blip2_inference(video_paths, save_path, mode, job_index):
    # initialize the model
    processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
    #model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-flan-t5-xxl", torch_dtype=torch.float16) 
    model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b",
                                                        torch_dtype=torch.float16,
                                                        device_map="auto")
                                                        #load_in_8bit=True)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    for video_path in tqdm(video_paths):
        frames = sample_frames(video_path, num_frames=5)
        # save the frames - useful for visualisation later
        saved_image_paths = save_frames(frames, save_path, video_path)
        
        results = []
        for image, image_path in zip(frames, saved_image_paths):
            caption = caption_image(image, model, processor, mode)
            results.append({'video': video_path, 'image_path': image_path, 'caption': caption})

    df = pd.DataFrame(results)
    df.to_csv('/efs/results/blip2_'+{mode}+'_captions_{job_index}.txt')


def caption_image(image, model, processor, mode):
    prompt = "What action or activity is taking place in this image?"
    if mode == 'prompt':
        inputs = processor(image, text=prompt, return_tensors="pt").to(device, torch.float16)
    elif mode == 'noprompt':
        inputs = processor(image, return_tensors="pt").to(device, torch.float16)
    generated_ids = model.generate(**inputs, max_new_tokens=50)
    generated_text = processor.decode(generated_ids[0], skip_special_tokens=True).strip()
    return generated_text


def main():
    parser = argparse.ArgumentParser(description="Process command line arguments.")
    
    # Adding arguments
    parser.add_argument("txt_file", help="Path to .txt file containing paths to videos")
    parser.add_argument("save_folder", help="Path to folder where files sampled frames from videos will be saved",
                        default='/efs/data/images/')
    parser.add_argument("mode", help="Mode - using Blip2 with or without prompt", choices=['prompt', 'noprompt'])
    parser.add_argument("job_index", help="Job Index - to keep track of split between GPUs")                

    # Parsing arguments
    args = parser.parse_args()

    # Accessing arguments
    files_folder = args.files_folder
    save_folder = args.save_folder
    mode = args.mode
    job_index = args.job_index

    run_blip2_inference(files_folder, save_folder, mode, job_index)

if __name__ == "__main__":
    main()
