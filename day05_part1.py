def read_database(filename: str = "input.txt") -> tuple[list[tuple[int, int]], list[int]]:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # Split into two sections: ranges and ids
    parts = content.split("\n\n")
    if len(parts) != 2:
        raise ValueError("Input file must contain ranges, a blank line, then IDs.")

    range_lines = [line.strip() for line in parts[0].splitlines() if line.strip()]
    id_lines = [line.strip() for line in parts[1].splitlines() if line.strip()]

    ranges: List[Tuple[int, int]] = []
    for line in range_lines:
        # Expect "a-b"
        start_str, end_str = line.split("-")
        start = int(start_str)
        end = int(end_str)
        if start > end:
            start, end = end, start  # normalize if needed
        ranges.append((start, end))

    ids = [int(line) for line in id_lines]

    return ranges, ids


def merge_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not ranges:
        return []

    ranges.sort()  # sort by start, then end
    merged: List[Tuple[int, int]] = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:  # overlapping or touching
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def is_fresh(ingredient_id: int, merged_ranges: List[Tuple[int, int]]) -> bool:
    # Manual binary search on interval starts
    lo, hi = 0, len(merged_ranges) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        start, end = merged_ranges[mid]
        if ingredient_id < start:
            hi = mid - 1
        elif ingredient_id > end:
            lo = mid + 1
        else:
            # start <= ingredient_id <= end
            return True
    return False


def count_fresh_ingredients(filename: str = "input.txt") -> int:
    ranges, ids = read_database(filename)
    merged_ranges = merge_ranges(ranges)

    fresh_count = 0
    for ingredient_id in ids:
        if is_fresh(ingredient_id, merged_ranges):
            fresh_count += 1

    return fresh_count


def main():
    result = count_fresh_ingredients("input.txt")
    print(result)


if __name__ == "__main__":
    main()