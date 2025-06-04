import random
import numpy as np
from scipy.optimize import fsolve
from math_tools import *

def generate_binary_list(N):
    """Generates a random binary list of size N."""
    return [random.randint(0, 1) for _ in range(N)]

def calculate_error_rate(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")

    mismatches = sum(b1 != b2 for b1, b2 in zip(list1, list2))
    return mismatches / len(list1) if list1 else 0.0
    
def parameter_estimation(key_A, key_B, M):
    """
    Randomly samples and removes M bits from both key_A and key_B to estimate error rate.
    
    Args:
        key_A (list of int): Alice's key.
        key_B (list of int): Bob's key.
        M (int): Number of bits to sample for estimation.
    
    Returns:
        (key_A_remaining, key_B_remaining, estimated_error): 
            The remaining keys and the error rate from the sampled bits.
    """
    if len(key_A) != len(key_B):
        raise ValueError("Keys must be of the same length.")
    if M > len(key_A):
        raise ValueError("Cannot sample more bits than available.")

    indices = random.sample(range(len(key_A)), M)
    #print(len(indices))
    sampled_A = [key_A[i] for i in indices]
    sampled_B = [key_B[i] for i in indices]
    estimated_error = calculate_error_rate(sampled_A, sampled_B)
    #print(estimated_error)
    #print(len(key_A))
    # Remove sampled bits (from high to low index to avoid shifting)
    for i in sorted(indices, reverse=True):
        key_A.pop(i)
        key_B.pop(i)
    return key_A, key_B, estimated_error

def apply_loss_and_noise(N, P_loss, P_noise, mf, strategy, 
                         eps = 0.1, alpha = 3, beta = 20):
    """
    Simulates loss and noise on a copy of the binary list.
    
    - Each bit is independently removed with probability P_loss.
    - If not removed, it is flipped (XORed with 1) with probability P_noise.
    - If removed from the copy, also remove from the original.
    
    Returns:
        modified_original: list with elements removed
        modified_copy: noisy copy with matching removals
    """
    key_A = generate_binary_list(N)
    bases_A = generate_binary_list(N)
    bases_B = generate_binary_list(N)
    modified_key_A = []
    modified_key_B = []

    for j, bit in enumerate(key_A):
        if random.random() < P_loss:
            # Simulate loss: skip both original and copy
            continue
        else:
            if bases_A[j] == bases_B[j]:
                # Keep bit, apply noise
                noisy_bit = bit ^ (random.random() < P_noise)
                modified_key_A.append(bit)
                modified_key_B.append(noisy_bit)

    #print(len(modified_key_A))
    intermediate_length = len(modified_key_A) #n
    p = 0.5 * (1 - P_loss)
    C_q = 3
    if strategy == 1 or strategy == 0.5:
        g = eps * (1 + alpha*10**(-beta*P_noise))
        A = int(1/g**2*(1/P_noise - 1)) #A
        M_estimate = A
        if strategy == 0.5:
            lf = (mf + 6 + 4*np.log2(mf/0.01))/(1 - 2.27*H(P_noise))
            def equation(x, C_q, p, l, A):
                return x**3 - C_q*np.sqrt(1 - p)*x**2 - (lf + A)*x + 0.5 * A*C_q*np.sqrt(1 - p)
            D = 0.25 * (C_q*np.sqrt(1 - p) + np.sqrt(C_q*C_q*(1 - p) + 4*(lf + A)))**2
            n0 = max(2*A, D) #initial guess
            solution = fsolve(lambda x: equation(x, C_q, p, lf, A), n0)
            n_lim = solution[0]**2
            nf = max(n_lim, 4*A*A/n_lim)
            M_estimate = A / np.sqrt(nf) *np.sqrt(intermediate_length)
        
    else:
        M_estimate = intermediate_length*strategy
    
    final_key_A, final_key_B, estimated_error = parameter_estimation(modified_key_A, modified_key_B, int(M_estimate))
    return final_key_A, final_key_B, estimated_error, intermediate_length, M_estimate

def fake_QKD(N, P_loss, P_noise, mf, strategy):
    final_key_A, final_key_B, estimated_error, intermediate_length, M_estimate = apply_loss_and_noise(N, P_loss, P_noise, mf = mf, strategy = strategy)
    
    #Information reconciliation. We use expected efficiency (upper threshold), and expected QBER 
    expected_leakage = 1.27 * len(final_key_A) * H(P_noise)
    
    #Privacy amplification
    l = len(final_key_A)
    k = l - expected_leakage - l * H(P_noise)
    #print("Fake k", k)
    final_length = int(m_solution(k)) # k = len(final_key_A) * (1 - (1 + efficiency)*H(P_noise)) - 6 - 4*np.log2()
    final_shared_key = generate_binary_list(final_length)

    print("fake QBER", P_noise)
    return final_shared_key, l, M_estimate
