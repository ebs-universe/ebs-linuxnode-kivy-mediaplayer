

from twisted.internet import reactor
from ebs.linuxnode.gui.kivy.core.basenode import BaseIoTNodeGui
from ebs.linuxnode.gui.kivy.mediaplayer.mixin import MediaPlayerGuiMixin


class ExampleNode(MediaPlayerGuiMixin, BaseIoTNodeGui):
    def start(self):
        print("Installing")
        self.install()
        super(ExampleNode, self).start()
        reactor.run()

    def stop(self):
        super(ExampleNode, self).stop()
        reactor.stop()
