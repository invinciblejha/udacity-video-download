from com.playlist import *
from com.vdata import *
from com.ntype2 import *
from com.download import *

"""
code = 34 for 640*360
code = 35 for 854*480(Default)
code = 22 for 1270*720
"""

code = 35


if code == 22:
    video_fmt = '.mp4'
else:
    video_fmt = '.flv'


units = [ 'http://www.youtube.com/playlist?list=PL1EF620FCB11312A6',\
          'http://www.youtube.com/playlist?list=PL107FD47786234011',\
          'http://www.youtube.com/playlist?list=PL5493E5D24A081719',\
          'http://www.youtube.com/playlist?list=PLAADAB4F235FE8D65',\
          'http://www.youtube.com/playlist?list=PL1B9983ACF22B1920',\
          'http://www.youtube.com/playlist?list=PLC9ED5AC39694C141',\
          'http://www.youtube.com/playlist?list=PL3475310BFB1CBE34'\
        ]
for i in xrange(0, 10):
    youtube_urls = pvideo_url(units[i])
    link_dict = extract_download_urls(youtube_urls, code)
    title_dict = type2(link_dict, i+1)
    download_videos(link_dict, title_dict, video_fmt)

