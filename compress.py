import os
from moviepy.editor import VideoFileClip

# set the parameters for the compressed videos
fps = 15
bitrate = '500k'
resolution = (720/2, 1280/2) # set to desired resolution

# set the paths for the input and output folders
input_folder = 'videos_full'
output_folder = 'videos_compressed'



# loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4'):

        # check if the compressed file already exists in the output folder
        if os.path.exists(os.path.join(output_folder, filename)):
            print(f'Skipping {filename} as it already exists in the output folder')
        else:
            # load the video clip and set the parameters
            video_clip = VideoFileClip(os.path.join(input_folder, filename))
            video_clip = video_clip.resize(resolution)
            video_clip.fps = fps
            
            # compress the video and save to the output folder
            compressed_filename = os.path.join(output_folder, filename)

            #compressed_filename = compressed_filename.split(".")[0]+".webm"
            video_clip.write_videofile(compressed_filename, bitrate=bitrate,
                    audio_codec="aac",
                    codec="libx264")
            
            print(f'Compressed {filename} and saved to {compressed_filename}')
