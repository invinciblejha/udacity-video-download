import urllib2
import json
import re
import urllib
import urlparse

def get_video_id(url):
    url = urllib2.urlopen(url)
    data = json.load(url)
    data_dump = str(data['payload']['course_rev']['units'])
    ids = re.findall('\'youtube_id\': u\'(.*?)\'', data_dump)
    return ids

def prepare_youtube_urls(ids):
    youtube_urls = list()
    for vid in ids:
        url = 'http://www.youtube.com/watch?v=' + vid
        youtube_urls.append(url)
    return youtube_urls
        
def extract_youtube_url(url):
    ids = get_video_id(url)
    youtube_urls = prepare_youtube_urls(ids)
    return youtube_urls


def extract_download_urls(urls, code):
    count = 0;
    dict_link = dict()
    for video_url in urls:
        video_id = re.findall('http://www.youtube.com/watch\?v=(.*)', video_url)[0]
        get_vars = urlparse.parse_qs(urllib.unquote(urllib2.urlopen("http://www.youtube.com/get_video_info?video_id=" + video_id).read()))
        title = get_vars['title'][0]
        
        i = 0
        entries = get_vars['itag']
        for entry in entries:
            match = re.search(r'.*itag=' + str(code), entry)
            if match:
                break
            i = i + 1
            
        if not match:
            print 'ERROR: Couldn\'t Download video: ', title
            continue

        link = get_vars['itag'][i]
        link = re.findall(r'\d+,url=(.*)', link)[0]
        dict_link[title] = link

    return dict_link
        
        
      

        
#urls = extract_youtube_url(json_url)
#dict_link = extract_download_urls(urls, 35)
    
     

    
