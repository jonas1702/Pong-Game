import tkinter as tk
import time
import random

class Ball:
    def __init__(self, canvas, x, y, x_velocity, y_velocity):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.size = 8
        self.ball = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill="#000")

    def move(self, dt, paddle1, paddle2):
        print(int(self.x))
        if (self.x + self.size > self.canvas.winfo_width()):
            self.start()
        
        if (self.x < 0):
            self.start()
            
        if (self.y < 0):
            self.y = 0
            self.y_velocity *= -1
    
        if (self.y + self.size > self.canvas.winfo_width()):
            self.y = self.canvas.winfo_width() - self.size
            self.y_velocity *= -1

        if (self.x < paddle1.x + paddle1.width and self.y < paddle1.y + paddle1.height and self.y > paddle1.y):
            self.x = paddle1.x + paddle1.width
            self.x_velocity *= -1

        if (self.x > paddle2.x and self.y < paddle2.y + paddle2.height and self.y > paddle2.y):
            self.x = paddle2.x
            self.x_velocity *= -1

        self.x += self.x_velocity * dt
        self.y += self.y_velocity * dt
        self.canvas.move(self.ball, self.x_velocity * dt, self.y_velocity * dt)
    
    def start(self):
        self.x = self.canvas.winfo_width() / 2
        self.y = self.canvas.winfo_height() / 2

        self.canvas.moveto(self.ball, self.x, self.y)

class Paddle:
    def __init__(self, canvas, x, y, speed):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 8
        self.height = 40
        self.move_up = False
        self.move_down = False
        self.paddle = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill='#000')
    
    def move(self, dt):
        if self.move_up and self.y > 0:
            self.y -= self.speed * dt
            self.canvas.move(self.paddle, 0, -self.speed * dt)
        if self.move_down and self.y + self.height < self.canvas.winfo_height():
            self.y += self.speed * dt
            self.canvas.move(self.paddle, 0, self.speed * dt)
            
def main():
    root = tk.Tk()
    root.focus_set()
    root.title("Pong")

    # create the canvas
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.config(highlightthickness=0, bd=0)
    canvas.pack()
    root.update()

    # create the ball
    ball = Ball(canvas, 200, 200, random.randint(70, 90), random.randint(70, 90))

    #create paddle
    paddle1 = Paddle(canvas, 30, 180, 100)
    paddle2 = Paddle(canvas, canvas.winfo_width() -30, 180, 100)
    
    # create the main loop  
    def updateGame():
        current_time = time.time()
        dt = current_time - updateGame.prev_time

        ball.move(dt, paddle1, paddle2)
        paddle1.move(dt)
        paddle2.move(dt)

        root.update()

        updateGame.prev_time = current_time   

        root.after(1000 // 180, updateGame)

    def on_key_press(event):
        if event.keysym == 'w':
            paddle1.move_up = True
        elif event.keysym == 's':
            paddle1.move_up = False
            paddle1.move_down = True
        elif event.keysym == 'Up':
            paddle2.move_up = True
        elif event.keysym == 'Down':
            paddle2.move_up = False
            paddle2.move_down = True

    def on_key_release(event):
        if event.keysym == 'w':
            paddle1.move_up = False
        elif event.keysym == 's':
            paddle1.move_down = False
        elif event.keysym == 'Up':
            paddle2.move_up = False
        elif event.keysym == 'Down':
            paddle2.move_down = False

    updateGame.prev_time  = time.time()

    root.bind("<KeyPress>", on_key_press)
    root.bind("<KeyRelease>", on_key_release)
    
    updateGame()
    root.resizable(False,False)
    root.mainloop()

if __name__ == '__main__':
    main()