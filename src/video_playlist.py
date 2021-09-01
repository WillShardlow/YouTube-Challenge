"""A video playlist class."""

from .video import Video


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_name: str):
        self._name = playlist_name
        self._videos = []                  # list of video objects in the playlist

    @property
    def name(self) -> str:
        """Returns the name of a playlist."""
        return self._name

    def change_name(self, new_name):
        self._name = new_name

    def add_video(self, video):
        self._videos.append(video)

    def remove_video(self, video):
        self._videos.remove(video)

    def clear(self):
        self._videos = []

    def get_all_videos(self):
        return self._videos
