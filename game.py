import numpy as np

class TwoPlayerGame:
    def __init__(self, action_set1: np.array, action_set2: np.array, payoffs1: np.ndarray, payoffs2: np.ndarray, strategy1: np.array, strategy2: np.array):
        self.action_sets = np.vstack((action_set1, action_set2))
        self.payoffs = np.stack((payoffs1, payoffs2))
        self.strategies = np.vstack((strategy1, strategy2))

    # for readability, I'm indexing players with 1 and 2, hence the -1 below
    def getStrategy(self, player: int) -> np.array:
        return self.strategies[player-1]

    def getPayoffs(self) -> np.ndarray:
        return self.payoffs

    # for readability, I'm indexing players with 1 and 2, hence the -1 below
    def getPayoffs(self, player: int) -> np.ndarray:
        return self.payoffs[player-1]

    def setStrategies(self, strategy1: np.array, strategy2: np.array):
        self.strategies = np.vstack((strategy1, strategy2))

    def expectedPayoffs(self, player: int) -> np.array:
        opponent = 1 if player == 2 else 2
        # multiply player's payoffs by respective probability of the opponent playing that action
        # then sum the rows so that each action of the player has an expected payoff
        return np.sum(self.payoffs[player-1] * self.strategies[opponent-1], axis=1)
