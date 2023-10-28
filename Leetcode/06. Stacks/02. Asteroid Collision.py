def asteroidCollision(asteroids):
    stack = []

    for collision in asteroids:
        
        while stack and collision < 0 < stack[-1]:
            if stack[-1] < -collision:
                stack.pop()
                continue
            elif stack[-1] == -collision:
                stack.pop()
            break
        else:
            stack.append(collision)

    return stack


asteroids = [5, 10, -5]
result = asteroidCollision(asteroids)
print(result)
