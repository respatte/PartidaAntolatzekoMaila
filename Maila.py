import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
        (mode, game_date, players, scores, sets, weight) = self.gather_game_info()
        # Save game information to database
        if mode == "duo":
            game_info = [players[team][p].name for team in players
                         for p in range(2)]
        else:
            tmp = [players[team][0].name for team in players]
            game_info = [tmp[0], None, tmp[1], None]
        game_info.append(self.scores_to_str(scores))
        game_info.append(sets)
        game_info.append(weight)
        game_info.append(game_date)
        self.games.loc[len(self.games.index)] = game_info
        self.games.to_csv(self.games_file, index = False)
        # Update player PAMs based on game
        PAMs_update = self.update_PAM(mode, players, scores,
                                      int(sets), float(weight))
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
    
    def visualise(self, vis_type = "classement"):
        """Display information about club players in various ways (plots and tables)."""
        if vis_type == "violin":
            self.plot_violin()
        elif vis_type == "classement":
            self.ranking_table()
    
    def reinitialise(self, verbose = False):
        """Reinitialise all player PAMs (when updating the elo computations)."""
        # Reinitialise PAMs based on starting club category
        self.players.loc[(self.players.Category == "2B"), ("PAM_solo","PAM_duo")] = 800
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
            scores = self.str_to_score(game.Score)
            sets = int(game.Sets)
            weight = float(game.Weight)
            PAMs_update = self.update_PAM(mode, players, scores, sets, weight)
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
        # Ask for game weight (to account for special tournaments)
        weight = input("Poids de la partie (défaut 1) : ")
        if weight == "":
            weight = 1
        # Get score and number of sets
        score_approved = False
        while not score_approved:
            scores = []
            sets = int(input("Nombre de sets joués : "))
            for s in range(sets):
                tmp = input(f"Score set {s+1} (pour l'équipe 1, format N1-N2) : ").split("-")
                set_score = [int(points) for points in tmp]
                scores.append(set_score)
            check = input(f"Score entrés : {scores}. Valider ? (oui/non) ")
            score_approved = check == "oui"
        # Return players list, total scores, and number of sets
        return (mode, game_date, players, scores, sets, weight)
    
    def scores_to_str(self, scores):
        return " ".join([f"{score[0]}-{score[1]}" for score in scores])
    
    def str_to_score(self, str_scores):
        return [[int(points) for points in score.split("-")]
                for score in str_scores.split(" ")]
    
    def update_PAM(self, mode, players, scores, sets, weight):
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
        resT1 = sum([score[0]>score[1] for score in scores]) > sets/2
        # Compute points in play, weighed to account for atypical tournaments
        k = 30 * weight
        # Get new PAMs
        PAMs_update = [k*(resT1-predT1),
                       k*(predT1-resT1)]
        return PAMs_update
    
    def plot_violin(self):
        """Plot the distribution of player PAMs by club category."""
        categories = ["2B", "2A", "1B", "1A"]
        for i, cat in enumerate(categories):
            plt.violinplot(self.players[self.players.Category == cat]["PAM_duo"],
                           positions = [i], showextrema=False)
            plt.boxplot(self.players[self.players.Category == cat]["PAM_duo"],
                        positions = [i])
        plt.xticks(ticks=list(range(len(categories))), labels=categories)
        plt.show()
    
    def ranking_table(self):
        """Print a ranking table of the players."""
        # Get only active members
        sorted_players = self.players[self.players.Member]
        # Sort by descending PAM
        sorted_players = sorted_players.sort_values(by = ["PAM_duo"],
                                                    ascending = False,
                                                    ignore_index=True)
        # Round PAM value for nicer display
        sorted_players = sorted_players.astype({"PAM_duo":int})
        # Select relevant columns
        sorted_players = sorted_players[["Name", "Category", "PAM_duo"]]
        # Make column names French
        sorted_players = sorted_players.rename(columns = {"Name" : "Joueur",
                                                          "Category" : "Série",
                                                          "PAM_duo" : "PAM"})
        # Start index at 1 and change index name
        sorted_players.index += 1
        sorted_players.index.name = "Classement"
        print(sorted_players.to_markdown())
        