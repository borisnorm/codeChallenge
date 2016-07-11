#given a matrix, start path and end path see if there is a path that goes
#down along the way


class Solution:

    def get_down_neighbors(x, y, matrix):
        temp = [(x-1, y), (x+1, y), (x, y-1), (x, y + 1)]
        neighbors = []
        for item in temp:
            x, y = item[0], item[1]
            if x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[0]):
                if (i != x and j != y) and (matrix[i][j] < matrix[x][y]):
                    neighbors.append(matrix[i][j], x, y)
        return neighbors


    def path_finder(matrix, sX, sY, endX, endY, visited, status):
        if sX == endX and sY == endY:
            status = True
            return
        if (len(visited) >= len(matrix) * len(matrix):
            return
        source = (sX, sY)
        neighbors = get_down_neighbors(sX, sY, matrix)
        for item in neighbors:
            path_finder(matrix, item[1], item[2], endX, endY, visited.add((sX, sY)), statu)


    def solution(matrix, sX, sY, endX, endY):
        status = False
        for item in get_down_neighbor:
            visited = set()
            path_finder(matrix, item[1], item[2], endX, endY, visited.add((sX, sY))
        return Status
