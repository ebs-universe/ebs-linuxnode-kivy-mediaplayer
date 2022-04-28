

from twisted.internet import reactor
from ebs.linuxnode.gui.kivy.core.basenode import BaseIoTNodeGui
from ebs.linuxnode.gui.kivy.mediaplayer.mixin import MediaPlayerGuiMixin


class ExampleNode(MediaPlayerGuiMixin, BaseIoTNodeGui):
    def start(self):
        reactor.callLater(5, self.mediaview.play, 'image.jpg', duration=10)
        reactor.callLater(20, self.mediaview.play, 'video.mp4')
        reactor.callLater(55, self.mediaview.play, 'pdf.pdf', duration=30)
        super(ExampleNode, self).start()
