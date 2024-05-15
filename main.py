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
    for state_id, num_steps in state_steps.items():
        for i in range(len(transition_matrix)):
            transition_prob = transition_matrix[state_id][i]
            probability_after_steps = transition_prob ** num_steps
            reachable_str = "(reachable) and (irreducible)" if probability_after_steps > 0 else "(unreachable)"
            print(f"Transition probability from state {state_id} to state {i} raised to the power of {num_steps} = {probability_after_steps} {reachable_str}")
is_reachable(Transition_prob_matrix, state_steps)

print("************************************************************************************************************8")

def is_closed(transition_matrix, state_steps):
    print("A state is closed if P[i][j] = 0")
    for state_id, num_steps in state_steps.items():
        for i in range(len(transition_matrix)):
            transition_prob = transition_matrix[state_id][i]
            closed_str = "(closed)" if transition_prob == 0 else ""
            print(f"Transition probability from state {state_id} to state {i} = {transition_prob} {closed_str}")
is_closed(Transition_prob_matrix, state_steps)

print("************************************************************************************************************8")

def is_absorbing(transition_matrix, state_steps):
    print("A state is absorbing if P[i][i] = 1")
    for state_id, num_steps in state_steps.items():
        for i in range(len(transition_matrix)):
            transition_prob = transition_matrix[state_id][i]
            if i == state_id and transition_prob == 1:
                absorbing_str = "(absorbing)"
            else:
                absorbing_str = ""
            print(f"Transition probability from state {state_id} to state {i} = {transition_prob} {absorbing_str}")
is_absorbing(Transition_prob_matrix, state_steps)

print("************************************************************************************************************8")


# OUTPUT1: MARKOV CHAIN CLASSIFICATION


# def is_recurrent():
#
#
# def is_transient():
#
#
# def is_periodic():
#
# def is_aperiodic():





# STEADY STATE STATES PROBABILITY (P)
# STATE PROBABILITIES AFTER N STEPS (P_N)
