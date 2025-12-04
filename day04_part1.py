def count_accessible_rolls(filename: str = "input.txt") -> int:
    # Read grid from file
    grid = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line:  # skip empty lines if any
                grid.append(list(line))

    rows = len(grid)
    if rows == 0:
        return 0

    accessible = 0

    # Directions for the 8 neighbors around each cell
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for r in range(rows):
        cols = len(grid[r])
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            adj_rolls = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check bounds; allow non-perfect rectangles just in case
                if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
                    if grid[nr][nc] == "@":
                        adj_rolls += 1

            if adj_rolls < 4:
                accessible += 1

    return accessible


if __name__ == "__main__":
    result = count_accessible_rolls("input.txt")
    print(result)