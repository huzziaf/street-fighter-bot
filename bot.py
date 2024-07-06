from command import Command
import numpy as np
import pandas as pd
from buttons import Buttons
class Bot:

    def __init__(self):
        #< - v + < - v - v + > - > + Y
        self.fire_code=["<","!<","v+<","!v+!<","v","!v","v+>","!v+!>",">+Y","!>+!Y"]
        self.exe_code = 0
        self.start_fire=True
        self.remaining_code=[]
        self.my_command = Command()
        self.buttn= Buttons()

    def fight(self,cgs,player,model):
        #python Videos\gamebot-competition-master\PythonAPI\controller.py 1
        test = pd.DataFrame({'ID1':[cgs.player1.player_id], 'ID2':[cgs.player2.player_id],'Player2_is_jumping': [cgs.player2.is_jumping], 'Player2_is_crouching': [cgs.player2.is_crouching], 'Player2_is_player_in_move': [cgs.player2.is_player_in_move], 'EuDistance' : [((cgs.player1.x_coord - cgs.player2.x_coord)**2 + (cgs.player1.y_coord - cgs.player1.y_coord)**2)**0.5], 'Player1_move_id':[cgs.player1.move_id],'Player2_move_id':[cgs.player2.move_id]})
        preds = model.predict(test)
        if player=="1":
            self.buttn.down=bool(preds[:,1])
            self.buttn.up=bool(preds[:,0])
            self.buttn.left=bool(preds[:,3])
            self.buttn.right=bool(preds[:,2])
            self.buttn.X=bool(preds[:,6])
            self.buttn.B=bool(preds[:,5])
            self.buttn.A=bool(preds[:,7])
            self.buttn.L=bool(preds[:,8])
            self.buttn.R=bool(preds[:,9])
            self.buttn.Y=bool(preds[:,4])

            if self.buttn.down:
                print('v')
            if self.buttn.up:
                print('^')
            if self.buttn.left:
                print('<')
            if self.buttn.right:
                print('>')
            if self.buttn.X:
                print('X')
            if self.buttn.B:
                print('B')
            if self.buttn.A:
                print('A')
            if self.buttn.L:
                print('L')
            if self.buttn.R:
                print('R')
            if self.buttn.Y:
                print('Y')
            
            self.my_command.player_buttons=self.buttn

        elif player=="2":
            self.buttn.down=bool(preds[:,1])
            self.buttn.up=bool(preds[:,0])
            self.buttn.left=bool(preds[:,2])
            self.buttn.right=bool(preds[:,3])
            self.buttn.X=bool(preds[:,6])
            self.buttn.B=bool(preds[:,5])
            self.buttn.A=bool(preds[:,7])
            self.buttn.L=bool(preds[:,8])
            self.buttn.R=bool(preds[:,9])
            self.buttn.Y=bool(preds[:,4])

            if self.buttn.down:
                print('v')
            if self.buttn.up:
                print('^')
            if self.buttn.left:
                print('<')
            if self.buttn.right:
                print('>')
            if self.buttn.X:
                print('X')
            if self.buttn.B:
                print('B')
            if self.buttn.A:
                print('A')
            if self.buttn.L:
                print('L')
            if self.buttn.R:
                print('R')
            if self.buttn.Y:
                print('Y')
            
            self.my_command.player2_buttons=self.buttn
        print('None')
        return self.my_command