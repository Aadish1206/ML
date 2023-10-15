def maxArea(height):
    area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        h1 = height[left]
        h2 = height[right]
        width = right - left
        #print(width)
        current= min(h1, h2) * width
        #print(current)
        area = max(area, current)
        #print(area)

        if h1 < h2:
            left += 1
        else:
            right -= 1

    return area


height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height1))  

height2 = [1, 2, 4, 9, 8, 5]
print(maxArea(height2)) 


#This problem is about finding the maximum amount of water that can be contained by two vertical lines and the x-axis. You're given an array called "height," where each element represents the height of a vertical line at a particular position.

#For example, if the input array is [1, 8, 6, 2, 5, 4, 8, 3, 7], it means that there are vertical lines of different heights at positions 1 to 9. The problem asks you to find the two vertical lines (represented by two heights) that, along with the x-axis, form a container that can hold the most water. The width of the container is determined by the distance between the two lines, and the height of the container is determined by the shorter of the two lines.

#The goal is to maximize the area of this container. To solve this, you use a two-pointer approach, where you start with two pointers at the beginning and end of the array. You calculate the area between the lines indicated by the two pointers, and then you move the pointer pointing to the shorter line toward the center to check for a potentially larger area. You repeat this process until the two pointers meet, calculating and updating the maximum area as you go. This technique is used to efficiently find the largest area while avoiding the need to check all possible pairs of lines, which would be less efficient.

#In the end, you return the maximum area found, which represents the largest amount of water that can be contained by any two vertical lines and the x-axis in the array.
