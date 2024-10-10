class Scoreboard:

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.scoreTeam1 = 0
        self.scoreTeam2 = 0
        self.activeTeam = 1


    def recordPlay(self, pointScored):
        if pointScored ==0:
            self.activeTeam += 1
        else:
            if self.activeTeam % 2 == 1:
                self.scoreTeam1 += pointScored
            else:
                self.scoreTeam2 += pointScored

    def getWinningTeam(self):
        if self.scoreTeam1>self.scoreTeam2:
            return self.team1
        elif self.scoreTeam1<self.scoreTeam2:
            return self.team2
        elif self.scoreTeam1 == self.scoreTeam2:
            return ("")

