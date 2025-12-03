def main():
    MOD = 100
    dial = 50  # starting position
    zero_clicks = 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            start = dial
            d = distance

            # Count how many times we land on 0 during this rotation
            if direction == 'R':  # moving +1 each click
                # first k in [1..] such that (start + k) % 100 == 0
                first_k = (MOD - start) % MOD
                if first_k == 0:
                    first_k = MOD  # k can't be 0; next time around is 100
            elif direction == 'L':  # moving -1 each click
                # first k in [1..] such that (start - k) % 100 == 0
                first_k = start % MOD
                if first_k == 0:
                    first_k = MOD
            else:
                raise ValueError(f"Invalid direction in line: {line}")

            if first_k <= d:
                # One hit at first_k, then every extra 100 steps
                zero_clicks += 1 + (d - first_k) // MOD

            # Update dial position after the full rotation
            if direction == 'R':
                dial = (dial + d) % MOD
            else:  # 'L'
                dial = (dial - d) % MOD

    print(zero_clicks)


if __name__ == "__main__":
    main()
