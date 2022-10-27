from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
from os import chdir, makedirs
from os.path import basename
from pathlib import Path

video = VideoFileClip('got_fired_captions.mp4').resize(width=1080)

bg = (ImageClip('vertical_highlight_bg.jpg')).set_duration(video.duration+2)

final = CompositeVideoClip([bg, video.set_position("center")])
outputName = f'vertical.mp4'

final.write_videofile(str(Path(outputName)))