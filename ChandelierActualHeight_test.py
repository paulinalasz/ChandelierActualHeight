import pytest
from datetime import date, datetime, timedelta
from ChandelierActualHeight import convert_to_actual_movement_time, convert_to_actual_movement_times

@pytest.mark.parametrize(
    "previous_row, current_row, expected_output",
    [
        #normal test
        #cahnging days
        #height is the same so no diff
        #really small height change
        #really big height change

        #Test case format: (previous_row, current_row, expected_output)
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

@pytest.mark.parametrize(
    "schedule, expected_output",
    [
        #Test case format: (previous_row, current_row, expected_output)
        (   # Standard test case
            [[datetime(2025, 1, 1, 1, 0, 0), 10], 
            [datetime(2025, 1, 1, 2, 0, 0), 15], 
            [datetime(2025, 1, 1, 3, 0, 0), 13], 
            [datetime(2025, 1, 1, 4, 0, 0), 10]], 

            [[datetime(2025, 1, 1, 1, 0, 00), 10], 
             [datetime(2025, 1, 1, 1, 57, 30), 10],
             [datetime(2025, 1, 1, 2, 2, 30), 15],
             [datetime(2025, 1, 1, 2, 59, 00), 15],
             [datetime(2025, 1, 1, 3, 1, 00), 13],
             [datetime(2025, 1, 1, 3, 58, 30), 13],
             [datetime(2025, 1, 1, 4, 1, 30), 10]]
        ),
        (   # With entries where height doesnt change
            [[datetime(2025, 1, 1, 1, 0, 0), 10], 
            [datetime(2025, 1, 1, 2, 0, 0), 15], 
            [datetime(2025, 1, 1, 3, 0, 0), 15], 
            [datetime(2025, 1, 1, 4, 0, 0), 13], 
            [datetime(2025, 1, 1, 5, 0, 0), 10]], 

            [[datetime(2025, 1, 1, 1, 0, 00), 10], 
             [datetime(2025, 1, 1, 1, 57, 30), 10],
             [datetime(2025, 1, 1, 2, 2, 30), 15],
             [datetime(2025, 1, 1, 3, 59, 00), 15],
             [datetime(2025, 1, 1, 4, 1, 00), 13],
             [datetime(2025, 1, 1, 4, 58, 30), 13],
             [datetime(2025, 1, 1, 5, 1, 30), 10]]
        )
    ]
)

def test_convert_to_actual_movemement_times(schedule, expected_output):
    output = convert_to_actual_movement_times(schedule)

    assert output == expected_output