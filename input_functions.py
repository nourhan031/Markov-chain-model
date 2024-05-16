def input_transition_prob_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    transition_prob_matrix = []
    for i in range(rows):
        while True:
            row = []
            for j in range(cols):
                element = float(input(f"Enter the element for row {i}, column {j}: "))
                row.append(element)
            if sum(row) == 1:
                transition_prob_matrix.append(row)
                break
            else:
                print(f"The elements of row {i} do not sum to 1. Please re-enter the row.")

    print("Transition probability matrix: ")
    for row in transition_prob_matrix:
        print(row)
    return transition_prob_matrix

def input_initial_state_prob_vector():
    size = int(input("Enter the size of the initial state probabilities vector: "))
    initial_state_prob_vector = []
    while True:
        initial_state_prob_vector = []
        for i in range(size):
            element = float(input(f"Enter the element for position {i}: "))
            initial_state_prob_vector.append(element)
        if sum(initial_state_prob_vector) == 1:
            break
        else:
            print("The elements of the vector do not sum to 1. Please re-enter the vector.")

    print("Initial state probability matrix: ", initial_state_prob_vector)
    return initial_state_prob_vector

def input_state_steps():
    rows = int(input("Enter the number of states: "))
    state_steps = {}
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
    return state_steps
