from collector import Youtube
from enum import Enum
from datetime import date


class Music:
    def __init__(self, name: str,
                 music_video: None | Youtube = None,
                 spotify: str | None = None,
                 youtube: str | None = None,
                 melon: str | None = None):
        self.name = name
        self.music_video = music_video
        self.spotify = spotify if spotify is not None else ""  # todo
        self.youtube = youtube if youtube is not None else ""  # todo
        self.melon = melon if melon is not None else ""  # todo


class AlbumType(Enum):
    SINGLE = 0,
    DIGITAL_SINGLE = 1,
    PRERELEASE = 2,
    EP = 3,
    ALBUM = 4


class Country(Enum):
    KOR = 1,
    JPN = 2,
    USA = 3


class Album:
    def __init__(self, name: str, type: AlbumType, cover: str,
                 target: Country = Country.KOR):
        self.name = name
        self.type = type
        self.poster = cover
        self.target = target

        self.titles: list[Music] = []
        self.b_sides: list[Music] = []

    def title(self, *args: Music):
        for e in args:
            self.titles.append(e)

    def b_side(self, *args: Music):
        for e in args:
            self.b_sides.append(e)


class Era:
    def __init__(self, album: Album, starts_in: date):
        self.album = album
        self.start_date = starts_in


eras = []

# todo: 일일히 추가하는게 아니라 spotify api를 사용하면 쉬울 것 같음
#  - 그리고 멜론 api를 응용해서 다양한 통계를 내는거지

ITz_Different = Album("IT'z Different",
                      type=AlbumType.DIGITAL_SINGLE,
                      cover="https://en.wikipedia.org/wiki/It%27z_Different#/media/File:Itzy_-_It'z_Different.png")

ITz_Different.title(Music('달라달라', music_video="https://youtu.be/pNfTK39k55U"))
ITz_Different.b_side(Music('WANT IT?', youtube="https://www.youtube.com/watch?v=UMfJoFnR4Ew"))
