from copy import deepcopy


with open(file='data.txt') as file:
    data = []
    for r, row in enumerate(file.read().split("\n")):  # creates grid
        data.append([])
        for c, col in enumerate(row):
            data[r].append(int(col))


ROW_LENGTH = len(data[0])
COL_LENGTH = len(data)


class BinaryDiagnosticTool:
    def __init__(self, grid):
        self.grid = grid
        self.gamma_epsilon_rating()
        self.oxygen_rating(deepcopy(self.grid), 0)
        self.co2_rating(deepcopy(self.grid), 0)

    def gamma_epsilon_rating(self):
        gamma_rate, epsilon_rate = "", ""

        for j in range(ROW_LENGTH):
            counts = {0: 0, 1: 0}
            for i in range(COL_LENGTH):
                counts[self.grid[i][j]] += 1

            if counts[0] > counts[1]:
                gamma_rate += str(0)
                epsilon_rate += str(1)
            else:
                epsilon_rate += str(0)
                gamma_rate += str(1)

        self.convert_binary_to_decimal(gamma_rate, epsilon_rate)

    def convert_binary_to_decimal(self, binary_one, binary_two):
        decimal_one, decimal_two = int(binary_one, 2), int(binary_two, 2)
        return print(decimal_one * decimal_two)

    def co2_rating(self, grid_copy, j):  # j == column index
        if len(grid_copy) == 1:
            return print("".join([str(i) for i in grid_copy[0]]))

        counts, even_counts = {0: 0, 1: 0}, False
        invalid_indices = []
        for i in range(len(grid_copy)):
            counts[grid_copy[i][j]] += 1

        if counts[0] == counts[1]:
            even_counts = True

        for k in range(len(grid_copy)):
            if even_counts and grid_copy[k][j] != 0:
                invalid_indices.append(k)
            elif counts[0] < counts[1] and grid_copy[k][j] != 0:
                invalid_indices.append(k)
            elif counts[1] < counts[0] and grid_copy[k][j] != 1:
                invalid_indices.append(k)

        for index in invalid_indices[::-1]:
            del grid_copy[index]

        self.co2_rating(grid_copy, j + 1)

    def oxygen_rating(self, grid_copy, j):  # j == column index
        if len(grid_copy) == 1:
            return print("".join([str(i) for i in grid_copy[0]]))

        counts, even_counts = {0: 0, 1: 0}, False
        invalid_indices = []
        for i in range(len(grid_copy)):
            counts[grid_copy[i][j]] += 1

        if counts[0] == counts[1]:
            even_counts = True

        for k in range(len(grid_copy)):
            if even_counts and grid_copy[k][j] != 1:
                invalid_indices.append(k)
            elif counts[0] > counts[1] and grid_copy[k][j] != 0:
                invalid_indices.append(k)
            elif counts[1] > counts[0] and grid_copy[k][j] != 1:
                invalid_indices.append(k)

        for index in invalid_indices[::-1]:
            del grid_copy[index]

        self.oxygen_rating(grid_copy, j + 1)


bd = BinaryDiagnosticTool(data)
