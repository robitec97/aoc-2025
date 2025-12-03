def main():
    dial = 50          # starting position
    MOD = 100          # dial has numbers 0-99
    zero_count = 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            direction = line[0]
            distance = int(line[1:])

            if direction == 'L':
                dial = (dial - distance) % MOD
            elif direction == 'R':
                dial = (dial + distance) % MOD
            else:
                raise ValueError(f"Invalid direction in line: {line}")

            if dial == 0:
                zero_count += 1

    print(zero_count)


if __name__ == "__main__":
    main()