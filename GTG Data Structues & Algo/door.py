door_is_closed = True
door_is_locked = True

def unlock_door():
    print("Unlocking...")
def open_door():
    print("Opening...")
def advance():
    print("In!")


if door_is_closed:
    if door_is_locked:
        unlock_door()
    open_door()
advance()