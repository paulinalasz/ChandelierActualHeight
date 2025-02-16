import pytest
from datetime import date, datetime, timedelta
from ChandelierActualHeight import convert_to_actual_movement_time

@pytest.mark.parametrize(
    "previous_row, current_row, expected_output",
    [
        #normal test
        #cahnging days
        #height is the same so no diff
        #really small height change
        #really big height change

        Test case format: (previous_row, current_row, expected_output)
        (   # Standard test case
            [datetime(2025, 1, 1, 1, 0, 0), 10], 
            [datetime(2025, 1, 1, 2, 0, 0), 15], 
            [[datetime(2025, 1, 1, 1, 57, 30), 10], [datetime(2025, 1, 1, 2, 2, 30), 15]]
        ),
        (   # Changing days
            [datetime(2025, 1, 1, 23, 0, 0), 20],
            [datetime(2025, 1, 2, 00, 0, 0), 10],
            [[datetime(2025, 1, 1, 23, 55, 0), 20], [datetime(2025, 1, 2, 00, 5, 0), 10]]
        ),
        (   # Changing years
            [datetime(2025, 12, 31, 23, 0, 0), 20],
            [datetime(2026, 1, 1, 00, 0, 0), 30],
            [[datetime(2025, 12, 31, 23, 55, 0), 20], [datetime(2026, 1, 1, 00, 5, 0), 30]]
        ),
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
    