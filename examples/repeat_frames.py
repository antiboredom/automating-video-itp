import sys
import moviepy.editor as mp

def repeat_frames(videofile, segment_length, repeat):
    original_video = mp.VideoFileClip(videofile)
    duration = original_video.duration

    clips = []

    clip_start = 0
    while clip_start < duration:
        clip_end = clip_start + segment_length

        if clip_end > duration:
            clip_end = duration

        clip = original_video.subclip(clip_start, clip_end)

        for i in range(0, repeat):
            clips.append(clip)

        clip_start = clip_end


    final_video = mp.concatenate(clips)

    final_video.write_videofile('repeated.mp4', codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')


if __name__ == '__main__':
    repeat_frames(sys.argv[1], float(sys.argv[2]), int(sys.argv[3]))






