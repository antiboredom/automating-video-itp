import glob
import random
import time
from vidpy import Clip, Composition

hands = glob.glob('hands/*.mp4')
hand = random.choice(hands)
print hand

clips = []
x = -400
start = 0

backgrounds = ['#2cffff', '#fc282a', '#fcdb2a', '#2452d8']

for i in range(0, 6): # same as for i in [0, 1, 2, 3, 4]
    clip = Clip(hand)
    clip.chroma()
    clip.set_offset(start)
    clip.position(x=x)
    clip.fadein(0.2)
    clip.fadeout(0.2)

    clips.append(clip)

    start += 0.5
    x += 150

composition = Composition(clips, bgcolor=random.choice(backgrounds))

outname = 'coolhands_{}.mp4'.format(int(time.time()))
composition.save(outname)
