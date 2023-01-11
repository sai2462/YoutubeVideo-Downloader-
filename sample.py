
SAVE_PATH = "D:/" 

from pytube import YouTube

# Prompting user for Youtube Video link
youtube_url = input("Please enter youtube link ")

# Creating YouTube object with the link
myVideo = YouTube(youtube_url)

# Creating StreamQuery Object
myVideoStream = myVideo.streams

# print(myVideoStream)
# Using Filters on the myVideoStream Object
webmStreams = myVideoStream.filter(mime_type = "video/mp4")

# print(webmStreams)

webmStreams.first().download(SAVE_PATH)



print("Your Files are downloaded successfully")