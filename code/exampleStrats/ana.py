# I start by cooperating
# I forgive 3 cheats in a row. After 3, I cheat you back.
# After a while, I see if you keep cheating.
# If you started to cooperate, I cooperate back until the end of the game

# For the outputs: the first value is just the move your strategy chooses to make,
# with 0 being defect and 1 being cooperate. The second value is any memory you'd
# like to retain into the next iteration. This can be 'None'.
import random



def strategy(history, memory):
    cooperate = 1
    cheater = 0
    choice = cooperate # i start by cooperating

    # I see if yu cheat for 3 times in a row. If so, I cheat you back
    if history.shape[1] >= 3 and history[1, -1] == cheater and history[1, -2] == cheater and history[1, -3] == cheater:    # and history[1,-2] == 0 and history[1,-3] == 0):
        choice = cheater
        # But i give you a second chance, and see if you have started to cooperate. If you do, I cooperate back
        if history.shape[1] >= random.random() and history[1,-1] == cooperate:
            choice = cooperate

    return choice, None