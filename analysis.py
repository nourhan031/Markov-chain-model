import input_functions
from math import gcd
import numpy as np

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



def state_probabilities_after_n_steps(transition_matrix, initial_state_prob_vector, num_steps):
    transition_matrix_power_n = np.linalg.matrix_power(transition_matrix, num_steps)
    state_probabilities = np.dot(initial_state_prob_vector, transition_matrix_power_n)
    return state_probabilities