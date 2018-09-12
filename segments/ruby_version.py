import subprocess
import os
from ..utils import ThreadedSegment


class Segment(ThreadedSegment):
    def add_to_powerline(self):
        ruby_version = os.getenv('RUBY_VERSION')
        if ruby_version is None:
            return

        bg = 148
        fg = 0
        self.powerline.append(' %s ' % ruby_version, fg, bg)
