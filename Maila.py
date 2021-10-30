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
    
    def add_game(self, mode = "duo", verbose = True):
        """Add a game to the database and update player PAMs."""
        # Gather game information
        (game_date, players, score, weight) = self.gather_game_info()
        # Save game information to database
        if mode == "duo":
            game_info = [players[team][p].name for team in players
                         for p in range(2)]
        else:
            tmp = [players[team][0].name for team in players]
            game_info = [tmp[0], None, tmp[1], None]
        game_info.append(self.scores_to_str(score))
        game_info.append(weight)
        game_info.append(game_date)
        self.games.loc[len(self.games.index)] = game_info
        #self.games.to_csv(self.games_file, index = False)
        # TODO: add save function on exit
        # Update player PAMs based on game
        PAMs_update = self.update_PAM(mode, players, score, float(weight))
        if verbose:
            print("Points changed by", max(PAMs_update))
        if mode == "duo":
            for p in range(2):
                self.update_player(players["Team 1"][p], PAMs_update[0])
                self.update_player(players["Team 2"][p], PAMs_update[1])
        else:
            self.update_player(players["Team 1"][0], PAMs_update[0])
            self.update_player(players["Team 2"][0], PAMs_update[1])
    
    def visualise(self, vis_type = "classement"):
        """Display information about club players in various ways (plots and tables)."""
        if vis_type == "violin":
            self.plot_violin()
        elif vis_type == "classement":
            self.ranking_table()
    
    def reinitialise(self, verbose = False):
        """Reinitialise all player PAMs (when updating the elo computations)."""
        # Reinitialise PAMs based on starting club category
        for i, player in self.players.iterrows():
            if player.Category == "2B":
                PAM = 800
            elif player.Category == "2A":
                PAM = 1000
            elif player.Category == "1B":
                PAM = 1200
            elif player.Category == "1A":
                PAM = 1400
            self.update_player(player, PAM, ("PAM_solo", "PAM_duo"))
        #self.players.to_csv(self.players_file, index = False)
        # Replay games
        if verbose:
            saved_updates = []
        for i, game in self.games.iterrows():
            # TODO: solo games (how are NAs coded ?)
            mode = "duo"
            players = {"Team 1" : [self.players.loc[self.players["Name"] == game.T1P1.tolist()[0],
                                   self.players.loc[self.players["Name"] == game.T1P2.tolist()[0]],
                       "Team 2" : [self.players.loc[self.players["Name"] == game.T2P1.tolist()[0],
                                   self.players.loc[self.players["Name"] == game.T2P2.tolist()[0]]}
            score = self.str_to_score(game.Score)
            weight = float(game.Weight)
            PAMs_update = self.update_PAM(mode, players, score, weight)
            if verbose:
                saved_updates.append(PAMs_update)
                print(i+2)
            if mode == "duo":
                for p in range(2):
                    self.update_player(players["Team 1"][p], PAMs_update[0])
                    self.update_player(players["Team 2"][p], PAMs_update[1])
            else:
                self.update_player(players["Team 1"][0], PAMs_update[0])
                self.update_player(players["Team 2"][0], PAMs_update[1])
        if verbose:
            return saved_updates
    
    def gather_game_info(self, mode):
        """Gather information about a new game (console interface)."""
        # Define number of players in the game
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
                player_ok = False
                while not player_ok:
                    player_name = input(f"Équipe {t+1}, joueur {p+1} : ")
                    player = self.players[self.players["Name"] == player_name]
                    if not player.empty:
                        players[team].append(player)
                        player_ok = True
                    else:
                        create_new = input("Joueur non reconnu, créer un nouveau joueur ? (oui/non) ")
                        if create_new == "non":
                            continue
                        else:
                            new_player = Pilotari(player_name, self.players_file)
                            player_info = [new_player.name]
                            player_info.append(new_player.category)
                            player_info.append(new_player.pam_solo)
                            player_info.append(new_player.pam_duo)
                            player_info.append(new_player.member)
                            self.players.loc[len(self.players.index)] = player_info
                            player = self.players[self.players["Name"] == player_name]
                            players[team].append(player)
                            player_ok = True
                            
        # Ask for game weight (to account for special tournaments)
        weight = input("Poids de la partie (défaut 1) : ")
        if weight == "":
            weight = 1
        # Get score and number of sets
        tmp = input("Score pour l'équipe 1 (en sets, format S1-S2) : ").split("-")
        score = [int(sets) for sets in tmp]
        # Return players list, total scores, and number of sets
        return (mode, game_date, players, score, weight)
    
    def scores_to_str(self, score):
        return f"{score[0]}-{score[1]}"
    
    def str_to_score(self, str_score):
        return [int(sets) for sets in str_score.split("-")]
    
    def update_PAM(self, mode, players, score, weight):
        """Update PAMs for all players for a given game."""
        # Setup general ELO rating parameters
        c = 100
        d = 400
        # Get each team's PAM based on mode
        if mode == "duo":
            PAMs = [(players["Team 1"][0].PAM_duo +\
                         players["Team 1"][1].PAM_duo)/2,
                    (players["Team 2"][0].PAM_duo +\
                         players["Team 2"][1].PAM_duo)/2]
        else:
            PAMs = [players["Team 1"][0].PAM_solo,
                    players["Team 2"][0].PAM_solo]
        # Compute each team 1's result and prediction according to PAMs
        # Team 2's result and prediction is 1 - team 1's result and prediction
        predT1 = 1 / (1 + c**((PAMs[1] - PAMs[0])/d))
        resT1 = int(score[0] > score[1])
        # Compute points in play, weighed to account for atypical tournaments
        k = 30 * weight
        # Get new PAMs
        PAMs_update = [k*(resT1-predT1),
                       k*(predT1-resT1)]
        return PAMs_update
    
    def update_player(self, player, PAM, PAM_type, absolute = False):
        """"Update a given player's PAM, relative to previous PAM by default."""
        # If relative change, add initial PAM of correct type
        if not absolute:
            try:
                PAM += player[PAM_type]
            except TypeError:
                PAM = [PAM + player[t] for t in PAM_type]
        # Update club's player list
        player_name = player.Name.tolist()[0]
        self.players.loc[self.players["Name"] == player_name, PAM_type] = PAM
        # Update player history
        player = Pilotari(player_name, self.players_file)
        player.update_PAM(PAM, PAM_type, reset = absolute)
    
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
        