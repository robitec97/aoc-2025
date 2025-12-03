import bisect

def generate_invalid_ids(max_R: int):
    
    invalid = set()
    max_digits = len(str(max_R))

    # d = length of the repeating block
    for d in range(1, max_digits // 2 + 1):
        start = 10 ** (d - 1)   # smallest d-digit block (no leading zero)
        end = 10 ** d           # one past the largest d-digit block

        # t = how many times the block is repeated (at least 2)
        # total length = d * t must be <= max_digits
        max_t = max_digits // d
        for t in range(2, max_t + 1):
            for h in range(start, end):
                # Build the repeated number as digits
                s = str(h)
                n = int(s * t)
                if n > max_R:
                    # As h increases, n increases; we can stop this loop
                    break
                invalid.add(n)

    # Return them sorted so we can binary-search and prefix-sum
    return sorted(invalid)


def main():
    # Read the single line of ranges from input.txt
    with open("input.txt", "r") as f:
        line = f.read().strip()

    ranges = []
    for part in line.split(","):
        part = part.strip()
        if not part:
            continue
        a_str, b_str = part.split("-")
        L, R = int(a_str), int(b_str)
        ranges.append((L, R))

    # We only need invalid IDs up to the maximum R
    max_R = max(R for _, R in ranges)

    invalid_ids = generate_invalid_ids(max_R)

    # Build prefix sums over the sorted invalid IDs
    prefix = [0]
    for x in invalid_ids:
        prefix.append(prefix[-1] + x)

    total_sum = 0
    for L, R in ranges:
        # Find indices of invalid_ids within [L, R]
        i = bisect.bisect_left(invalid_ids, L)
        j = bisect.bisect_right(invalid_ids, R)
        total_sum += prefix[j] - prefix[i]

    print(total_sum)


if __name__ == "__main__":
    main()
