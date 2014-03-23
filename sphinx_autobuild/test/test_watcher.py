from sphinx_autobuild import LivereloadWatchdogWatcher
from livereload import Server


class TestWatchdogWatcher(object):
    def test_watch(self):
        watcher = LivereloadWatchdogWatcher()
        server = Server(watcher=watcher)
