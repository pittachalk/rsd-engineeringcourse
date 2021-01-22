import numpy as np

"""  Simplistic 1-dimensional diffusion model """




def simple_monte_carlo_1d(energy_function, starting_point, limit=100):
    import numpy as np
    current_state = np.array(starting_point)
    current_energy = energy_function(current_state)
    counter = 0
    while counter < limit:
        run_mc_step(current_state, current_energy, energy_function)
        print(current_state, current_energy)
        counter +=1
    

def run_mc_step(current_state, current_energy, energy_function):
    new_state = move_one_particle(current_state)
    new_energy = energy_function(new_state)

    if new_energy < current_energy:
        current_state = new_state
        current_energy = new_energy

    else:
        p0 = compute_p0(new_energy, current_energy)
        p1 = np.random.uniform()
        if p0 > p1:
            current_state = new_state
            current_energy = new_energy

    return current_state, current_energy

    

def compute_p0(new_energy, current_energy, beta=1, T=1):
    return np.exp(-1 * beta * (new_energy - current_energy))

def move_one_particle(density):
    n_elements = len(density) 
    element_to_move = np.random.randint(0, n_elements, size=1)

    # repeat until get a position with at least one particle
    while density[element_to_move] == 0:
        element_to_move = np.random.randint(0, n_elements, size=1)

    # particle moves from current position
    density[element_to_move] -= 1

    if element_to_move == 0: 
        density[element_to_move + 1] += 1 # leftmost can only move right
    elif element_to_move == n_elements - 1: 
        density[element_to_move - 1] += 1 # rightmost only left
    else: 
        # o/w both with equal probability
        if np.random.uniform() > 0.5:
            density[element_to_move + 1] += 1 
        else:
            density[element_to_move - 1] += 1 

    return density


def energy_function(density):
    """ 
    Energy associated with the diffusion model
        :Parameters:
        density: array of positive integers
            Number of particles at each position i in the array/geometry
    """
    from numpy import array, any, sum 

    # Make sure input is an numpy array
    density = array(density)

    # ...of the right kind (integer). Unless it is zero length, 
    #    in which case type does not matter.

    if density.dtype.kind != 'i' and len(density) > 0:
        raise TypeError("Density should be a array of *integers*.")
        # and the right values (positive or null)
    if any(density < 0): 
        raise ValueError("Density should be an array of *positive* integers.")
    if density.ndim != 1:
        raise ValueError("Density should be an a *1-dimensional*"+
                        "array of positive integers.")

    return sum(density * (density - 1)) 



starting_point_test =  np.array([0, 0, 3, 5, 8, 4, 2, 1])
simple_monte_carlo_1d(energy_function, starting_point_test)
