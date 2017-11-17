import glob
import random
from vidpy import Clip, Composition, Text
import time

text = '''The history of all hitherto existing society
is the history of class struggles.
Freeman and slave, patrician and plebeian,
lord and serf, guild-master and journeyman,
in a word, oppressor and oppressed,
stood in constant opposition to one another,
carried on an uninterrupted, now hidden,
now open fight, a fight that each time ended,
either in a revolutionary reconstitution of society at large,
or in the common ruin of the contending classes.
In the earlier epochs of history,
we find almost everywhere a complicated arrangement of society
into various orders, a manifold gradation of social rank.'''

sentences = text.split('\n')
sentence = random.choice(sentences)
sentence = sentence.strip()
sentence = sentence.upper()

backgrounds = glob.glob('images/*.jpg')
background_image = random.choice(backgrounds)


background_clip = Clip(background_image)
background_clip.squareblur('0=0.8;40=0;60=0.2;100=0')
clip = Text(sentence, olcolor='#00000', outline=10)
# clip.position(x=0)
clip.glow()

composition = Composition([background_clip, clip], width=1280, height=720, duration=5)
# composition.save('commie_{}.mp4'.format(time.time()))
composition.preview()
