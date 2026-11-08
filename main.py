import requests
from pathlib import Path
import re

# Supported video formats
VIDEO_EXTENSIONS = {".mkv", ".mp4", ".avi", ".m4v", ".mov"}

# Get the IMDb ID
imdb_id = input("IMDb ID: ")

# Connect to the API
url = f"http://127.0.0.1:8000/episodes/{imdb_id}"
response = requests.get(url)
response.raise_for_status()

data = response.json()

# Get the show's directory
current_dir = Path(input("Enter the show's directory: ")).expanduser()

if not current_dir.exists() or not current_dir.is_dir():
    print("Invalid directory.")
    exit()
    
show_name = current_dir.name

# Find all season folders
season_folders = sorted(
    [folder for folder in current_dir.iterdir() if folder.is_dir()],
    key=lambda folder: int(re.search(r"\d+", folder.name).group())
    if re.search(r"\d+", folder.name) else 999
)

print(f"\nShow: {show_name}")
print(f"Seasons found: {len(season_folders)}")


# Process each season
for season_number, season_folder in enumerate(season_folders, start=1):

    season_key = str(season_number)

    if season_key not in data["seasons"]:
        print(f"Missing API data for {season_number}")
        continue

    # Get episode information
    episodes = data["seasons"][season_key]

    # Sort episodes by episode number
    episodes = sorted(
        episodes.items(),
        key=lambda episode: int(re.search(r"E(\d+)", episode[0]).group(1))
    )

    # Find video files
    video_files = sorted(
        [
            file for file in season_folder.iterdir()
            if file.is_file() and file.suffix.lower() in VIDEO_EXTENSIONS
        ]
    )

    print(f"\nProcessing {season_folder.name}")
    print(f"Files found: {len(video_files)}")
    print(f"Episodes found: {len(episodes)}")

    # Make sure the number of files matches the number of episodes
    if len(video_files) != len(episodes):
        print("WARNING: File count doesn't match episode count!")
        print("Skipping this season to prevent incorrect renaming.")
        continue

    # Rename files
    for video_file, (episode_code, episode_name) in zip(video_files, episodes):

        new_name = (
            f"{show_name} - {episode_code} - {episode_name}"
            f"{video_file.suffix.lower()}"
        )

        new_path = video_file.with_name(new_name)

        if new_path.exists():
            print(f"Skipping: {new_name} already exists.")
            continue

        print(f"{video_file.name} -> {new_name}")

        video_file.rename(new_path)
