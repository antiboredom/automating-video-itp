## FFMPEG

Official site: [https://ffmpeg.org](https://ffmpeg.org)

Documentation: [https://ffmpeg.org/ffmpeg.html](https://ffmpeg.org/ffmpeg.html)

Filter documentation: [https://ffmpeg.org/ffmpeg-filters.html](https://ffmpeg.org/ffmpeg-filters.html)

### Installation

#### Mac (the harder way)

Install homebrew

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Use brew to install ffmpeg

```bash
brew install ffmpeg --with-ffplay
```

#### Mac (The easier way)

[Download ffmpeg](http://lav.io/ffmpeg.zip) and unzip it.

Then, in the terminal type:

```
mv ~/Downloads/ffmpeg /usr/local/bin/
```

#### Windows
Download from here:
[https://ffmpeg.zeranoe.com/builds/
](https://ffmpeg.zeranoe.com/builds/)

--------

### Basic Use

Converting from one format to another:

```
ffmpeg -i input.mp4 output.avi
```

Turning a video into a gif:

```
ffmpeg -i input.mp4 output.gif
```

Turning a video into choppier but smaller gif:
(```-r 3``` will make it 3 frames per second)

```
ffmpeg -i input.mp4 -r 3 output.gif
```

Extracting the audio:

```
ffmpeg -i input.mp4 audio.mp3
```

Extracting frames from a video:

```
ffmpeg -i input.mp4 frame%d.jpg
```

Turning a series of images into a video:

```
ffmpeg -f image2 -i image%d.jpg video.mp4
```

Increasing the speed of a video:

```
ffmpeg -i input.mp4 -vf "setpts=0.5*PTS" fastvideo.mp4
```

Slowing it down:

```
ffmpeg -i input.mp4 -vf "setpts=2.0*PTS" slowvid.mp4
```

Resize a video:

```
ffmpeg -i input.mp4 -c:v libx264 -s:v 100x100 -c:a copy output.mp4
```

Extracting a portion of a video:
(this will get five seconds, starting at 1 minute and 30 seconds)

```
ffmpeg -ss 00:01:30 -i input.mp4 -c:v copy -c:a copy -t 5 output.mp4
``` 


### More complex stuff


Making a mirror effect:

```
ffmpeg -i input.mp4 -vf "crop=iw/2:ih:0:0,split[left][tmp];[tmp]hflip[right];[left][right] hstack" output.mp4
```


Edge detection:

```
ffmpeg -i input.mp4 -vf "edgedetect=low=0.1:high=0.4" output.mp4
```

Fading in:

```
ffmpeg -i input.mp4 -vf "fade=in:0:30" output.mp4
```

Slow down a video with frame interpolation:

```
ffmpeg -i input.mp4 -vf ""[0:v]minterpolate=fps=120:mi_mode=mci[out];[out]setpts=5*PTS"" -y output.mp4
```

Stitch together all mp4s in a folder:

```
ffmpeg -f concat -i <(for f in /path/to/folder/*.mp4; do echo "file '$f'"; done) -c copy output.mp4
```
