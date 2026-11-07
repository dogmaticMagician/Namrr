from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="Episode API")

TVMAZE_API = "https://api.tvmaze.com"

@app.get("/episodes/{imdb_id}")
def get_episodes(imdb_id: str):

    # Find the TV show using its IMDb ID
    response = requests.get(
        f"{TVMAZE_API}/lookup/shows",
        params={"imdb": imdb_id},
        timeout=15
    )

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Show not found")

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="TVmaze API error")

    show = response.json()

    # Retrieve all episodes
    episode_response = requests.get(
        f"{TVMAZE_API}/shows/{show['id']}/episodes",
        timeout=15
    )

    if episode_response.status_code != 200:
        raise HTTPException(status_code=502, detail="Could not retrieve episodes")

    episodes = episode_response.json()

    # Organize episodes by season
    seasons = {}

    for episode in episodes:
        season = episode["season"]
        number = episode["number"]
        name = episode["name"]

        if season is None or number is None:
            continue

        season_key = str(season)
        episode_key = f"S{season:02d}E{number:02d}"

        if season_key not in seasons:
            seasons[season_key] = {}

        seasons[season_key][episode_key] = name

    return {
        "imdb_id": imdb_id,
        "series_name": show["name"],
        "seasons": seasons
    }