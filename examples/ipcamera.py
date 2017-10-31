'''
Control an axis IP camera with python
Manual can be found at: https://www.axis.com/files/manuals/um_p5534_45175_en_1112.pdf
Pan/tilt/zoom api (see page 20): https://www.axis.com/files/manuals/vapix_ptz_52933_en_1307.pdf
'''

import requests
import subprocess

# change the BASE_URL as needed
BASE_URL = 'http://172.22.151.17'
CONTROL_URL = BASE_URL + '/axis-cgi/com/ptz.cgi'
MJPG_URL = BASE_URL + '/mjpg/video.mjpg'
RTSP_URL = (BASE_URL + ':554/axis-media/media.amp').replace('http://', 'rtsp://')

USER = 'root'
PASS = 'enter'


def relative_zoom(steps):
    '''
    Zooms the camera in or out relative to current zoom
    positive value zooms in, negative zooms out
    '''
    requests.get(CONTROL_URL, {'rzoom': steps})


def zoom(steps):
    '''
    Zooms to specific location between 1 and 9999
    '''
    requests.get(CONTROL_URL, {'zoom': steps})


def pan(location):
    '''Pans to a specific location between -180 and 180'''
    requests.get(CONTROL_URL, {'pan': location})


def tilt(location):
    '''Tilts to a specific location between -180 and 180'''
    requests.get(CONTROL_URL, {'tilt': location})


def center(x, y):
    '''Centers the camera on an x,y coordinate'''
    requests.get(CONTROL_URL, {'center': '{},{}'.format(x, y)})


def move(location):
    '''
    Moves the image 25 % of the image field width in the specified direction.
    '''
    valid = ['home', 'up', 'down', 'left', 'right',
             'upleft', 'upright', 'downleft', 'downright', 'stop']
    if location in valid:
        requests.get(CONTROL_URL, {'move': location})


def record(outputname, duration='10:00:00', rtsp=True):
    '''
    Records a video from the camera
    Default duration is for 10 hours
    You can either use rtsp or mjpeg
    '''

    if rtsp:
        args = ['ffmpeg', '-i', RTSP_URL, '-vcodec', 'copy', '-acodec', 'copy', '-f', 'mp4', '-t', duration, '-y', outputname]
    else:
        args = ['ffmpeg', '-f', 'mjpeg', '-r', '30', '-i', MJPG_URL, '-t', duration, '-y', outputname]

    # records in the background to allow script to continue
    subprocess.Popen(args)
