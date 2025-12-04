def read_grid(filename: str = "input.txt"):
    grid = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line:  # skip empty lines
                grid.append(list(line))
    return grid


def count_adjacent_rolls(grid, r, c) -> int:
    rows = len(grid)
    # directions for 8 neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    adj = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
            if grid[nr][nc] == "@":
                adj += 1
    return adj


def total_removable_rolls(filename: str = "input.txt") -> int:
    grid = read_grid(filename)
    if not grid:
        return 0

    total_removed = 0

    while True:
        to_remove = []

        # Find all rolls currently accessible
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] != "@":
                    continue
                adj = count_adjacent_rolls(grid, r, c)
                if adj < 4:
                    to_remove.append((r, c))

        # If none are accessible, we're done
        if not to_remove:
            break

        # Remove them all simultaneously
        for r, c in to_remove:
            grid[r][c] = "."

        total_removed += len(to_remove)

    return total_removed


if __name__ == "__main__":
    result = total_removable_rolls("input.txt")
    print(result)
