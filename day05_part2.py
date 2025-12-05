def read_ranges(filename: str = "input.txt") -> List[Tuple[int, int]]:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # Split into the two sections
    parts = content.split("\n\n")
    if len(parts) < 1:
        raise ValueError("Input file format not recognized.")

    range_lines = [line.strip() for line in parts[0].splitlines() if line.strip()]

    ranges = []
    for line in range_lines:
        start, end = map(int, line.split("-"))
        if start > end:
            start, end = end, start  # normalize
        ranges.append((start, end))

    return ranges


def merge_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not ranges:
        return []

    ranges.sort()
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # overlap or touching
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def count_total_fresh_ids(filename: str = "input.txt") -> int:
    ranges = read_ranges(filename)
    merged = merge_ranges(ranges)

    total_ids = 0
    for start, end in merged:
        total_ids += (end - start + 1)  # inclusive range count

    return total_ids


def main():
    print(count_total_fresh_ids("input.txt"))


if __name__ == "__main__":
    main()
