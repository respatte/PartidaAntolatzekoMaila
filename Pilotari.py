import pandas as pd
#os.chdir("/home/arthur/Documents/CPBP/PartidaAntolatzekoMaila/")

class Pilotari(object):
    """Class for a single player (pilotari)"""
    
    def __init__(self, name):
        """Initialise a player.
        
        Check if player present in database, else create a new one.
        
        """
        # Check if player exists
        self.name = name
        self.filename = "".join(["pilotari_historio/"] + name.split() + [".csv"])
        try:
            self.player_info = pd.read_csv(self.filename)
            # If player exists, get info
            self.latest_date = max(self.player_info.Date)
            self.latest_info = self.player_info.loc[self.player_info.Date == self.latest_date]
            self.category = self.latest_info.loc[:,"Category"].tolist()[0]
            self.pam = float(self.latest_info.loc[:,"PAM"].tolist()[0])
            self.member = self.latest_info.loc[:,"Member"].tolist()[0]
        except FileNotFoundError:
            # If player not registered, create new player
            self.new_player()
    
    def new_player(self):
        """Create a new player (console interface).
        
        If filename provided, save new player at the end of the file.
        
        """
        # Set date for initial PAM (fake date)
        self.latest_date = pd.to_datetime("01/01/1900", dayfirst = True)
        # Get club category, define initial PAM based on category
        category = None
        while category not in ["1A","1B","2A","2B"]:
            category = input("Catégorie club (1A/1B/2A/2B) pour " + self.name + " : ")
        self.category = category
        if category == "2B":
            self.pam = 800
        elif category == "2A":
            self.pam = 1000
        elif category == "1B":
            self.pam = 1200
        else:
            self.pam = 1400
        # Is player an active member? (for club ranking displays)
        member = None
        while member not in ["oui", "non"]:
            member = input(self.name + " est membre actif.ve du club ? (oui/non) ")
        self.member = member == "oui"
        # Create player csv
        data = {"Name" : self.name,
                "Category" : self.category,
                "PAM" : self.pam,
                "Member" : self.member,
                "Date" : self.latest_date}
        self.player_info = pd.DataFrame(data,index=[0])
        self.latest_info = pd.DataFrame(data,index=[0])
        self.player_info.to_csv(self.filename, index = False)
    
    def update_PAM(self, PAM, date, reset):
        # If player reset, only keep initial line
        if reset:
            self.player_info = self.player_info.loc[self.player_info.Date == date]
        # If no reset, update PAM
        if date == self.latest_date:
            # If date already added, updated PAM in place
            self.player_info.loc[self.player_info.Date == self.latest_date,
                                 "PAM"] = PAM
        else:
            # If new date, add a row with new PAM
            self.player_info.loc[len(self.player_info)] = [self.name,
                                                           self.category,
                                                           PAM,
                                                           self.member,
                                                           date]
        self.player_info.to_csv(self.filename, index = False)
            