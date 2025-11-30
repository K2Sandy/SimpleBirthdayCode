import turtle as t
import time, random, threading
try:
    import winsound
except ImportError:
    winsound = None

# Setup screen
screen = t.Screen()
screen.bgcolor("black")
screen.title("Happy Birthday Mami!")
screen.tracer(0)

# Heart turtle
pen = t.Turtle()
pen.hideturtle()
pen.pensize(3)
pen.color("red")

# Text turtle
text_turtle = t.Turtle()
text_turtle.hideturtle()
text_turtle.penup()

# Sparkle turtle
sparkle = t.Turtle()
sparkle.hideturtle()
sparkle.penup()

# Mouse-follow heart
follower = t.Turtle()
follower.hideturtle()
follower.color("pink")

messages = [
    "Selamat Ulang Tahun Mami.",
    "Semoga semua mimpi Mami terkabul",
    "Semoga Mami Terus Banyak Rezeki",
    "Makasih Dah Jagain Adek ma Rara ",
    "We Love You So Much, Mami! 💖",
]

msg_index = 0

def draw_heart(scale=1.0, color="red"):
    pen.color(color)
    pen.fillcolor(color)
    pen.penup()
    pen.goto(0, -100 * scale)
    pen.setheading(150)
    pen.pendown()
    pen.begin_fill()
    pen.forward(180 * scale)
    pen.circle(-90 * scale, 180)
    pen.setheading(60)
    pen.circle(-90 * scale, 180)
    pen.forward(180 * scale)
    pen.end_fill()

def glow_heart():
    colors = ["#ff9999", "#ff4d4d", "red"]
    sizes = [1.1, 1.05, 1.0]
    for c, s in zip(colors, sizes):
        draw_heart(s, c)

def show_message(text):
    text_turtle.clear()
    # shadow
    text_turtle.goto(-2, -152)
    text_turtle.color("black")
    text_turtle.write(text, align="left", font=("Lucida Handwriting", 26, "bold"))
    # main
    text_turtle.goto(0, -150)
    text_turtle.color("white")
    text_turtle.write(text, align="left", font=("Lucida Handwriting", 26, "bold"))

def typing_message(text):
    text_turtle.clear()
    for i in range(1, len(text)+1):
        show_message(text[:i])
        screen.update()
        time.sleep(0.1)

def sparkle_effect():
    sparkle.clear()
    sparkle.color(random.choice(["white", "pink"]))
    sparkle.goto(random.randint(-150, 150), random.randint(-50, 200))
    sparkle.dot(random.randint(3, 7))

def follower_heart(x, y):
    follower.clear()
    follower.penup()
    follower.goto(x, y)
    follower.pendown()
    follower.color("pink")
    follower.begin_fill()
    follower.setheading(150)
    follower.forward(10)
    follower.circle(-5, 180)
    follower.setheading(60)
    follower.circle(-5, 180)
    follower.forward(10)
    follower.end_fill()

def heartbeat(scale_cycle=[1.0, 1.05, 0.95, 1.0], idx=0):
    pen.clear()
    glow_heart()
    draw_heart(scale_cycle[idx])
    sparkle_effect()
    screen.update()
    screen.ontimer(lambda: heartbeat(scale_cycle, (idx+1)%len(scale_cycle)), 300)

def next_message(x=None, y=None):
    global msg_index
    msg_index = (msg_index + 1) % len(messages)
    typing_message(messages[msg_index])
    if winsound:
        threading.Thread(target=lambda: winsound.Beep(500,200)).start()

def setup():
    screen.tracer(1)   
    pen.speed(1)      
    draw_heart()
    show_message(messages[msg_index])
    time.sleep(0.5)

    pen.speed(0)
    screen.tracer(0)
    heartbeat()

screen.onclick(next_message)
screen.listen()
screen.onkey(next_message, "space")
screen.onscreenclick(follower_heart, 1)

setup()
t.done()
