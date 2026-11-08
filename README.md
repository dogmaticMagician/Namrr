# Namrr - Episode Naming Tool for Jellyfin

**DISCLAIMER** - Namrr is in no way associated with any of Servarr's software.

Namrr is an episode naming/renaming tool for Jellyfin.
When you rip physical media from something like a Blu-Ray or a DVD, the episodes are very rarely named in a way that Jellyfin will recognize.
Typically, the only thing you can do about this is go in and manually rename every episode.  Nobody wants to do that.
Luckily, you can now get around this by using Namrr!

## Installation

Installing Namrr is super easy and straightforward.
1. Download the .zip
2. Extract it to where you want Namrr to live
3. Run the following command in the Namrr directory

```
pip install -r requirements.txt
```

## Usage

To use Namrr, simply run it using the [run.sh](run.sh) script in the directory containing the season folders of your show.
Namrr will prompt you for an IMDb ID.  You can get this right from the IMDb website.
To find the IMDb ID of a show navigate to the IMDb page for the show and check the URL.

```
https://www.imdb.com/title/<IMDb_ID>/
```

After that Namrr will prompt you for a directory.  This should be the Directory containing all season folders for the show.
You can use Namrr even if you don't have all seasons of a show, it will simply skip any seasons that are not present in the directory you input.
I suggest having your season folders named according to [Jellyfin's official recommended naming scheme.](https://jellyfin.org/docs/general/server/media/shows/)
