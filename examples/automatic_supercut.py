import sys
from pattern.en import ngrams
import videogrep
from collections import Counter

videofile = sys.argv[1]
subtitlefile = videofile.replace('.mp4', '.srt')

lines = open(subtitlefile).read()
grams = ngrams(lines, n=3)

most_common = Counter(grams).most_common(1)

phrase = most_common[0][0]
phrase = ' '.join(phrase)

print phrase

outputfile = videofile + '.most_common.mp4'
videogrep.videogrep([videofile], outputfile, phrase, 're')

