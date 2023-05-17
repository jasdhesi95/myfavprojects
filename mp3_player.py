import pygame
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    # Create a Tkinter root window (hidden) to use the file dialog
    Tk().withdraw()

    # Open a file dialog to select the MP3 file
    file_path = askopenfilename(filetypes=[("MP3 Files", "*.mp3")])

    if file_path:
        play_music(file_path)
        input("Press Enter to stop the music...")
        stop_music()

if __name__ == "__main__":
    main()
