import subprocess
import os
def download_videos(link_dict, title_dict, video_fmt):
    for name in link_dict.keys():
        title = title_dict[name][0]  + video_fmt
        dirname = title_dict[name][1]
        link = link_dict[name]
        
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        os.chdir(dirname)
        
        print '\n-->Downloading, Title: ', name
        #subprocess.call(['C:\Program Files (x86)\Internet Download Manager\IDMan.exe',\
        #                 '/p', os.getcwd(),\
        #                 '/f', title,\
        #                 '/a',\
        #                 '/d', link])
        os.chdir('..')
    
