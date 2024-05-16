from math import gcd
import numpy as np

# INPUT1: Transition probability matrix
rows = int(input("Enter #rows: "))
cols = int(input("Enter #columns: "))

print("---------------------------------------------")

Transition_prob_matrix = []
for i in range(rows):
    while True:  # keep asking for input until the row sums to 1
        row = []
        for j in range(cols):
            element = float(input(f"Enter the element for row {i}, column {j}: "))
            row.append(element)
        if sum(row) == 1:
            Transition_prob_matrix.append(row)
            break  # exit the loop if the row sums to 1
        else:
            print(f"The elements of row {i} do not sum to 1. Please re-enter the row.")

print("Transition probability matrix: ")
for row in Transition_prob_matrix:
    print(row)

print("---------------------------------------------")

# INPUT2: Initial state probabilities vector
size = int(input("Enter the size of the initial state probabilities vector: "))

initial_state_prob_vector = []
while True:  # keep asking for input until the vector sums to 1
    initial_state_prob_vector = []
    for i in range(size):
        element = float(input(f"Enter the element for position {i}: "))
        initial_state_prob_vector.append(element)
    if sum(initial_state_prob_vector) == 1:
        break  # exit the loop if the vector sums to 1
    else:
        print("The elements of the vector do not sum to 1. Please re-enter the vector.")

print("Initial state probability matrix: ", initial_state_prob_vector)

print("---------------------------------------------")

# INPUT3: Number of steps
# INPUT4: State ID
state_steps = {} # dictionary whose keys are STATE_ID and the values are NUMBER OF STEPS for each state
for i in range(rows):
    while True:
        state_id = int(input(f"Enter the state ID (from 0 to {rows - 1}): "))
        if 0 <= state_id < rows:
            break
        else:
            print("Please re-enter the correct number of states.")

    num_steps = int(input(f"Enter the number of steps for state {i}: "))
    state_steps[state_id] = num_steps

print("State IDs and their respective number of steps:")
print(state_steps)

print("************************************************************************************************************8")

# OUTPUT1: TYPE OF STATE

def is_reachable(transition_matrix, state_steps):
    print("A state is reachable if P[i][j]**n > 0")
    print("A state is irreducible if it is reachable")
    print("Markov chain is Reducible if there is at least one set isn't reachable")

    flag = True

    for state_id, num_steps in state_steps.items():
        state_reachable = False

        for i in range(len(transition_matrix)):
            transition_prob = transition_matrix[state_id][i]
            probability_after_steps = transition_prob ** num_steps
            reachable_str = "(reachable) and (irreducible)" if probability_after_steps > 0 else "(unreachable)"
            print(f"Transition probability from state {state_id} to state {i} raised to the power of {num_steps} = {probability_after_steps} {reachable_str}")
            if probability_after_steps > 0:
                state_reachable = True
        if not state_reachable:
                flag = False

    if flag:
        print("The Markov chain is irreducible")
    else:
        print("The Markov chain is reducible")

is_reachable(Transition_prob_matrix, state_steps)

print("************************************************************************************************************8")

def is_closed(transition_matrix, state_steps):
    print("A state is closed if P[i][j] = 0")
    print("Markov chain is Reducible if there is at least one closed set")

    flag = False

    for state_id, num_steps in state_steps.items():
        for i in range(len(transition_matrix)):
            transition_prob = transition_matrix[state_id][i]
            closed_str = "(closed)" if transition_prob == 0 else ""
            print(f"Transition probability from state {state_id} to state {i} = {transition_prob} {closed_str}")
            if transition_prob == 0:
                flag = True

    if flag:
        print("The Markov chain is Reducible.")
    else:
        print("The Markov chain is Irreducible.")

is_closed(Transition_prob_matrix, state_steps)

print("************************************************************************************************************8")

def is_absorbing(transition_matrix, state_steps):
    print("A state is absorbing if P[i][i] = 1")
    print("Markov chain is Recurrent if there is at least one absorbing state")
    print("Markov chain is Absorbing if all states are absorbing")

    flag = False
    all_absorbing = True

    for state_id, num_steps in state_steps.items():
        for i in range(len(transition_matrix)):
            transition_prob = transition_matrix[state_id][i]
            if (i == state_id):
                if (transition_prob == 1):
                    absorbing_str = "(absorbing/recurrent)"
                    flag = True
                elif (transition_prob < 1):
                    absorbing_str = "(transient)"
                    all_absorbing = False
            else:
                absorbing_str = ""
            print(f"Transition probability from state {state_id} to state {i} = {transition_prob} {absorbing_str}")

    if flag:
        print("The Markov chain is Recurrent.")
    elif all_absorbing:
        print("The Markov chain is absorbing.")
    else:
        print("The Markov chain is not recurrent or absorbing.")

is_absorbing(Transition_prob_matrix, state_steps)

print("************************************************************************************************************8")

def is_periodic(transition_matrix, state_steps):
    flag = False
    # iterate over all state IDs
    for state_id in state_steps.keys():
        # for each state, calc the set of all return times to that state
        return_times = set()

        for num_steps in state_steps.values():
            # find the greatest common divisor of these return times
            return_times.add(num_steps)

        gcd_return_times = gcd(*return_times)

        if gcd_return_times > 1:
            print(f"State {state_id} is periodic with period {gcd_return_times}.")
        else:
            print(f"State {state_id} is aperiodic.")
            flag = True

    if flag:
        print("The Markov chain is aperiodic.")
    else:
        print("The Markov chain is not aperiodic.")

is_periodic(Transition_prob_matrix, state_steps)

print("************************************************************************************************************8")


# OUTPUT2: MARKOV CHAIN CLASSIFICATION
"""
-> at least one closed set? Reducible✅ 
-> at least one state is not reachable? Reducible✅
-> at least one state is absorbing? Recurrent✅
-> at lease one aperiodic state? Aperiodic✅
-> all states are absorbing? Absorbing✅
"""



# OUTPUT 3 and 4
# STATE PROBABILITIES AFTER N STEPS (P_N)
def state_probabilities_after_n_steps(transition_matrix, initial_state_prob_vector, num_steps):
    transition_matrix_power_n = np.linalg.matrix_power(transition_matrix, num_steps)
    state_probabilities = np.dot(initial_state_prob_vector, transition_matrix_power_n)
    return state_probabilities

num_steps = int(input("Enter the number of steps you want to calculate the state probability for: "))
state_probabilities = state_probabilities_after_n_steps(Transition_prob_matrix, initial_state_prob_vector, num_steps)
print(f"State probabilities after {num_steps} steps:")
print(state_probabilities)
