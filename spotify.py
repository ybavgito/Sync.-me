'''Developed by Mukunth Vaibhav | Sync.me'''

import sys
import json
import spotipy
import spotipy.util as util
import os
import getPicture
import getMood
import createPlaylist
import getTrainingData
import learnSongs

#Tries to obtain username from terminal
if len(sys.argv) > 1:
	username = sys.argv[1]

else:
	print("Please supply a user ID")
	sys.exit()

scopes = ("user-read-recently-played"
		  " user-top-read"
		  " user-library-modify"
		  " user-library-read"
		  " user-read-private"
		  " playlist-read-private"
		  " playlist-modify-public"
		  " playlist-modify-private"
		  " user-read-email"
		  " user-read-private"
		  " user-read-playback-state"
		  " user-modify-playback-state"
		  " user-read-currently-playing"
		  " app-remote-control"
		  " streaming"
		  " user-follow-read"
		  " user-follow-modify")

#Fetching Permission to access spotify

try:
	token = util.prompt_for_user_token(username,scopes,
								   client_id='b05498d9c6164304a950fc2fd185e19c',
								   client_secret='3e406d9ddb2a4b1aa96fce31d72b5f75',
								   redirect_uri='http://google.com/')
except:
	os.remove(".cache-{}".format(username))
	token = util.prompt_for_user_token(username,scopes,
								   client_id='b05498d9c6164304a950fc2fd185e19c',
								   client_secret='3e406d9ddb2a4b1aa96fce31d72b5f75',
								   redirect_uri='http://google.com/')
#Takes picture of user to analyze their mood after they have provided permission
getPicture.getPicture()

if token:
	#define spotify object and user
	sp = spotipy.Spotify(auth=token)
	user = sp.current_user()

	#will run till user quits the program
	while True:
		print("Welcome to the Sync.me. We got you,fam !")
		print("Please choose an option.")
		print("0-Create personalized playlist")
		print("1-exit")
		print("")
		choice = input("Your choice: ")
		#create personalized playlist
		if choice == '0':
			#user can manually input mood
			print("If you would like to manually input a mood, please enter happy, angry, sad, or relaxed. Else just click enter.")
			choice =  input("Your choice: ")
			if choice != '':
				mood = choice
			#otherwise program will try to guess user's mood
			else:
				mood = getMood.getMood()
			model = learnSongs.main()
			createPlaylist.main(sp, user, model, mood)
			print("Successfully created playlist!")
		#End program
		if choice == '1':
			break
