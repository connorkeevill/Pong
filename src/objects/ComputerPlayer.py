#CK

from objects.Player import Player


class ComputerPlayer(Player):
    # | Call the superclass __init__() method
    def __init__(self, paddle, scoreTitle, ball):
        Player.__init__(self, paddle, scoreTitle)
        self.ball = ball

    # | movePaddle()
    # |----------------------------------------
    # | Attempts to put the paddle inline with
    # | the ball that the player is tracking
    # |----------------------------------
    def movePaddle(self):
        # | If paddle is above the ball
        if self.paddle.rect.bottom < self.ball.rect.centery:
            self.movePaddleDown()
        # | If paddle is below the ball
        elif self.paddle.rect.top > self.ball.rect.centery:
            self.movePaddleUp()