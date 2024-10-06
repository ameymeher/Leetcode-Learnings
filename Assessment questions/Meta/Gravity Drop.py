def get_min_obstacles(grid):
    from collections import defaultdict

    min_moves = float('inf')
    obstacle_map = defaultdict(int)
    m,n = len(grid), len(grid[0])

    for j in range(n):
        curr_moves = 0
        for i in range(m):
            if grid[i][j] == "*":
                curr_moves = 0
            else:
                curr_moves +=1
                if grid[i][j] == '@':
                    obstacle_map[curr_moves] +=1

        min_moves = min(min_moves,curr_moves)

    print(f"Number of obstacles to be removed after the number of steps performed")
    print(obstacle_map)

    ans = 0

    for i in range(min_moves+1):
        ans += obstacle_map[i]

    print(f"Minimum obstacles to remove: {ans}")

    return ans


grid = [["*","*","*"],
        ["@","*","*"],
        ["*","*"," "],
        [" "," "," "],
        [" ","@","@"]]

get_min_obstacles(grid)