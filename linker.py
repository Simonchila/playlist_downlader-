import os

link = input("Enter your link here: ")

# Ensure FFmpeg is used for merging
os.system(f"yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]' --merge-output-format mp4 -o '%(title)s.%(ext)s' {link}")

