


class Robot:
    def __init__(self, name, x = 0, y = 0, dir = 1):
        self.name = name
        self.x = x
        self.y = y
        self.dir = dir
        self.img = None
        self.moveMult = 0


    def nameFile(self):
        return f"{str(self.name)}{str(self.dir)}.png"

    def turnLeft(self):
        self.dir -=1
        if self.dir == -1:
            self.dir = 3

    def turnRight(self):
        self.dir +=1
        if self.dir == 4:
            self.dir = 0

    def moveRight(self):
        self.x += 46

        if self.y > 460:
            self.y = 460

        if self.x > 460:
            self.x = 460

        if self.y < 0:
            self.y = 0

        if self.x < 0:
            self.x = 0
    def moveDown(self):
        self.y += 46

        if self.y > 460:
            self.y = 460

        if self.x > 460:
            self.x = 460

        if self.y < 0:
            self.y = 0

        if self.x < 0:
            self.x = 0
    def moveLeft(self):
        self.x -= 46

        if self.y > 460:
            self.y = 460

        if self.x > 460:
            self.x = 460

        if self.y < 0:
            self.y = 0

        if self.x < 0:
            self.x = 0
    def moveUp(self):
        self.y -= 46

        if self.y > 460:
            self.y = 460

        if self.x > 460:
            self.x = 460

        if self.y < 0:
            self.y = 0

        if self.x < 0:
            self.x = 0

    def moveForward(self):
        if (self.dir == 0 ):
            self.moveUp()

        if (self.dir == 1):
            self.moveRight()

        if (self.dir == 2):
            self.moveDown()

        if (self.dir == 3):
            self.moveLeft()

    def moveBackward(self):
        if(self.dir == 0):
            self.moveDown()

        if(self.dir == 1):
            self.moveLeft()

        if(self.dir == 2):
            self.moveUp()

        if(self.dir == 3):
            self.moveRight()


if __name__ == "__main__":
    r2d2 = Robot('R2D2')

    while True:
        choice = input("Left or Right")
        if choice == "L":
            r2d2.turnLeft()

        if choice == "R":
            r2d2.turnRight()

        print(r2d2.nameFile())
        print()
