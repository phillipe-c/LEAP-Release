# ██       ████████████ ██████ ████████████ 
# ██       ██          ██    ██ ██        ██
# ██       ██████      ████████ ███████████ 
# ██       ██          ██    ██ ██          
# ████████ ███████████ ██    ██ ██          

#########################################################
#  LISA Music Streaming Service (LMSS)
#  
#  Created by Phillipe Caetano.
#  Copyright © 2022 Phillipe Caetano. All rights reserved.
##########################################################

# Modules
from debugpy import listen
from youtubesearchpython import VideosSearch
import sys
from playsound import playsound
from pytube import YouTube
import multiprocessing
import platform

# Variables
path = "/Users/phillipecaetano/Downloads/"
query = str(' '.join(sys.argv[1:]))
hotwords = ['parar', 'para', 'pare', 'pausa', 'pause', 'chega', 'parô', 'parou', 'lisa', 'elisa', 'linda']
filename = 'temporary_audio.mp4'
artist_separating_words = ["de", "da", "do"]

# Functions
def preprocess_query(query, artist_separating_words = artist_separating_words):
	for a in artist_separating_words:
		if a in query:
			preocessed_query = query.split(' ')
			preocessed_query.reverse()
			artist = []
			song = []
			went_through = False
			at_artist = True
			for n, i in enumerate(preocessed_query):
				if i in artist_separating_words and went_through == False:
					went_through = True
					at_artist = False
				else:
					if at_artist == True:
						artist.append(i)
					else:
						song.append(i)
			artist.reverse()
			song.reverse()
			return {"SONG": " ".join(song), "ARTIST": " ".join(artist)}
	
	for a in artist_separating_words:
		if a not in query:
			return {"SONG": query, "ARTIST": ""}


def get_video_link(query):
	videosSearch = VideosSearch(query, limit = 2)
	result = videosSearch.result()
	return str(result['result'][0]['link'])

def download_video(video_link, filename = 'temporary_audio.mp4', path=path):
	yt = YouTube(video_link)
	videos = yt.streams
	stream_number = len(videos)-4
	video_to_download = videos[stream_number]
	video_to_download.download(path, filename)

def play(filename = 'temporary_audio.mp4', path=path):
	playsound(path+filename)
	print("A")


# All the stuff coming together
name = preprocess_query(query)
song = name['SONG'] + name['ARTIST']
link = get_video_link(query=song)
download_video(link)

if __name__ == "__main__":
		p = multiprocessing.Process(target=play)
		p.start()
		from hotword_detection import hotword_engine
		hotword_engine.start_listener(hotwords, print_=False)
		while True:
			try:
				if hotword_engine.hotword_detection(hotwords, print_=False) == 1:
					print("OK") # this line is absolutely necessary for lisa to continue working 
					p.terminate()
					hotword_engine.clear_all()
			except:
				break
