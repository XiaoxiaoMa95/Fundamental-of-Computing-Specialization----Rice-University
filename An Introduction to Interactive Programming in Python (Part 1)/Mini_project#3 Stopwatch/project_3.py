# template for "Stopwatch: The Game"

http://www.codeskulptor.org/#user47_p6XyTES3DllRMCW.py

import simplegui

# define global variables
t = 0
time = 0
total_stops = 0
successful_stops = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global time, t
    seconds = int((time % 600) // 10)
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)
    t = str(time // 600) + ":" + seconds + "." + str((time % 600) % 10)
    return t


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()


def stop():
    global total_stops, successful_stops
    if timer.is_running():
        timer.stop()
        total_stops += 1
        if t[-1] == '0':
            successful_stops += 1


def reset():
    global time, total_stops, successful_stops
    time = 0
    total_stops, successful_stops = 0,0


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1


# define draw handler
def draw_handler(canvas):
    format()
    canvas.draw_text(t, [150, 150], 40, "White")
    canvas.draw_text(str(successful_stops) + '/' + str(total_stops), [300, 40], 20, "white")


# create frame
frame = simplegui.create_frame("Stopwatch", 400, 300)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
