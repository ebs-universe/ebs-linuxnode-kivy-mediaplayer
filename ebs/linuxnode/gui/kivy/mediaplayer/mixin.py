

from kivy_garden.ebs.core.colors import ColorBoxLayout
from ebs.linuxnode.gui.kivy.core.basenode import BaseIoTNodeGui
from ebs.linuxnode.mediaplayer.mixin import MediaPlayerCoreMixin

from .players.video import VideoPlayer
from .players.image import ImagePlayer
from .players.pdf import PDFPlayer


class MediaPlayerGuiMixin(MediaPlayerCoreMixin, BaseIoTNodeGui):
    def __init__(self, *args, **kwargs):
        super(MediaPlayerGuiMixin, self).__init__(*args, **kwargs)
        self._gui_mediaview = None

    def _install_builtin_players(self):
        super(MediaPlayerGuiMixin, self)._install_builtin_players()
        self.install_player(VideoPlayer)
        self.install_player(PDFPlayer)
        self.install_player(ImagePlayer)

    def media_play(self, content, duration=None, **kwargs):
        self.gui_bg_pause()
        deferred = super(MediaPlayerGuiMixin, self).media_play(content, duration=duration, **kwargs)
        self.gui_mediaview.make_opaque()
        self.gui_mediaview.add_widget(self._media_playing)
        return deferred

    def media_stop(self, forced=False):
        self.gui_mediaview.clear_widgets()
        super(MediaPlayerGuiMixin, self).media_stop(forced=forced)

        def _resume_bg():
            if not self._mediaplayer_now_playing:
                self.gui_bg_resume()
                self.gui_mediaview.make_transparent()
        self.reactor.callLater(0.1, _resume_bg)

    def stop(self):
        super(MediaPlayerGuiMixin, self).stop()

    @property
    def gui_mediaview(self):
        if self._gui_mediaview is None:
            self._gui_mediaview = ColorBoxLayout(bgcolor=(0, 0, 0, 0))
            self.gui_main_content.add_widget(self._gui_mediaview)
        return self._gui_mediaview

    def gui_setup(self):
        gui = super(MediaPlayerGuiMixin, self).gui_setup()
        _ = self.gui_mediaview
        return gui
