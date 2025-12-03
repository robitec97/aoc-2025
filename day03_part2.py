def max_joltage_with_picks(bank: str, picks: int = 12) -> int:
    bank = bank.strip()
    n = len(bank)
    if n <= picks:
        # If there are <= picks digits, we just take them all
        return int(bank) if bank else 0

    # We need to remove exactly k digits to leave `picks` digits
    k = n - picks
    stack = []

    for ch in bank:
        # While we can still remove digits (k > 0) and
        # the last digit in stack is smaller than current,
        # pop it to maximize the resulting number.
        while k > 0 and stack and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)

    # If we still have more than `picks` digits, cut from the end
    result_digits = stack[:picks]
    return int("".join(result_digits))


def main():
    total = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += max_joltage_with_picks(line, picks=12)

    print(total)


if __name__ == "__main__":
    main()
