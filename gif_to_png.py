from PIL import Image
import os

def gif_to_png(the_gif, folder_name):
    # check if the folder exists, if not, create it
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    img = Image.open(the_gif)
    index = 0
    
    try:
        while True:
            # save the current frame
            frame_name = f"frame_{index:04d}.png"
            img.save(os.path.join(folder_name, frame_name), "PNG")
                
            # move to the next frame
            index += 1
            img.seek(index)
    except EOFError:
        # this happens when there are no more frames
        print(f"Finished! {index} frames saved in the folder: '{folder_name}'")

# run the function (change the gif name)
gif_file = "gif_name_here.gif" 
output_folder = "output_frames"
gif_to_png(gif_file, output_folder)