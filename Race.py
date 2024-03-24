from graphics import *
from Dice import *

class Horse:
    def __init__(self, speed, y, image, win):
        self.speed = speed
        self.x = 0
        self.y = y
        self.image = image
        self.win = win

    def move(self):
        horse_movement = Dice(self.speed)
        self.x += horse_movement.roll()

    def draw(self):
        self.image.draw_at_pos(self.win, self.x, self.y)

    def crossed_finish_line(self, finish_line):
        if self.x >= 600:
            return True
        return False

def main():
    win = GraphWin("Churchill Downs", 700, 350, autoflush=False) #Churchill Downs is a famous race track in my home state
    win.setBackground('green')

    #creating the horses
    image1 = Image(Point(0, 150), "horse6.png")
    image2 = Image(Point(0, 200), "horse8.png")
    horse6 = Horse(10, 150, image1, win) #top horse
    horse8 = Horse(10, 200, image2, win) #bottom horse

    #running the race through a loop
    while horse6.crossed_finish_line(600) == False and horse8.crossed_finish_line(600) == False :
        win.clear_win()

        #drawing the finish line
        finish_line = Line(Point(600, 0), Point(600, 350))
        finish_line.setWidth(15)
        finish_line.setOutline('white')
        finish_line.draw(win)

        #making the horses move
        horse6.move()
        horse8.move()
        horse6.draw()
        horse8.draw()

        win.update()

        #printing results of the race
        if horse6.crossed_finish_line(600) == True and horse8.crossed_finish_line(600) == True:
            print("It's a tie!")
        elif horse6.crossed_finish_line(600) == True:
            print("Horse #6 is the winner!")
        elif horse8.crossed_finish_line(600) == True:
            print("Horse #8 is the winner!")


    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()

