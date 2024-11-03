from math import gcd

def LCG_generator(m, a, c, seed):
    x = seed
    while True:
        x = (a * x + c) % m
        yield x

def is_primitive_root(a, m):
    if gcd(a, m) != 1:
        return False
    phi = sum(gcd(i, m) == 1 for i in range(1, m))
    return all(pow(a, (m-1)//p, m) != 1 for p in range(2, m) if (m-1) % p == 0)

def find_the_a_for_max_period(m):
    for a in range(2, m):
        if is_primitive_root(a, m):
            return a
    return None

def combined_LCG(m1, m2, m3, a1, a2, a3, c1, c2, c3, seed):
    lcg1 = LCG_generator(m1, a1, c1, seed)
    lcg2 = LCG_generator(m2, a2, c2, seed)
    lcg3 = LCG_generator(m3, a3, c3, seed)
    m = m1 * m2 * m3
    while True:
        x1, x2, x3 = next(lcg1), next(lcg2), next(lcg3)
        yield (x1 * (m // m1) * pow(m // m1, -1, m1) +
               x2 * (m // m2) * pow(m // m2, -1, m2) +
               x3 * (m // m3) * pow(m // m3, -1, m3)) % m

def find_period(generator):
    seen = {}
    x = next(generator)
    period = 0
    while x not in seen:
        seen[x] = period
        x = next(generator)
        period += 1
        if period > 100000:
            return 0
    return period

def find_moduli_and_parameters():
    alpha = 1
    for m1 in range(2, 100):
        for m2 in range(m1 + 1, 100):
            if gcd(m1, m2) != 1:
                continue
            for m3 in range(m2 + 1, 100):
                if gcd(m1, m3) != 1 or gcd(m2, m3) != 1:
                    continue
                if m1 * m2 * m3 <= 30000:
                    continue
                a1 = find_the_a_for_max_period(m1)
                a2 = find_the_a_for_max_period(m2)
                a3 = find_the_a_for_max_period(m3)
                if a1 and a2 and a3:
                    lcg = combined_LCG(m1, m2, m3, a1, a2, a3, 1, 1, 1, 1)
                    period = find_period(lcg)
                    if (period > 30000):
                        return m1, m2, m3, a1, a2, a3, period
    return None

print(178 % 9)
result = find_moduli_and_parameters()
if result:
    m1, m2, m3, a1, a2, a3, period = result
    print(f"Suitable moduli: {m1}, {m2}, {m3}")
    print(f"Suitable multipliers: {a1}, {a2}, {a3}")
    print([period])
else:
    print("No suitable parameters found")