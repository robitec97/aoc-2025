def max_bank_joltage(bank: str) -> int:
    bank = bank.strip()
    max_joltage = -1
    best_right_digit = -1  # max digit to the right of current position

    # Scan from right to left so we always know the best possible ones digit to the right
    for i in range(len(bank) - 1, -1, -1):
        d = int(bank[i])

        # If there is at least one digit to the right, try forming a 2-digit number
        if best_right_digit != -1:
            candidate = 10 * d + best_right_digit
            if candidate > max_joltage:
                max_joltage = candidate

        # Update the best right-side digit
        if d > best_right_digit:
            best_right_digit = d

    return max_joltage


def main():
    total = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += max_bank_joltage(line)

    print(total)


if __name__ == "__main__":
    main()
