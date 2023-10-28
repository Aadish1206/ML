def countEqualRowColumnPairs(grid):
    count = 0
    n = len(grid)
    #print(n)

    for i in range(n):
        for j in range(n):
            equal = True

            for k in range(n):
                if grid[i][k] != grid[k][j]:
                    equal = False
                    break

            if equal:
                count += 1

    return count


grid1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
grid2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]

result1 = countEqualRowColumnPairs(grid1)
result2 = countEqualRowColumnPairs(grid2)

print("Output for grid1:", result1)  
print("Output for grid2:", result2)  
