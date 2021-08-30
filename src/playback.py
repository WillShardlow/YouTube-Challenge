"""A playback class"""

from .video import Video


class PlayBack:
    """A class used to represent playback."""

    def __init__(self, video=None):  # optional argument so can open PlayBack without having to play a video
        self._video = video
        self._playback_state = None

    def current_video(self):
        if self._video is None:
            return None
        else:
            return self._video.title  # not .title() because video.title is not a method it is a property decorator

    def play(self):
        self._playback_state = "Playing"

    def pause(self):
        self._playback_state = "Paused"

    def stop(self):
        self._video = None
        self._playback_state = None

    def change_video(self, video):
        self._video = video


"""Video player takes video object from library, feeds video object into playback """
""""""
