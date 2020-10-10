from butterfly_edit import Butterfly


test_data = [
    ([[2, 1, 0, 2, 1],
      [1, 0, 1, 0, 1],
      [1, 0, 0, 0, 2]], -1),

    ([[2, 1, 0, 2, 1],
      [1, 0, 1, 2, 1],
      [1, 0, 0, 2, 1]], 2),

    ([[1, 1, 1, 1, 1],
      [0, 2, 1, 1, 1]], 4),

    ([[2, 1, 1],
      [1, 1, 0],
      [0, 1, 1]], 4),

    ([[0, 1, 0],
      [1, 2, 1],
      [0, 1, 0]], 1)
]


def test_min_time():
    for data, ans in test_data:
        obj = Butterfly(data)
        assert obj.all_larva_transform_time() == ans
