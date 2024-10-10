from scoreboard import Scoreboard

scoreFile = open("Scoreboard.txt", "r")
scores = scoreFile.readlines()
finalWinningTeam = []
winningTeamNames = []
winningTeamScore = []
num = 0

for line in scores:
    teamNameChars = []
    lineScore = []
    team1 = []
    team2 = []
    activeTeam = 0
    for character in line:
        if character.isalpha():
            teamNameChars.append(character)
        elif character.isnumeric():
            lineScore.append(character)
    for char_team in teamNameChars:
        if char_team.isupper():
            activeTeam += 1
        if activeTeam % 2 == 1:
            team1.append(char_team)
        if activeTeam %2 ==0:
            team2.append(char_team)
    team1Name = "".join(team1)
    team2Name = "".join(team2)
    tempScores = Scoreboard(team1Name, team2Name)
    for tempScore in lineScore:
        tempScores.recordPlay(int(tempScore))
    tempWinningTeam = tempScores.getWinningTeam()
    if tempWinningTeam != "":
        finalWinningTeam.append(tempWinningTeam)

for winningTeam in finalWinningTeam:
    doNotAppend = False
    for teamName in winningTeamNames:
        if winningTeam == teamName:
            doNotAppend = True
    if not doNotAppend:
        winningTeamNames.append(winningTeam)
        winningTeamScore.append(0)
    for teamName1 in winningTeamNames:
        if winningTeam == teamName1:
            pos = winningTeamNames.index(winningTeam)
            winningTeamScore[pos] += 1

sortedWinningTeamScore = sorted(winningTeamScore, reverse=True)
sortedWinningTeamName = []

for score in sortedWinningTeamScore:
    winningTeamScore.index(score)
    sortedWinningTeamName.append(winningTeamNames[winningTeamScore.index(score)])

while num != (len(winningTeamScore)):
    print(str(num + 1) + ". " + str(sortedWinningTeamName[num]) + " - " + str(sortedWinningTeamScore[num]))
    num += 1







