from typing import List, Tuple


class Butterfly(object):
    def __init__(self, mat: List[List[int]]):
        self.mat = mat
        self.dim = (len(mat), len(mat[0]))

    def next_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        moves = []
        if row == 0:
            rows = [row+1]
        elif row == self.dim[0]-1:
            rows = [row-1]
        else:
            rows = [row+1, row-1]

        for r in rows:
            moves.append((r, col))

        if col == 0:
            cols = [col+1]
        elif col == self.dim[1]-1:
            cols = [col-1]
        else:
            cols = [col+1, col-1]

        for c in cols:
            moves.append((row, c))

        return moves

    def all_larva_transform_time(self) -> int:
        step = 0
        butterflies, larva = set(), set()

        for row in range(self.dim[0]):
            for col in range(self.dim[1]):
                if self.mat[row][col] == 1:
                    larva.add((row, col))
                elif self.mat[row][col] == 2:
                    butterflies.add((row, col))

        if not larva:
            return 0

        while butterflies:
            step += 1
            new_butterflies = set()
            for row, col in butterflies:
                for pos in self.next_moves(row, col):
                    if pos in larva:
                        new_butterflies.add(pos)

                # transform larva to butterfly
                larva -= new_butterflies

                if not larva:
                    return step

            butterflies = new_butterflies

        return -1
