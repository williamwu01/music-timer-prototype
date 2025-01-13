import os

MP3_PATH = "C:\\Users\\info\\Downloads\\test.mp3"
    
def play_music_on_vlc():
	## function for playing the music on vlc 
    try:
        print("Playing MP3 file with VLC...")
        os.system("vlc " + " --intf dummy " + MP3_PATH + ' --play-and-exit')
    except Exception as e:
        print(f"Error while trying to play MP3: {e}")

def main():
    play_music_on_vlc()

main()



#for testing 
# Get the current working directory
# current_dir = os.getcwd()
# print("Current Directory:", current_dir)

# List files and directories in the current directory
# files = os.listdir()
# print("Files in directory:", files)

# Create a new directory
# os.mkdir("new_directory")
# print("New directory created!")
