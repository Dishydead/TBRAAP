import scipy.special

z = -5 * (2.71828 ** -5)  # Compute -5 e^(-5)
W_value = scipy.special.lambertw(z, k=-1).real  # Use the lower branch (k=-1)
print(W_value)