

import os
from abc import ABC
from abc import abstractmethod


class PlayerBusy(Exception):
    def __init__(self, player, now_playing):
        self.player = player
        self.now_playing = now_playing

    def __repr__(self):
        return "<{0} Busy, Now Playing {1}>" \
               "".format(self.player, self.now_playing)


class MediaPlayerBase(ABC):
    _extensions = []
    _is_visual = True

    def __init__(self, actual):
        self._actual = actual
        self._player = None

    def is_visual(self):
        return self._is_visual

    @property
    def actual(self):
        return self._actual

    def check_support(self, filepath):
        if self._extensions[0] == '*':
            return True
        return os.path.splitext(filepath)[1].lower() in self._extensions

    @abstractmethod
    def _play(self, filepath, **kwargs):
        pass

    def play(self, filepath, **kwargs):
        if self._player:
            raise PlayerBusy(self, self._player)
        return self._play(filepath, **kwargs)

    @abstractmethod
    def _stop(self):
        pass

    def stop(self):
        self._stop()
        self._player = None
