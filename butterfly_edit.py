from typing import List, Tuple


class Butterfly:
    def __init__(self, grid):
        self.grid = grid
        self.dim = (len(grid), len(grid[0]))

    def _get_valid_moves(self, row: int, col: int) -> List[Tuple[int, int]]:

        max_row, max_col = self.dim[0]-1, self.dim[1]-1

        moves = []
        if row == 0:
            rows = [row+1]
        elif row == max_row:
            rows = [row-1]
        else:
            rows = [row-1, row+1]

        for i in rows:
            moves.append((i, col))

        if col == 0:
            cols = [col+1]
        elif col == max_col:
            cols = [col-1]
        else:
            cols = [col-1, col+1]

        for j in cols:
            moves.append((row, j))

        return moves

    def get_min_time(self):
        larva = set()
        butterfly = set()
        count = 0

        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if self.grid[i][j] == 1:
                    larva.add((i, j))
                elif self.grid[i][j] == 2:
                    butterfly.add((i, j))

        if not larva:
            return 0

        while butterfly:
            count += 1
            new_butterflies = set()
            for row, col in butterfly:
                for next_row, next_col in self._get_valid_moves(row, col):
                    if (next_row, next_col) in larva:
                        new_butterflies.add((next_row, next_col))
                larva -= new_butterflies
                butterfly = new_butterflies

                if not larva:
                    return count
        return -1


if __name__ == '__main__':
    mat = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    obj = Butterfly(mat)
    assert obj.get_min_time() == 4
