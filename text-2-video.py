import os
import time

from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# The text that will be typed out in the video
text = "Hello, this is a sample text that will be typed out in the video."

# The duration of the video in seconds
duration = 5

# The frame rate of the video
fps = 30

# The font size of the text
font_size = 30

# The font family of the text
font_family = 'Arial'

# The color of the text
color = 'red'

# The background color of the text
bg_color = 'white'

# The horizontal alignment of the text
horizontalalignment = 'left'

# The vertical alignment of the text
verticalalignment = 'bottom'

# The figure and axis objects for the Matplotlib animation
fig, ax = plt.subplots()

# Hide the axis and frame of the figure
ax.axis('off')
ax.set_frame_on(False)

# Set the figure and axis background colors
fig.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

# Set the figure and axis sizes to match the video dimensions
fig.set_size_inches(1280/100, 720/100)
ax.set_position([0, 0, 1, 1])

# Set the text properties
text_obj = ax.text(0, 0, '', fontsize=font_size,
                   fontfamily=font_family, color=color,
                   horizontalalignment=horizontalalignment,
                   verticalalignment=verticalalignment)

# Function to update the text of the animation at each frame
def update_text(i):
    text_obj.set_text(text[:i])
    return (text_obj,)

# Create the animation using the update function
anim = animation.FuncAnimation(fig, update_text, frames=len(text)+1, interval=1000/fps)

# Convert the animation to a video clip
clip = VideoClip(mplfig_to_npimage, duration=duration)
clip = clip.set_duration(duration)

# Save the video to a file
clip.write_videofile("typing_text.mp4", fps=fps)
