class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp   = 1500
        self.team = team

    def introduce(self):
        print(f"I'm {self.name} and I Play for {self.team}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players   = []

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def show_players(self):
        for player in self.players:
            player.introduce()

    # player를 삭제하는 method
    def remove_players(self):
        print("remove_players")

    # Team 의 경험치(XP) 총합을 보여주는 method
    def sum_xp(self):
        sum = 0
        for player in self.players:
            sum += player.xp
        print(f"sum : {sum}")

team_x = Team("Team X")
team_x.add_player("Wendy")
team_x.show_players()
team_x.sum_xp()

team_y = Team("Team Y")
team_y.add_player("Irene")
team_y.add_player("Joy")
team_y.show_players()
team_y.sum_xp()

# home work
# 1. Team class에 player를 삭제하는 method
# 2. Team 의 경험치(XP) 총합을 보여주는 method