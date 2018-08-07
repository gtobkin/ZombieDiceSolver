# Represents game state in between actual turns.
class InterTurnGameState():
    def __init__(self, scores, nextPlayer):
        self.scores = scores
        self.nextPlayer = nextPlayer
    
    def __str__(self):
        # e.g. [3, 11, 7, 5], 1 => "[  3 ,>11<,  7 ,  1 ]"
        outstr = "["
        for score in self.scores[:-1]:
            outstr += format(score, '>3')   # e.g. "  4"
            outstr += ' ,'
        outstr += format(self.scores[-1], '>3')
        outstr += ' ]'
        outstr = (outstr[:(1+5*nextPlayer)] + '>' + outstr[(2+5*nextPlayer):(4+5*nextPlayer)]
                + '<' + outstr[(5+5*nextPlayer):])
        return outstr

class IntraTurnGameState():
    def __init__(self):
        self.brains = None
        self.blasts = None
        self.hand   = None
        self.cup    = None

