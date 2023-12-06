import random

class ChessPlayer:
    def __init__(self,name, age, elo, tenacity, isBoring):
        self.name = name
        self.age = age
        self.elo = elo
        #self.rating = rating
        self.tenacity = tenacity
        self.isBoring = isBoring
        self.tournament_score = 0
        

def simulateMatch(PlayerA, PlayerB):
    eloA, eloB, tenacityA, tenacityB = PlayerA.elo, PlayerB.elo, PlayerA.tenacity, PlayerB.tenacity
    diff = abs(eloA - eloB)
    if diff > 100:
        if eloA > eloB:
            PlayerA.tournament_score += 1
        else:
            PlayerB.tournament_score += 1

    elif PlayerB.isBoring or PlayerA.isBoring:
        PlayerA.tournament_score += 0.5
        PlayerB.tournament_score += 0.5

    elif diff > 50 and diff < 100:
        if eloA > eloB:
            if tenacityB * random.randint(1,9) > eloA:
                PlayerB.tournament_score += 1
            else:
                PlayerA.tournament_score += 1    
        else:
            if tenacityA * random.randint(1,9) > eloB:
                PlayerA.tournament_score += 1
            else:
                PlayerB.tournament_score += 1 

    elif diff < 50:
        if tenacityA > tenacityB:
            PlayerA.tournament_score += 1
        else:
            PlayerB.tournament_score += 1

            

def main():
    Courage_the_Cowardly_Dog = ChessPlayer('Courage the Cowardly Dog', 25,1000.29, 1000, False)
    Princess_Peach = ChessPlayer('Princess Peach', 23, 945.65, 50, True)
    Walter_White = ChessPlayer('Walter White', 50, 1650.73, 750,False)
    Rory_Gilmore = ChessPlayer('Rory Gilmore', 16, 1700.87, 500, False)
    Anthony_Fantano = ChessPlayer('Anthony Fantano', 37, 1400.45, 400, True)
    Beth_Harmon = ChessPlayer('Beth Harmon', 20, 2500.34, 150, False)

    players = [Courage_the_Cowardly_Dog, Princess_Peach, Walter_White, Rory_Gilmore, Anthony_Fantano, Beth_Harmon]

    for playerA in players:
        for playerB in players:
            if playerA != playerB:
                print(playerA.name,playerB.name)
                simulateMatch(playerA,playerB)
    print("Tournament Scores- ")
    for player in players:
        print(f"{player.name}: {player.tournament_score}")             


if __name__ == '__main__':
    main()