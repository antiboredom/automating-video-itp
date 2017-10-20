import sys
import random
import moviepy.editor as mp

def randomize_video(videofile, segment_length):
    original_video = mp.VideoFileClip(videofile)
    duration = original_video.duration

    clips = []

    clip_start = 0
    while clip_start < duration:
        clip_end = clip_start + segment_length

        if clip_end > duration:
            clip_end = duration

        clip = original_video.subclip(clip_start, clip_end)
        clips.append(clip)

        clip_start = clip_end

    random.shuffle(clips)

    final_video = mp.concatenate_videoclips(clips)

    final_video.write_videofile('random.mp4', codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')


if __name__ == '__main__':
    randomize_video(sys.argv[1], float(sys.argv[2]))




