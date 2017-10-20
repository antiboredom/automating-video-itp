import moviepy.editor as mp

clip1 = mp.ColorClip((1280, 720), col=(255, 0, 0))
clip1 = clip1.set_duration(5)

clip2 = mp.ImageClip('someimage.jpg')
clip2 = clip2.set_duration(10)

final_video = mp.concatenate_videoclips([clip1, clip2], method="compose")
final_video.write_videofile('composition.mp4', fps=24, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
