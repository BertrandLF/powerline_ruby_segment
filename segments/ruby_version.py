import os

def add_ruby_version_segment():
    ruby_version = os.getenv('RUBY_VERSION')
    if ruby_version is None:
        return

    bg = 148
    fg = 0
    powerline.append(' %s ' % ruby_version, fg, bg)

add_ruby_version_segment()
