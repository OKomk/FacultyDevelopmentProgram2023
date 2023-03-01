import numpy as np
import random 
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")


def montyHall(noOfTrails, switch_door=False):

    noOfWins = 0

    for i in range (noOfTrails):
        prize_door = random.randint(1, 3)
        
        # The contestant chooses a door at random
        contestant_door = random.randint(1, 3)
        
        # The host chooses a door to reveal that does not have the prize
        revealed_door = random.choice([door for door in range(1, 4) if door != prize_door and door != contestant_door])
        
        if switch_door:
            # The contestant switches to the other unopened door
            contestant_door = [door for door in range(1, 4) if door != contestant_door and door != revealed_door][0]
            
        # Check if the contestant has won
        if contestant_door == prize_door:
            noOfWins += 1
    
    win_probability = noOfWins / noOfTrails
    return win_probability


def plot_win_probability(num_trials, switch_door=True):
    probabilities = []
    
    for i in range(1, num_trials+1, 100):
        win_probability = montyHall(i, switch_door=switch_door)
        probabilities.append(win_probability)
        
    plt.plot(range(1, num_trials+1, 100), probabilities)
    plt.xlabel("Number of Trials")
    plt.ylabel("Win Probability")
    plt.title("Monty Hall Problem Simulation")

n = int(input('Enter the no. of Trails\n'))

pSwitch = montyHall(n,True)
pNoSwitch = montyHall(n,False)

print(f'Probability of Winning after switching: {pSwitch}')
print(f'Probability of Winning without switching: {pNoSwitch}')

plot_win_probability(n, switch_door=True)
plot_win_probability(n, switch_door=False)
plt.legend(["Switching Doors", "Not Switching Doors"])
plt.show()

# Define a function to plot the distribution of wins
def plot_win_distribution(num_trials, switch_door=True):
    num_wins = 0
    win_doors = []
    
    # Iterate over the number of trials
    for i in range(num_trials):
        # Choose a random door to hide the prize behind
        prize_door = random.randint(1, 3)
        
        # The contestant chooses a door at random
        contestant_door = random.randint(1, 3)
        
        # The host chooses a door to reveal that does not have the prize
        revealed_door = random.choice([door for door in range(1, 4) if door != prize_door and door != contestant_door])
        
        if switch_door:
            # The contestant switches to the other unopened door
            contestant_door = [door for door in range(1, 4) if door != contestant_door and door != revealed_door][0]
            
        # Check if the contestant has won
        if contestant_door == prize_door:
            num_wins += 1
            win_doors.append(prize_door)
        else:
            win_doors.append(0)
            
    # Plot the distribution of wins
    sns.histplot(win_doors, bins=[0, 1, 2, 3], stat='probability', discrete=True)
    plt.xticks([1, 2, 3], ['Door 1', 'Door 2', 'Door 3'])
    plt.xlabel("Winning Door")
    plt.ylabel("Probability")
    plt.title("Distribution of Wins")

plot_win_distribution(n, True)
plot_win_distribution(n, False)

plt.show()

# Define a function to plot the win probability histogram
def plot_win_probability_histogram(num_trials, switch_door=True):
    win_probabilities = []
    
    for i in range(num_trials):
        win_probability = montyHall(1, switch_door=switch_door)
        win_probabilities.append(win_probability)
        
    plt.hist(win_probabilities, bins=20, range=(0, 1), alpha=0.5)
    plt.xlabel("Win Probability")
    plt.ylabel("Frequency")
    plt.title("Monty Hall Problem Simulation")

# Example usage
num_trials = 10000

# Plot the win probability over time
plt.subplot(2, 2, 1)
plot_win_probability(num_trials, switch_door=True)
plot_win_probability(num_trials, switch_door=False)
plt.legend(["Switching Doors", "Not Switching Doors"])

# Plot the win probability histogram
plt.subplot(2, 2, 2)
plot_win_probability_histogram(num_trials, switch_door=True)

# Plot the win probability histogram with density curve
plt.subplot(2, 2, 3)
plot_win_probability_histogram(num_trials, switch_door=False)
win_probabilities = [montyHall(1, switch_door=False) for i in range(num_trials)]
plt.plot(sorted(win_probabilities), [i/num_trials for i in range(num_trials)], color="red")
plt.xlabel("Win Probability")
plt.ylabel("Density")
plt.title("Monty Hall Problem Simulation")

plt.tight_layout()
plt.show()