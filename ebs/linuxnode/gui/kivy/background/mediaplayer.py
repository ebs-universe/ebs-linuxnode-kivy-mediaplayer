

from kivy.uix.boxlayout import BoxLayout
from ebs.linuxnode.gui.kivy.background.base import BackgroundProviderBase
from ebs.linuxnode.gui.kivy.mediaplayer.manager import KivyMediaPlayerManager
from ebs.linuxnode.mediaplayer.manager import BACKGROUND


class MediaPlayerBackgroundProvider(BackgroundProviderBase):
    def __init__(self, actual):
        super(MediaPlayerBackgroundProvider, self).__init__(actual)
        self._mpm = KivyMediaPlayerManager(actual, BACKGROUND, self.widget)
        self.actual.install_media_player_manager(self._mpm)

    def check_support(self, target):
        if not target or not isinstance(target, str):
            rv = False
        else:
            rv = self._mpm.check_supports(target)
        return rv

    def play(self, target, **kwargs):
        self._mpm.play(target, **kwargs)
        return self._widget

    def stop(self):
        self._mpm.stop()

    def pause(self):
        pass

    def resume(self):
        pass

    @property
    def widget(self):
        if not self._widget:
            self._widget = BoxLayout()
        return self._widget
