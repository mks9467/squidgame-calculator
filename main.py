import random

class Player:
    "Player piece"
    def __init__(self, player_position, total_steps=18):
        self.bridge_position = 0 # where this player is on the bridge
        self.player_position = player_position # where this player is in the sequence
        self.leader = False # if this player is in the lead
        self.alive = True # if this player is still alive
        self.active = True
        self.survived = False
        self.total_steps = total_steps
    def lead_step(self):
        if self.alive==True and self.active==True:
            if self.bridge_position <= self.total_steps:
                self.bridge_position +=1
                self.side_choice = random.choice(['a','b'])
            else:
                self.active=False
class Tile:
    "Tile Piece"
    def __init__(self, step, side, safe=True):
        self.side=side
        self.step=step
        self.safe=safe
class Bridge:
    def __init__(self):
        self.name=''       
    def draw_bridge(self, total_steps=18):
        self.bridge=[]
        self.total_steps=total_steps
        side = ['a','b']
        step = [i for i in range(1,self.total_steps+1)]
        for s in step:
            for d in side:
                if d=='a':
                    safe = random.choice([True, False])
                else:
                    if safe==True:
                        safe=False
                    else:
                        safe = True
                self.bridge.append(Tile(s,d,safe))
class Game:
    def __init__(self,game_number, total_steps=18, total_players = 16):
        self.game_numnber = game_number
        self.bridge = Bridge()
        self.total_steps=total_steps
        self.total_players = total_players
    def setup_game(self):
        "Initializes the game"
        self.bridge.draw_bridge(self.total_steps)
        self.glass_bridge = {}
        for tile in self.bridge.bridge:
            self.glass_bridge[str(tile.step)+tile.side]=tile.safe
        self.players = [Player(i,self.total_steps) for i in range(1,self.total_players+1)]
    def play_game(self):
        memory=0
        self.results = {}
        for player in self.players:
            player.bridge_position = memory
            if memory < self.total_steps:
                while player.alive==True and player.active==True and player.bridge_position<=self.total_steps:
                    if player.bridge_position < self.total_steps:
                        player.lead_step()
                        tile_choice = str(player.bridge_position) + player.side_choice
                        if self.glass_bridge[tile_choice]==False:
                            player.alive=False
                            self.results[player.player_position] = player.survived
                        memory+=1
                    elif player.bridge_position == self.total_steps:
                        player.survived=True
                        player.bridge_position += 1
                        self.results[player.player_position] = player.survived                    
            else:
                player.survived=True
                self.results[player.player_position] = player.survived                
                pass