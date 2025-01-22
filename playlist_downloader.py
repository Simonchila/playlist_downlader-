import yt_dlp


def download_playlist(playlist_url, download_path="downloads"):
    try:
        # Options for yt-dlp to download the playlist
        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'format': 'best',  # Download the best quality
        }

        # Create a yt-dlp object with the options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the playlist
            print(f"Downloading playlist: {playlist_url}")
            ydl.download([playlist_url])

        print("Playlist download complete.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    playlist_url = input("Enter the playlist URL: ")
    download_path = input(
        "Enter the download folder path (default: 'downloads'): ") or "downloads"

    download_playlist(playlist_url, download_path)
