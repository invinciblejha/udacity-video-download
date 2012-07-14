import re
import urllib2
youtube_url = 'http://www.youtube.com'
def pvideo_url(purl):
    page = urllib2.urlopen(purl)
    htmlSource = page.read()
    video_urls = re.findall(r'href="(/watch\?v=.*?)&.*?index', htmlSource, re.DOTALL)
    video_urls = [ str(youtube_url + url) for url in video_urls ]
    return video_urls
