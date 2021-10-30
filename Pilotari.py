import pandas as pd
#os.chdir("/home/arthur/Documents/CPBP/PartidaAntolatzekoMaila/")

class Pilotari(object):
    """Class for a single player (pilotari)"""
    
    def __init__(self, name, filename = "pilotari_historio.csv"):
        """Initialise a player.
        
        Check if player present in database, else create a new one.
        
        """
        # Check if player exists
        club_players = pd.read_csv(filename)
        player_info = club_players[club_players["Name"] == name]
        # If player exists, get info
        if not player_info.empty:
            self.latest = max(player_info.Date)
            self.player_info = player_info.loc[player_info.Date == self.latest]
            self.name = name
            self.category = self.player_info.loc[:,"Category"].tolist()[0]
            self.pam_solo = float(self.player_info.loc[:,"PAM_solo"]).tolist()[0]
            self.pam_duo = float(self.player_info.loc[:,"PAM_duo"]).tolist()[0]
        # If player not registered, create new player
        else:
            self.new_player(name, filename)
    
    def new_player(self, name):
        """Create a new player (console interface).
        
        If filename provided, save new player at the end of the file.
        
        """
        self.name = name
        # Get club category, define initial PAM based on category
        category = None
        while category not in ["1A","1B","2A","2B"]:
            category = input("Catégorie club (1A/1B/2A/2B) pour " + name + " : ")
        self.category = category
        if category == "2B":
            self.pam_solo = 800
            self.pam_duo = 800
        elif category == "2A":
            self.pam_solo = 1000
            self.pam_duo = 1000
        elif category == "1B":
            self.pam_solo = 1200
            self.pam_duo = 1200
        else:
            self.pam_solo = 1400
            self.pam_duo = 1400
        # Is player an active member? (for club ranking displays)
        member = None
        while member not in ["oui", "non"]:
            member = input(name + " est membre actif.ve du club ? (oui/non) ")
        self.member = member == "oui"
    
    def update_PAM(self, PAM, PAM_type, date,
                   reset):
        #TODO
        pass
    
    def save_player(self, filename):
        """Saves player information."""
        club_players = pd.read_csv(filename)
        club_players.loc[club_players["Name"] == self.name] = [self.name,
                                                               self.category,
                                                               self.pam_solo,
                                                               self.pam_duo,
                                                               self.member]
        club_players.to_csv(filename, index = False)
            