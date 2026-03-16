"""
This module contains the Song class.
"""

import re
from unidecode import unidecode


class Song:
    """
    A class that represents a song.

    Attributes:
        title (str): The title of the song.
        artist (str): The artist of the song.
        duration (int): The duration of the song in seconds.
        track_id (str): The ID of the song.
        owner_id (str): The ID of the song's owner.
        url (str): The URL of the song.
    """

    def __init__(
        self,
        title: str,
        artist: str,
        duration: int,
        track_id: str,
        owner_id: str,
        url: str = "",
    ) -> None:
        """
        Initializes a Song object.

        Args:
            title (str): The title of the song.
            artist (str): The artist of the song.
            duration (int): The duration of the song in seconds.
            track_id (str): The ID of the song.
            owner_id (str): The ID of the song's owner.
            url (str): The URL of the song.
        """
        self.title = title
        self.artist = artist
        self.duration = duration
        self.track_id = track_id
        self.owner_id = owner_id
        self.url = url

        def safe_format(string):
            pattern = r"[^a-zA-Zа-яА-ЯёЁ0-9!@#№\$;%\^&\(\)\[\]\{\}~`',\.\-+\s]"
            # unidecode everything except latin, cyrillic and special symbols
            string = re.sub(pattern, lambda x: unidecode(x.group()), string)
            # remove everything except latin, cyrillic and special symbols
            return re.sub(pattern, "", string)

        self._title_safe = safe_format(self.title)
        self._artist_safe = safe_format(self.artist)

    def __str__(self):
        return self.to_string(safe=True)

    def to_string(self, safe: bool = False):
        return f"{self._title_safe if safe else self.title} - {self._artist_safe if safe else self.artist}"

    def to_dict(self) -> dict:
        """
        Converts the song to a dictionary.

        Returns:
            dict: The song as a dictionary.
        """
        return self.__dict__

    def to_safe(self):
        """
        Deprecated
        """
        pass

    @classmethod
    def from_json(cls, item) -> "Song":
        """
        Creates a Song object from a JSON object.

        Args:
            item (dict): A JSON object.

        Returns:
            Song: A Song object.
        """
        title = str(item["title"])
        artist = str(item["artist"])
        duration = int(item["duration"])
        track_id = str(item["id"])
        owner_id = str(item["owner_id"])
        url = str(item["url"])
        song = cls(title, artist, duration, track_id, owner_id, url)
        return song
