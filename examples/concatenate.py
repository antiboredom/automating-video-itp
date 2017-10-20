import sys
import moviepy.editor as mp

videos = []

for filename in sys.argv[1:]:
    video = mp.VideoFileClip(filename)

    # just get the first second
    video = video.subclip(0, 1)

    # make all videos the same size
    video = video.resize((1280, 720))
    videos.append(video)

final_video = mp.concatenate_videoclips(videos, method="compose")
final_video.write_videofile('composition.mp4', codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
