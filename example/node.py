

from twisted.internet import reactor
from ebs.linuxnode.gui.kivy.core.basenode import BaseIoTNodeGui
from ebs.linuxnode.gui.kivy.mediaplayer.mixin import MediaPlayerGuiMixin
from kivy_garden.ebs.clocks.digital import SimpleDigitalClock


class ExampleNode(MediaPlayerGuiMixin, BaseIoTNodeGui):
    def _mediaplayer_example(self):
        reactor.callLater(5, self.mediaview.play, 'image.jpg', duration=10)
        reactor.callLater(20, self.mediaview.play, 'video.mp4')
        reactor.callLater(55, self.mediaview.play, 'pdf.pdf', duration=30)

    def _set_bg(self, target):
        self.gui_bg = target

    @property
    def clock(self):
        return SimpleDigitalClock()

    def _background_example(self):
        reactor.callLater(10, self._set_bg, '1.0:0.5:0.5:1.0')
        reactor.callLater(20, self._set_bg, 'image.jpg')
        reactor.callLater(30, self._set_bg, '0.5:1.0:0.5:1.0')
        reactor.callLater(40, self._set_bg, None)
        # Install kivy_garden.ebs.clocks
        reactor.callLater(50, self._set_bg, 'structured:clock')
        reactor.callLater(60, self._set_bg, 'video.mp4')
        reactor.callLater(70, self._set_bg, 'pdf.pdf')

    def start(self):
        super(ExampleNode, self).start()
        self._background_example()
