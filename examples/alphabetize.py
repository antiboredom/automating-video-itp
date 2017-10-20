import sys
import moviepy.editor as mp
import audiogrep


videofile = sys.argv[1]

# get the sentence timestamps
sentences = audiogrep.convert_timestamps([videofile])

timestamps = []
for sentence in sentences:
    timestamps += sentence['words']

# alphabetize the list
timestamps.sort(key=lambda x: x[0])

# we could limit how many clips here
# words = words[100:200]

original_video = mp.VideoFileClip(videofile)

clips = []

for timestamp in timestamps:
    word = timestamp[0]
    start = float(timestamp[1])
    end = float(timestamp[2])

    # skip this clip if the word is shorter than 5 characters

    if len(word) < 5:
        continue

    clip = original_video.subclip(start, end)
    clips.append(clip)


final_video = mp.concatenate_videoclips(clips)
final_video.write_videofile('alphabetized.mp4', codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
