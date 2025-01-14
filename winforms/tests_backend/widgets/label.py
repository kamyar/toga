import System.Windows.Forms

from .base import SimpleProbe


class LabelProbe(SimpleProbe):
    native_class = System.Windows.Forms.Label

    @property
    def text(self):
        return self.native.Text
