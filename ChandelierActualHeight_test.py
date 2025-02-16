import pytest
from datetime import datetime, timedelta
from ChandelierActualHeight import convert_to_actual_movement_time

@pytest.mark.parametrize(
    "previous_row, current_row, expected_output",
    [
        # Test case format: (previous_row, current_row, expected_output)
        (
            [datetime(2025, 1, 1, 1, 0, 0), 10], 
            [datetime(2025, 1, 1, 2, 0, 0), 15], 
            [[datetime(2025, 1, 1, 1, 57, 30), 10], [datetime(2025, 1, 1, 2, 2, 30), 15]]
        ),

        # ((datetime(2025, 1, 1, 1, 0, 0), 20), (datetime(2025, 1, 1, 2, 0, 0), 10), 5.0, (20, 10)),
        # ((datetime(2025, 1, 1, 3, 0, 0), 5), (datetime(2025, 1, 1, 4, 0, 0), 15), 5.0, (5, 15)),
    ]
)

def test_convert_to_actual_movement_time(previous_row, current_row, expected_output):
    output = convert_to_actual_movement_time(previous_row, current_row)

    # Assert movement start time
    assert output[0][0] == expected_output[0][0]
    # Assert movement start height
    assert output[0][1] == expected_output[0][1]

    # Assert movement end time
    assert output[1][0] == expected_output[1][0]
    # Assert movement end height
    assert output[1][1] == expected_output[1][1]
    