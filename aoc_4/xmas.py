def count_xmas(grid):
    def search_word(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if (
                nx < 0
                or ny < 0
                or nx >= len(grid)
                or ny >= len(grid[0])
                or grid[nx][ny] != word[i]
            ):
                return False
        return True

    word = "XMAS"
    count = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if search_word(x, y, dx, dy):
                    count += 1

    return count


# Import the grid from the file
with open("input.txt") as file:
    grid = file.read().splitlines()

# Count the occurrences of "XMAS"
result = count_xmas(grid)
print(f"Number of times 'XMAS' appears: {result}")
