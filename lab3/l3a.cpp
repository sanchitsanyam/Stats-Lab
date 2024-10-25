import numpy as np
import matplotlib.pyplot as plt

# Observed data
observed_frequencies = np.array([36, 40, 22, 2])
n = 3  # Number of coins
total_trials = 100  # Total number of trials

# Step 1: Estimate probability of heads (p)
mean_heads = np.sum(observed_frequencies * np.arange(4)) / total_trials
p_estimated = mean_heads / n  # Estimate of p
print(f"Estimated Probability of Heads (p): {p_estimated:.4f}")

# Step 2: Define a function to compute factorial manually
def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

# Step 3: Define a function to compute binomial probability P(X = k)
def binomial_probability(n, k, p):
    comb = factorial(n) / (factorial(k) * factorial(n - k))  # nCk
    prob = comb * (p ** k) * ((1 - p) ** (n - k))
    return prob

# Step 4: Calculate expected frequencies using the binomial formula
expected_frequencies = np.zeros(4)

# Using for loop to calculate expected frequencies
for k in range(4):
    prob = binomial_probability(n, k, p_estimated)
    expected_frequencies[k] = total_trials * prob

# Print observed and expected frequencies
print("Observed Frequencies:", observed_frequencies)
print("Expected Frequencies:", expected_frequencies)

# Step 5: Plot observed vs expected frequencies
x = np.arange(4)

plt.bar(x - 0.2, observed_frequencies, width=0.4, label='Observed', color='blue')
plt.bar(x + 0.2, expected_frequencies, width=0.4, label='Expected', color='orange')

plt.xlabel('Number of Heads')
plt.ylabel('Frequency')
plt.xticks(x)
plt.legend()
plt.title('Observed vs Expected Frequencies')

# Step 6: Plot the binomial probability distribution
plt.figure()

# Using for loop to calculate probabilities for the plot
probs = np.zeros(4)
for k in range(4):
    probs[k] = binomial_probability(n, k, p_estimated)

plt.stem(x, probs, use_line_collection=True)

plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Binomial Probability Distribution')

plt.show()

