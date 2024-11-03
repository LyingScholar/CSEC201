# import numpy as np
# import scipy as sp

# # recursively definied sterling function
# def stirling_num(n, k):
#     if k == 0 and n == 0:
#         return 1
#     elif k == 0 or k > n:
#         return 0
#     elif k == n:
#         return 1
#     return k * stirling_num(n - 1, k) + stirling_num(n - 1, k - 1)

# def digit_pair_freq(s):
#     pair_frequencies = {str(i).zfill(2): 0 for i in range(100)}
#     n = len(s)
#     if n % 2:  # if odd length, ignore last digit
#         n -= 1


#     for i in range(0, n // 2):
#         pair = s[2*i:2*i+2]
#         if pair in pair_frequencies:
#             pair_frequencies[pair] += 1
#         else:
#             pair_frequencies[pair] = 1
    
#     return pair_frequencies

# def chi_square_uniform(observed):
#     total_observed = sum(observed)
#     num_categories = len(observed)
#     expected = total_observed / num_categories
#     chi_square = sum((obs - expected)**2 / expected for obs in observed)
#     return chi_square


# def chi_square_poker_test(s):
#     freq = digit_pair_freq(s)
#     chi_square_stat = chi_square_uniform(list(freq.values()))
    
#     #alternate method to find critical value for 95% at 4 degrees of freedom
#     # chi_square_crit_val = sp.stats.chi2.isf(0.05, 4, loc=0, scale=1)
#     chi_square_crit_val = 9.488
    
#     print("Chi-Square Statistic:", chi_square_stat)
#     if chi_square_stat < chi_square_crit_val:
#         print("FAIL to reject: Data PASSES")
#     else:
#         print("REJECTED Null hypothesis: Data FAILS")


# def lcg(seed, a, c, m, n):
#     numbers = []
#     x = seed
#     for i in range(n):
#         x = (a * x + c) % m
#         numbers.append(x)
#     return numbers

# def transform_to_digits(numbers, m):
#     return ''.join(str(int((i / m) * 10)) for i in numbers)
    
# seed = 12345
# a = 1664525
# c = 1013904223
# m = 2**32
# n = 1000
# random_numbers = lcg(seed, a, c, m, 1000)
# digits_string = transform_to_digits(random_numbers, m)
# chi_square_poker_test(digits_string)
# import numpy as np
# import scipy.stats as stats

# def generate_lcg_values(a, m, seed, n):
#     values = []
#     x = seed
#     for _ in range(n):
#         x = (a * x) % m
#         values.append(x)
#     return values

# def combine_lcgs(values1, values2, values3, mod1):
#     combined_values = []
#     for x1, x2, x3 in zip(values1, values2, values3):
#         y = (x1 - x2 + x3) % mod1
#         combined_values.append(y)
#     return combined_values

# def scale_to_digits(values, m1, num_bins):
#     digits = [int((x / m1) * num_bins) for x in values]
#     # Ensure digits are within the correct range
#     digits = [min(d, num_bins - 1) for d in digits]
#     return digits

# def chi_square_serial_test(digits, num_bins):
#     pairs = [(digits[i], digits[i+1]) for i in range(len(digits)-1)]
#     observed_freq = np.zeros((num_bins, num_bins), dtype=int)
#     for x, y in pairs:
#         observed_freq[x, y] += 1

#     num_pairs = len(pairs)
#     expected_freq = np.full((num_bins, num_bins), num_pairs / (num_bins ** 2))

#     observed = observed_freq.flatten()
#     expected = expected_freq.flatten()

#     # Apply Chi-Square test
#     chi_square_stat = ((observed - expected) ** 2 / expected).sum()
#     degrees_of_freedom = (num_bins ** 2) - 1
#     critical_value = stats.chi2.ppf(0.95, degrees_of_freedom)
#     return chi_square_stat, critical_value, degrees_of_freedom

# # Parameters
# m1, a1 = 32363, 157
# m2, a2 = 31727, 146
# m3, a3 = 31657, 142
# seed = 123  # Arbitrary seed
# n = 500
# num_bins = 5  # Reduced number of bins

# # Generate sequences
# values1 = generate_lcg_values(a1, m1, seed, n)
# values2 = generate_lcg_values(a2, m2, seed, n)
# values3 = generate_lcg_values(a3, m3, seed, n)

# # Combine sequences
# combined_values = combine_lcgs(values1, values2, values3, m1 - 1)
# digits = scale_to_digits(combined_values, m1, num_bins)

# # Perform Chi-Square Serial Test on pairs
# chi_square_stat, critical_value, degrees_of_freedom = chi_square_serial_test(digits, num_bins)

# print(f"Chi-Square Statistic: {chi_square_stat}")
# print(f"Critical Value (95% confidence level): {critical_value}")
# print(f"Degrees of Freedom: {degrees_of_freedom}")

# if chi_square_stat < critical_value:
#     print("Failed to reject the null hypothesis.")
# else:
#     print("Rejected the null hypothesis.")


# LCG parameters
# m = 2**31 - 1  # Modulus
# a = 16807      # Multiplier
# c = 0          # Increment
# seed = 123456789  # Seed value

# def digits_to_bits(s):
#     bitsy = ''.join(['1' if int(digit) >= 5 else '0' for digit in s])
#     return bitsy
    

# def count_runs(bit_string):
#     runs_of_0 = 0
#     runs_of_1 = 0
#     bitie = bit_string[0]
#     if bitie == '0':
#         runs_of_0 += 1
#     else:
#         runs_of_1 += 1
    
#     for bit in bit_string[1:]:
#         if bit != bitie:
#             bitie = bit
#             if bitie == '0':
#                 runs_of_0 += 1
#             else:
#                 runs_of_1 += 1
                
#     return runs_of_0, runs_of_1

# def runs_test(bit_string):
#     N = len(bit_string)
#     n1 = bit_string.count('0')
#     n2 = bit_string.count('1')

#     #making sure test can actually be run on the string
#     if n1 == 0 or n2 == 0:
#         return {
#             'Runs': None,
#             'Expected Runs (mean)': None,
#             'Variance': None,
#             'Z-value': None,
#             'Result': "Test not applicable."
#         }
    

#     runs = 1
#     for i in range(1, N):
#         if bit_string[i] != bit_string[i - 1]:
#             runs += 1
    
#     # Expected or mean runs and variance
#     mean_runs = ((2 * n1 * n2) / N) + 1
#     variance_runs = (2 * n1 * n2 * (2 * n1 * n2 - N)) / (N**2 * (N - 1))
#     Z = (runs - mean_runs) / ((variance_runs)**(1/2))
    
    
#     critical_value = 1.96  # For 95% confidence level (two-tailed)
#     if abs(Z) < critical_value:
#         result = "Accepted the null hypothesis: sequence is random."
#     else:
#         result = "Rejected the null hypothesis: sequence  not random."
    
#     return {
#         'Runs': runs,
#         'Expected Runs (mean)': mean_runs,
#         'Variance': variance_runs,
#         'Z-value': Z,
#         'Result': result
#     }


# def generate_digits_LCG(seed, a, c, m, n):
#     """
#     Generates 'n' digits (0-9) using an LCG and the transformation ⌊(x/m)*10⌋.
#     """
#     x = seed
#     digits = ''
#     for _ in range(n):
#         x = (a * x + c) % m
#         digit = int((x / m) * 10)
#         digits += str(digit)
#     return digits

# # Generate 1000 digits using the LCG
# digits_string = generate_digits_LCG(seed, a, c, m, 1000)

# # Convert digits to bits
# bit_string = digits_to_bits(digits_string)

# # Perform the Runs test
# test_result = runs_test(bit_string)

# # Output the test results
# print("Runs Test Result:")
# print(f"Number of runs: {test_result['Runs']}")
# print(f"Expected number of runs: {test_result['Expected Runs (mean)']}")
# print(f"Variance of runs: {test_result['Variance']}")
# print(f"Z-value: {test_result['Z-value']}")
# print(f"Conclusion: {test_result['Result']}")



import numpy as np
import scipy.stats as stats

# Recursively defined Stirling function
def stirling_num(n, k):
    if n == k == 0:
        return 1
    elif k == 0 or k > n:
        return 0
    elif k == n:
        return 1
    else:
        return k * stirling_num(n - 1, k) + stirling_num(n - 1, k - 1)

def poker_test_counts(s):
    n = len(s)
    num_groups = n // 5
    counts = [0] * 5  # For categories with 1 to 5 distinct digits

    for i in range(num_groups):
        group = s[i*5:(i+1)*5]
        distinct_digits = len(set(group))
        if 1 <= distinct_digits <= 5:
            counts[distinct_digits - 1] += 1

    return counts

def calculate_probabilities():
    d = 10  # Number of possible digits (0-9)
    k = 5   # Size of each group
    p = []
    for r in range(1, 6):
        numerator = np.math.factorial(d) / np.math.factorial(d - r) * stirling_num(k, r)
        denominator = d ** k
        pr = numerator / denominator
        p.append(pr)
    return p

def chi_square_poker_test(s):
    observed_counts = poker_test_counts(s)
    n = sum(observed_counts)
    p = calculate_probabilities()
    expected_counts = [n * pi for pi in p]

    chi_square_stat = sum((obs - exp)**2 / exp for obs, exp in zip(observed_counts, expected_counts))

    degrees_of_freedom = len(observed_counts) - 1  # 5 categories - 1
    chi_square_crit_val = stats.chi2.ppf(0.95, degrees_of_freedom)

    print("Chi-Square Statistic:", chi_square_stat)
    if chi_square_stat < chi_square_crit_val:
        print("FAIL to reject: Data PASSES")
    else:
        print("REJECTED Null hypothesis: Data FAILS")


seed = 12345
a = 1664525
c = 1013904223
m = 2**32
n = 1000  # Number of digits should be a multiple of 5

def lcg(seed, a, c, m, n):
    numbers = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x)
    return numbers

def transform_to_digits(numbers, m):
    return ''.join(str(int((i / m) * 10)) for i in numbers)
    
def main():
    random_numbers = lcg(seed, a, c, m, n)
    digits_string = transform_to_digits(random_numbers, m)
    chi_square_poker_test(digits_string)

main()
