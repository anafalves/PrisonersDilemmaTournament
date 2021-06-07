# I start by cooperating
# I forgive 3 cheats in a row. After 3, I cheat you back.
# After a while, I see if you keep cheating.
# If you started to cooperate, I cooperate back until next step, where i revise again if you cheat me twice in a row

# This revision actually seems to screw up the results. If I don't add it, I can get the 2nd or 3rd place.
# If I add it, I get between 3rd and 6th place. ¯\_(ツ)_/¯

import random



def strategy(history, memory):
    cooperate = 1
    cheater = 0
    choice = cooperate # I start by cooperating

    gameLength = history.shape[1]
    gameStep = random.random()

    # I see if you cheat for 3 times in a row. If so, I cheat you back
    if gameLength >= 3 and history[1, -1] == cheater and history[1, -2] == cheater and history[1, -3] == cheater:    # and history[1,-2] == 0 and history[1,-3] == 0):
        choice = cheater

        # But i give you a second chance, and see if you have started to cooperate. If you do, I cooperate back
        if gameLength >= gameStep and history[1,-1] == cooperate:
            choice = cooperate

        # Next step, where i revise again if you cheat me twice in a row. If so, I cheat you back
        if gameLength >= gameStep * 2 and history[1, -1] == cheater and history[1, -2] == cheater:
            choice = cheater

    return choice, None