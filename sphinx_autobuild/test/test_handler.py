from sphinx_autobuild import _WatchdogHandler
from collections import namedtuple


Call = namedtuple('Call', ['args', 'kwargs'])


class CallRecorder(object):
    def __init__(self, retval=None):
        self.calls = []
        self.retval = retval

    def __call__(self, *args, **kwargs):
        self.calls.append(Call(args, kwargs))
        return self.retval


class Stub(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def test_file_action():
    watcher = object()

    action = CallRecorder()
    event = Stub(is_directory=False, src_path=object())

    h = _WatchdogHandler(watcher, action)
    h.on_any_event(event)

    assert len(action.calls) == 1

    call = action.calls[0]

    assert not call.kwargs
    assert len(call.args) == 2
    assert call.args[0] is watcher
    assert call.args[1] is event.src_path


def test_dir_action():
    watcher = object()

    action = CallRecorder()
    event = Stub(is_directory=True, src_path=object())

    h = _WatchdogHandler(watcher, action)
    h.on_any_event(event)

    assert not action.calls
