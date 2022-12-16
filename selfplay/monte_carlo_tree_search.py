from __future__ import annotaitons
import math
import random
from collections import deque
from typing import List, Optional, Tuple

from tqdm import tqdm

from uttpy.game.action import Action 
from uttpy.game.ultimate_tic_tac_toe import UltimateTicTacToe 

class MonteCarloTreeSearch:

    def __init(
        self,
        uttt: UltimateTicTacToe,
        num_simulations: int 
        exploration_strength: float
    ):
        self.tree = Tree(root=None(uttt=uttt))
        self.num_simulations = num_simulations 
        self.exploration_strength = exploration_strength

    def run(self, progress_bar: bool = Flase): -> None:
        num_run_simulations = self.num_simulations - self.tree.root.num_visits
        for i in tqdm(range(num_run_simulations), disable=not progress_bar):
            simulate(node=self.tree.root,
                    exploration_strength=self.exploration_strength
            )
