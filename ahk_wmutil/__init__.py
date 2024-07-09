import wmutil as _wmutil
from ahk import AHK
from ahk import AsyncAHK
from ahk import AsyncWindow
from ahk import Window
from ahk.extensions import Extension

wmutil_extension = Extension()

__all__ = ['wmutil_extension']


@wmutil_extension.register_window_method
def get_monitor(self: Window) -> _wmutil.Monitor:
    """
    retrieves a handle to the display monitor that has the largest area of intersection with
     the bounding rectangle of a specified window. If the window does not intersect any display monitor,
     the return value will be that of the primary monitor.

    """
    hwnd = int(self.id, 0)
    return _wmutil.get_window_monitor(hwnd)


@wmutil_extension.register_window_method
async def get_monitor(self: AsyncWindow) -> _wmutil.Monitor:
    """
    retrieves a handle to the display monitor that has the largest area of intersection with
     the bounding rectangle of a specified window. If the window does not intersect any display monitor,
     the return value will be that of the primary monitor.

    """
    hwnd = int(self.id, 0)
    return _wmutil.get_window_monitor(hwnd)


@wmutil_extension.register
def monitor_from_mouse_position(self: AHK) -> _wmutil.Monitor:
    mouse_position = self.get_mouse_position(coord_mode='Screen')
    return _wmutil.get_monitor_from_point(*mouse_position)


@wmutil_extension.register
async def monitor_from_mouse_position(self: AsyncAHK) -> _wmutil.Monitor:
    mouse_position = await self.get_mouse_position(coord_mode='Screen')
    return _wmutil.get_monitor_from_point(*mouse_position)


@wmutil_extension.register_window_method
def move_to_monitor(
    self: Window,
    monitor: _wmutil.Monitor,
    *,
    x: int = 0,
    y: int = 0,
    size_to_monitor: bool = False,
    width: int | None = None,
    height: int | None = None
) -> None:
    """
    Move the window to a specific monitor.

    :param monitor: the monitor to move the window to
    :param x: x-offset where to place the window within the monitor. By default, the window will be placed to the left-most side of the monitor.
    :param y: y-offset where to place the window within the monitor. By default, the window will be placed at the top-most position of the monitor.
    :param size_to_monitor: when ``True``, sets the size of the window to fill the monitor, otherwise, retains the window's current size (unless the ``width`` or ``height`` arguments are also provided)
    :param width: resize the window to this width when it is moved. This parameter is mutually exclusive with ``size_to_monitor``. If not specified, the window width will not change.
    :param height: resize the window to this height when it is moved. This parameter is mutually exclusive with ``size_to_monitor`` If not specified, the window height will not change
    """

    dest_x, dest_y = monitor.position
    if x:
        dest_x += x
    if y:
        dest_y += y
    if size_to_monitor:
        if height or width:
            raise TypeError("The 'height' and 'width' parameters are mutually exclusive with 'size_to_monitor'")
        width, height = monitor.size
    self.move(dest_x, dest_y, width=width, height=height)
    return None


@wmutil_extension.register_window_method
async def move_to_monitor(
    self: AsyncWindow,
    monitor: _wmutil.Monitor,
    *,
    x: int = 0,
    y: int = 0,
    size_to_monitor: bool = False,
    width: int | None = None,
    height: int | None = None
) -> None:
    """
    Move the window to a specific monitor.

    :param monitor: the monitor to move the window to
    :param x: x-offset where to place the window within the monitor. By default, the window will be placed to the left-most side of the monitor.
    :param y: y-offset where to place the window within the monitor. By default, the window will be placed at the top-most position of the monitor.
    :param size_to_monitor: when ``True``, sets the size of the window to fill the monitor, otherwise, retains the window's current size (unless the ``width`` or ``height`` arguments are also provided)
    :param width: resize the window to this width when it is moved. This parameter is mutually exclusive with ``size_to_monitor``. If not specified, the window width will not change.
    :param height: resize the window to this height when it is moved. This parameter is mutually exclusive with ``size_to_monitor`` If not specified, the window height will not change
    """

    dest_x, dest_y = monitor.position
    if x:
        dest_x += x
    if y:
        dest_y += y

    if size_to_monitor:
        if height or width:
            raise TypeError("The 'height' and 'width' parameters are mutually exclusive with 'size_to_monitor'")
        width, height = monitor.size
    await self.move(dest_x, dest_y, width=width, height=height)
    return None
