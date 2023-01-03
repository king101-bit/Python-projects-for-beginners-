from datetime import datetime, time
import time as t
from pytube import YouTube
import pygame

# Search for the bell sound on YouTube
query = "bell sound"
yt = YouTube("https://youtu.be/TRgs9jv8ah0")
search_results = yt.search(query)

# Select the first result
result = search_results[0]

# Download the audio file
audio_file = result.get_audio()

# Save the audio file to a temporary file
temp_file = "temp.mp3"
audio_file.download(temp_file)

# Initialize pygame
pygame.init()

timetable = [
    (time(8, 30), time(9, 20)),  # Period 1
    (time(9, 20), time(10, 10)),  # Period 2
    (time(10, 30), time(11, 20)),  # Period 3
    (time(11, 20), time(12, 10)),  # Period 4
    (time(12, 10), time(13, 0)),  # Lunch
    (time(13, 0), time(13, 50)),  # Period 5
    (time(13, 50), time(14, 40)),  # Period 6
    (time(14, 40), time(15, 30))  # Period 7
]

while True:
    current_time = datetime.now().time()
    for start, end in timetable:
        if start <= current_time < end:
            # Calculate the time remaining in the current period
            period_length = (end - start).total_seconds()
            time_elapsed = (current_time - start).total_seconds()
            time_remaining = period_length - time_elapsed
            # Wait until the end of the period
            t.sleep(int(time_remaining))
            # Play the bell sound
            pygame.mixer.music.load(temp_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            pygame.mixer.music.stop()
            pygame.quit()
