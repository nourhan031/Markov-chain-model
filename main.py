import input_functions
import analysis

Transition_prob_matrix = input_functions.input_transition_prob_matrix()
initial_state_prob_vector = input_functions.input_initial_state_prob_vector()
state_steps = input_functions.input_state_steps()

print("************************************************************************************************************")

analysis.is_reachable(Transition_prob_matrix, state_steps)

print("************************************************************************************************************")

analysis.is_closed(Transition_prob_matrix, state_steps)

print("************************************************************************************************************")

analysis.is_absorbing(Transition_prob_matrix, state_steps)

print("************************************************************************************************************8")

analysis.is_periodic(Transition_prob_matrix, state_steps)

print("************************************************************************************************************8")

num_steps = int(input("Enter the number of steps you want to calculate the state probability for: "))
state_probabilities = analysis.state_probabilities_after_n_steps(Transition_prob_matrix, initial_state_prob_vector, num_steps)
print(f"State probabilities after {num_steps} steps:")
print(state_probabilities)
