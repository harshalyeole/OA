# A pilot was asked to drop food packets in a terrain. He must fly over the entire terrain only once but cover a maximum number of drop points.
# The points are given as inputs in the form of integer co-ordinates in a two-dimensional field. The flight path can be horizontal or vertical, but not a mix of the two or diagonal.
# Write an algorithm to find the maximum number of drop points that can be covered by flying over the terrain once.

# Input
# The first line of input consists of an integer- Coordinate_size, representing the number of x coordinates (N).
# The next line consists of N space-separated integers representing the × coordinates.
# The third line consists of an integer-Coordinate_size, representing the number of y coordinates (M).
# The next line consists of M space-separated integers representing the y coordinates.

# Output
# Print an integer representing the number of coordinates in the best path which covers the maximum number of dron points by flying over the terrain once.

# Note
# A path is valid path if, more than one drop points are connected (Single coordinate don't create any path, so pilot cannot fly over it).

# Example
# Input:
# 5
# 2 3 2 4 2
# 5
# 2 2 6 5 8
# Output:
# 3
# Explanation:
# There are 5 coordinates- (2,2), (3,2), (2,6), (4,5) and (2,8).
# The best path is the horizontal one covering (2,2), (2,6) and (2,8).
# So, the output is 3.

def funcDrop(xCoordinate, yCoordinate):
    ans = 1
    for i in range(len(xCoordinate)):
        time = 1
        for j in range(i + 1, len(xCoordinate)):
            if xCoordinate[i] == xCoordinate[j]:
                time += 1
        if time > ans:
            ans = time
    for i in range(len(yCoordinate)):
        time = 1
        for j in range(i+1, len(yCoordinate)):
            if yCoordinate[i] == yCoordinate[j]:
                time+=1
        if time > ans : 
            ans = time
    return ans

def main():
    xCordinate = []
    #Same the xcorrdinate size is not reqired
    xCordinate = list(map(int,input("First put the xcordinates --> ").split()))

    yCordinate = []
    #Same the ycorrdinate size is not reqired
    yCordinate = list(map(int,input("Put the ycordinates --> ").split()))

    result = funcDrop(xCordinate, yCordinate)
    print(result)

if __name__ == "__main__":
    main()