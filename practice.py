from playsound import playsound
import time
import threading

# --- Play song in background ---
def play_song():
    playsound("mann_mera.mp3")

threading.Thread(target=play_song).start()

# --- Lyrics with timings (you can adjust delays) ---
lyrics = [
    ("saari raat aahen bharta", 2.5),
    ("pal pal yaadon mein marta", 3.0),
    ("maane na meri mann mera", 3.0),
    ("", 1.0),
    ("thoda thoda hosh madhoshi si hai,", 3.0),
    ("neend behoshi si hai,", 3.0),
    ("jaane kuchh bhi na mann mera..", 3.0)
]

# --- Print lyrics using your timing ---
for line, delay in lyrics:
    print(line)
    time.sleep(delay)
