import pandas as pd
from Pilotari import Pilotari

class Maila(object):
    """Access and update ranks (maila) for the club."""
    
    def __init__(self, players_file = "pilotariak.csv", games_file = "partidak.csv"):
        """Read player list and games list."""
        self.players_file = players_file
        self.players = pd.read_csv(players_file)
        self.games_file = games_file
        self.games = pd.read_csv(games_file)
    
    def add_game(self):
        """Add a game to the database and update player PAMs."""
        # Gather game information
        (mode, game_date, players, total_score, sets) = self.gather_game_info()
        # Save game information to database
        if mode == "duo":
            game_info = [players[team][p].name for team in players
                         for p in range(2)]
        else:
            tmp = [players[team][0].name for team in players]
            game_info = [tmp[0], None, tmp[1], None]
        game_info.append(f"{total_score[0]}-{total_score[1]}")
        game_info.append(sets)
        game_info.append(game_date)
        self.games.loc[len(self.games.index)] = game_info
        self.games.to_csv(self.games_file, index = False)
        # Update player PAMs based on game
        PAMs_update = self.update_PAM(mode, players, total_score)
        if mode == "duo":
            for p in range(2):
                players["Team 1"][p].pam_duo += PAMs_update[0]
                players["Team 2"][p].pam_duo += PAMs_update[1]
        else:
            players["Team 1"][0].pam_solo += PAMs_update[0]
            players["Team 2"][0].pam_solo += PAMs_update[1]
        for team in players:
            for p in range(2):
                try:
                    players[team][p].save_player(self.players_file)
                except IndexError:
                    pass
    
    def reinitialise(self, verbose = False):
        """Reinitialise all player PAMs (when updating the elo computations)."""
        # Reinitialise PAMs based on starting club category
        self.players.loc[(self.players.Category == "2B"), ("PAM_solo","PAM_duo")] = 700
        self.players.loc[(self.players.Category == "2A"), ("PAM_solo","PAM_duo")] = 1000
        self.players.loc[(self.players.Category == "1B"), ("PAM_solo","PAM_duo")] = 1200
        self.players.loc[(self.players.Category == "1A"), ("PAM_solo","PAM_duo")] = 1400
        self.players.to_csv(self.players_file, index = False)
        # Replay games
        if verbose:
            saved_updates = []
        for i, game in self.games.iterrows():
            # TODO: solo games (how are NAs coded ?)
            mode = "duo"
            players = {"Team 1" : [Pilotari(game.T1P1, self.players_file),
                                   Pilotari(game.T1P2, self.players_file)],
                       "Team 2" : [Pilotari(game.T2P1, self.players_file),
                                   Pilotari(game.T2P2, self.players_file)]}
            total_score = [int(points) for points in game.Score.split("-")]
            PAMs_update = self.update_PAM(mode, players, total_score)
            if verbose:
                saved_updates.append(PAMs_update)
            if mode == "duo":
                for p in range(2):
                    players["Team 1"][p].pam_duo += PAMs_update[0]
                    players["Team 2"][p].pam_duo += PAMs_update[1]
            else:
                players["Team 1"][0].pam_solo += PAMs_update[0]
                players["Team 2"][0].pam_solo += PAMs_update[1]
            for team in players:
                for p in range(2):
                    try:
                        players[team][p].save_player(self.players_file)
                    except IndexError:
                        pass
        self.players = pd.read_csv(self.players_file)
        if verbose:
            return saved_updates
    
    def gather_game_info(self):
        """Gather information about a new game (console interface)."""
        # Define number of players in the game
        mode = None
        while not mode in ["duo", "solo"]:
            mode = input("Mode de jeu (duo/solo) : ")
        if mode == "duo":
            n_players = 2
        elif mode == "solo":
            n_players = 1
        # Get game date to allow evolution analysis
        game_date = pd.to_datetime(input("Date de la partie (JJ/MM/AA) : "),
                                   dayfirst = True)
        # Get player informations, create players if new players
        players = {"Team 1" : [], "Team 2" : []}
        for t, team in enumerate(players):
            for p in range(n_players):
                player_name = input(f"Équipe {t+1}, joueur {p+1} : ")
                players[team].append(Pilotari(player_name, self.players_file))
        # Get score and number of sets
        score_approved = False
        while not score_approved:
            total_score = [0, 0]
            scores = []
            sets = int(input("Nombre de sets joués : "))
            for s in range(sets):
                tmp = input(f"Score set {s+1} (pour l'équipe 1, format N1-N2) : ").split("-")
                set_score = [int(points) for points in tmp]
                scores.append(set_score)
                total_score[0] += set_score[0]
                total_score[1] += set_score[1]
            check = input(f"Score entrés : {scores}. Valider ? (oui/non) ")
            score_approved = check == "oui"
        # Return players list, total scores, and number of sets
        return (mode, game_date, players, total_score, sets)
    
    def update_PAM(self, mode, players, total_score):
        """Update PAMs for all players for a given game."""
        # Setup general ELO rating parameters
        c = 100
        d = 400
        # Get each team's PAM based on mode
        if mode == "duo":
            PAMs = [(players["Team 1"][0].pam_duo +\
                         players["Team 1"][1].pam_duo)/2,
                    (players["Team 2"][0].pam_duo +\
                         players["Team 2"][1].pam_duo)/2]
        else:
            PAMs = [players["Team 1"][0].pam_solo,
                    players["Team 2"][0].pam_solo]
        # Compute each team 1's result and prediction according to PAMs
        # Team 2's result and prediction is 1 - team 1's result and prediction
        predT1 = 1 / (1 + c**((PAMs[1] - PAMs[0])/d))
        resT1 = int(total_score[0] > total_score[1])
        # Compute match importance as total score difference
        k = 20 * (3 - 2*min(total_score)/max(total_score))
        # Get new PAMs
        PAMs_update = [k*(resT1-predT1),
                       k*(predT1-resT1)]
        return PAMs_update