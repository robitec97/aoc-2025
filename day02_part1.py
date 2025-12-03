def sum_invalid_in_range(L: int, R: int) -> int:
    
    total = 0
    max_digits = len(str(R))

    # k = number of digits in the half H
    for k in range(1, max_digits // 2 + 1):
        m = 10 ** k + 1        # N = H * (10^k + 1)
        h_min = 10 ** (k - 1)  # smallest k-digit number (no leading zero)
        h_max = 10 ** k - 1    # largest k-digit number

        # Quick exit: if even the smallest possible N with this k is > R, we're done
        if h_min * m > R:
            break

        # For N in [L, R], we need H in [ceil(L/m), floor(R/m)]
        h_lo_by_L = (L + m - 1) // m   # ceil(L / m)
        h_hi_by_R = R // m             # floor(R / m)

        # Intersect with the valid k-digit H range
        lb = max(h_lo_by_L, h_min)
        ub = min(h_hi_by_R, h_max)

        if lb <= ub:
            n = ub - lb + 1
            # Sum of H from lb to ub is n * (lb + ub) // 2
            # Sum of N = m * sum(H)
            total += m * n * (lb + ub) // 2

    return total


def main():
    # Read the single-line input with comma-separated ranges
    with open("input.txt", "r") as f:
        line = f.read().strip()

    total_sum = 0
    for part in line.split(","):
        part = part.strip()
        if not part:
            continue
        a_str, b_str = part.split("-")
        L, R = int(a_str), int(b_str)
        total_sum += sum_invalid_in_range(L, R)

    print(total_sum)


if __name__ == "__main__":
    main()
