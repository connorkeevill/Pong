#CK

class Player():
    def __init__(self, paddle, scoreTitle):
        self.score = 0
        self.paddle = paddle
        self.scoreTitle = scoreTitle

    def score(self):
        self.score += 1
        self.updateScoreTitle()

    def updateScoreTitle(self):
        self.scoreTitle.changeText(self.score)

    def movePaddleUp(self):
        self.paddle.moveUp()

    def movePaddleDown(self):
        self.paddle.moveDown()