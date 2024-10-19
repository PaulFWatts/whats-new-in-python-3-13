import sys

frame_locals = None
[frame_locals := sys._getframe().f_locals for number in range(3)]
print(frame_locals)
print("number" in frame_locals)  # False in 3.13, True in 3.12

frame_locals = None
[frame_locals := locals() for number in range(3)]
print(frame_locals)
print("number" in frame_locals)  # True in 3.13, True in 3.12


def locals_func():
    frame_locals = None
    [frame_locals := locals() for number in range(3)]
    return frame_locals


print(locals_func())


def f_frame():
    x = 1
    sys._getframe().f_locals["x"] = 2
    print(x)


f_frame()  # 2 in 3.13, 1 in 3.12


def f_locals():
    x = 1
    locals()["x"] = 2
    print(x)


f_locals()  # 1 in 3.13, 1 in 3.12
