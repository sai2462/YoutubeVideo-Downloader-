from flask import Flask, render_template, request
import os
from pytube import YouTube
import random

VideoDownloder = Flask(__name__)

destFolder = os.path.join('static', 'downloads')

VideoDownloder.config['UPLOAD_FOLDER'] = destFolder

@VideoDownloder.route('/')
def index():
	return render_template('userpage.html')

@VideoDownloder.route('/', methods = ['POST'])
def getvalue():
	lnk = request.form['lnk']
	resol = request.form['quality']
	SAVE_PATH = "static/downloads"

	try:

		fileName = "V"+ str(random.randint(1,999999))+".mp4"
		myVideo = YouTube(lnk)
		myVideoStream = myVideo.streams

		mp4Streams = myVideoStream.filter(mime_type = "video/mp4")
		if(resol == "1"):
			mp4Streams.first().download(f"{SAVE_PATH}", filename = fileName)
		else:
			mp4Streams.last().download(f"{SAVE_PATH}", filename = fileName)

	except:
		return render_template('Failure.html')


	myVDO = os.path.join(VideoDownloder.config['UPLOAD_FOLDER'], fileName)
	print(myVDO)
	return render_template('OutPage.html', user_video = myVDO)

if(__name__ == '__main__'):
	VideoDownloder.run(host = "0.0.0.0", debug = True)