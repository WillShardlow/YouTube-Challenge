"""A video player class."""

from .video_library import VideoLibrary
from .playback import PlayBack
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playback = PlayBack()
        self._num_videos = len(self._video_library.get_all_videos())

    def test(self):
        '''This is a function that I can edit to test different things
        but having all the various classes and methods etc. defined.'''

        print(self._video_library._videos)

    @staticmethod
    def tag_printer(tags):

        if tags == ():
            return '[]'
        else:
            tags_string = ''
            num_tags = len(tags)

            for i in range(num_tags-1):
                tags_string = tags_string + tags[i] + ' '
            tags_string = tags_string + tags[num_tags-1]

            return f'[{tags_string}]'

    @staticmethod
    def single_printer(video):
        return(f"{video.title} ({video.video_id}) {VideoPlayer.tag_printer(video.tags)}")

    def number_of_videos(self):
        """Returns number of videos"""
        #num_videos = len(self._video_library.get_all_videos())
        #print(f"{num_videos} videos in the library")
        # above^^ is what was already given but I've changed it

        print(f"{self._num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        list_videos = self._video_library.get_all_videos()
        list_videos.sort(key=lambda x: x.title)

        print("Here\'s a list of all available videos:")
        for i in range(self._num_videos):
            print(VideoPlayer.single_printer(list_videos[i]))

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        if self._video_library.get_video(video_id) is None:
            print("Cannot play video: Video does not exist")
        else:
            video = self._video_library.get_video(video_id)
            if self._playback.current_video() is not None:
                print(f"Stopping video: {self._playback.current_video()}")
            self._playback._video = video
            self._playback.play()
            print(f"Playing video: {self._playback.current_video()}")

    def stop_video(self):
        """Stops the current video."""

        if self._playback.current_video() is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self._playback.current_video()}")
            self._playback.stop()

    def play_random_video(self):
        """Plays a random video from the video library."""

        list_videos = self._video_library.get_all_videos()
        random_video = random.choice(list_videos)

        self.play_video(random_video.video_id)

    def pause_video(self):
        """Pauses the current video."""

        if self._playback.current_video() is None:
            print("Cannot pause video: No video is currently playing")
        elif self._playback._playback_state == "Paused":
            print(f"Video already paused: {self._playback.current_video()}")
        else:
            print(f"Pausing video: {self._playback.current_video()}")
            self._playback.pause()

    def continue_video(self):
        """Resumes playing the current video."""

        if self._playback.current_video() is None:
            print("Cannot continue video: No video is currently playing")
        elif self._playback._playback_state == "Playing":
            print("Cannot continue video: Video is not paused")
        else:
            print(f"Continuing video: {self._playback.current_video()}")
            self._playback.play()

    def show_playing(self):
        """Displays video currently playing."""

        current_video = self._playback._video

        if current_video is None:
            print("No video is currently playing")
        elif self._playback._playback_state == "Paused":
            print(f"Currently playing: {VideoPlayer.single_printer(current_video)} - PAUSED")
        else:
            print(f"Currently playing: {VideoPlayer.single_printer(current_video)}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
