#CK

# | Player()
# |-------------------------------------------------------------------
# | The player class. Takes care of the player's score, and score
# | title, and manages the movement of the player's paddle
# |-----------------------------------------------
class Player():
    def __init__(self, paddle, scoreTitle):
        self.score = 0
        self.paddle = paddle
        self.scoreTitle = scoreTitle

    # | increaseScore()
    # |----------------------------------
    # | Adds one to the player's score
    # |---------------------------
    def increaseScore(self):
        self.score += 1
        self.updateScoreTitle()

    # | updateScoreTitle()
    # |-------------------------------------------------
    # | Changes the text of the player's score title,
    # | to allow it to match the player's score
    # |-------------------------------------
    def updateScoreTitle(self):
        self.scoreTitle.changeText(str(self.score))

    # | movePaddleUp()
    # |--------------------------------
    # | Moves the player's paddle up
    # |--------------------------
    def movePaddleUp(self):
        self.paddle.moveUp()

    # | movePaddleDown()
    # |---------------------------------
    # | Moves the player's paddle down
    # |---------------------------
    def movePaddleDown(self):
        self.paddle.moveDown()