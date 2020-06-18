"""
    This file contains your final_strategy that will be submitted to the contest.
    It will only be run on your local machine, so you can import whatever you want!
    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""
from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

PLAYER_NAME = 'just chillin up here'  # Change this line!

GOAL_SCORE = 100

def baseline_strategy(score, opponent_score):
    """ beats all other strategies """

    """if not(bad_zero_swap(score, opponent_score)):
        if not(swap_strategy(score, opponent_score, 7)) or not(swap_strategy(score, opponent_score, abs(GOAL_SCORE - score))):
            return 0
        elif score > 89:
                return (GOAL_SCORE - score) // 2"""

    return 6


def swap_or_go_home(score, opponent_score):

    return 6

"""def best_move(score, opponent_score):
    best_score = free_bacon(opponent_score)
    best_roll = 0
    for i in range(11):
        new_score = score + roll_dice(i)
        if roll_dice(i) > best_score and ((free_bacon(score+roll_dice(i)) + opponent_score) < 10):
             if not is_swap()


    return best_roll"""

def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    best_roll, best_score, i = 1, 0, 1
    while i<11:
        pos_best = make_averaged(roll_dice, num_samples)(i,dice)
        if pos_best > best_score:
            best_roll = i
            best_score = pos_best
        i += 1
    return best_roll

def make_averaged(g, num_samples=1000):
    """Return a function that returns the average value of G when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """

    def averager(*args):
        total = 0
        for i in range (num_samples):
            total += g(*args)
        return total/num_samples
    return averager


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    roll, score, one = 0, 0, 0
    for i in range(num_rolls):
        roll = dice()
        if roll == 1:
            one = 1
        score += roll
    if one:
        return 1
    return score

def bad_zero_swap(score, opponent_score):
    """ Returns False when rolling zero would allow the opponent
     to then also roll zero and swap scores with us giving them the lead """

    score_if0 = score + free_bacon(opponent_score)
    opponent_if0 = opponent_score + free_bacon(score_if0)
    if score_if0 > opponent_if0 and is_swap(score_if0, opponent_if0):
        return True
    return False

def bacon_strategy(score, opponent_score, margin=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least MARGIN points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    if free_bacon(opponent_score) >= margin:
        return 0
    return num_rolls # Replace this statement
    # END PROBLEM 10


def swap_strategy(score, opponent_score, margin=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points and does not trigger a
    non-beneficial swap. Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    bacon_score = score + free_bacon(opponent_score)
    if (bacon_score < opponent_score) and is_swap(bacon_score, opponent_score):
        return 0
    elif (free_bacon(opponent_score) >= margin) and (not(is_swap(bacon_score, opponent_score)) or (opponent_score > bacon_score)):
        return 0
    return num_rolls

def is_swap(player_score, opponent_score):
    """
    Return whether the two scores should be swapped
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    pow_three = pow(3, player_score + opponent_score)
    ten_power = len(str(pow_three)) - 1
    return pow_three%10 == pow_three//(pow(10,ten_power))

def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    #assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    trip_score = pow(score, 3)
    len_trip = len(str(trip_score))
    add, sub = lambda x: x, lambda x: -x
    sum = 0

    if len_trip%2 == 0:
        even, odd = add, sub
    else:
        even, odd = sub, add

    for i in range(len_trip):
        if (i+1)%2==0:
             sum += even(trip_score%10)
        else:
            sum += odd(trip_score%10)
        trip_score //= 10
        #print('DEBUG: sum:', sum, 'trip_score:', trip_score)
    sum = abs(sum)+1
    return sum
