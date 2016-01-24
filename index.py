"""
you know, i love downloading files, like, game, applications, musics, video, and pdf file.
i store all my downloaded file in one folder it is in 'C:\Users\ANdersoN\Downloads'.
when i opened my download folder, i see bunch of stupid file rigt there, and i decided to manage them, so i created this simple program..
this program will reads a folder contents and will move them to some folder based on theirs extensions. for an example, if a file with name maroon5.mp3 in download folder, then this program will move that file to Music folder. yea. just that. thank you. sorry for my bad english.
"""
from fileman import Fileman
import os
from time import sleep
manager = Fileman()
files = (manager.read_directory())#read a folder contents
for i in files:
    if os.path.isfile(os.path.join(manager.folder, i)) :#loop and check does i is a file?
        fd_name = manager.get_folder_name(i) #get the folder name, [destination folder]
        if fd_name != None: #make sure if the file extension is listed in supported extension
            source = os.path.join(manager.folder, i) #the current file location
            destination = os.path.join(manager.folder, fd_name, i) #destination folder
            try:
                print(manager.move_it(source, destination)+' ::> '+os.path.join(fd_name,i)) #tell it, does it success or fail
            except Exception as e:
                print(e) #error handling and keep my program working
            
sleep(3)#sleep for 3 secs

