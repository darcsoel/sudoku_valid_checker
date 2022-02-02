from typing import List


class Solution:
    BOARD_LENGTH = 9
    valid_symbols = list(map(str, (range(10)))) + ['.']

    def __init__(self, board: List[List[str]]):
        self._board = board

    def _check_sub_boxes(self):
        for col_index in range(self.BOARD_LENGTH):
            for row_index in range(self.BOARD_LENGTH):
                if col_index % 3 == row_index % 3 == 0:
                    line = []
                    for inner_col_index in range(col_index, col_index + 3):
                        for inner_row_index in range(row_index, row_index + 3):
                            line.append(self._board[inner_col_index][inner_row_index])
                    if not self._check_line(line):
                        return False
        return True

    def _check_line(self, line):
        symbols = [x for x in line if x in self.valid_symbols]

        if symbols != line:
            return False

        symbols = [x for x in symbols if x.isdigit()]

        if len(symbols) != len(set(symbols)):
            return False

        return True

    def _check_columns(self):
        for index in range(self.BOARD_LENGTH):
            line = [self._board[column][index] for column in range(self.BOARD_LENGTH)]
            if not self._check_line(line):
                return False

        return True

    def _check_rows(self):
        for row in self._board:
            if not self._check_line(row):
                return False

        return True

    def is_valid(self) -> bool:
        sub_boxes = self._check_sub_boxes()
        columns = self._check_columns()
        rows = self._check_rows()

        return all((sub_boxes, columns, rows))
