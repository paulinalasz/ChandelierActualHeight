import csv
from datetime import datetime
from datetime import timedelta

SCHEDULE_FILE = "schedule.csv"
OUTPUT_FILE = "output.csv"
MOTOR_SPEED = 1 # meter per minute

def read_schedule(file_path):
    schedule = []
    
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            timestamp = datetime.fromisoformat(row[0].replace("Z", "+00:00"))
            height = int(row[1])
            schedule.append((timestamp, height))

    # Ensure the schedule is sorted by time
    schedule.sort(key=lambda x: x[0])
    return schedule

def write_output(file_path, output):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in output:
            writer.writerow([row[0].isoformat().replace("+00:00", "Z"), row[1]])

def find_time_delta_each_side_of_hour(previous_row, current_row):
    distance_to_move = abs(previous_row[1] - current_row[1])
    time_taken_to_move = distance_to_move/MOTOR_SPEED
    return timedelta(minutes=time_taken_to_move/2);

def convert_to_actual_movement_time(previous_row, current_row):
    time_each_side_of_hour = find_time_delta_each_side_of_hour(previous_row, current_row)
    output = [[current_row[0] - time_each_side_of_hour, previous_row[1]], # Time and height when Chandelier starts moving
              [current_row[0] + time_each_side_of_hour, current_row[1]]]  # Time and height when Chandelier stops moving

    return output

# Find the times that the motor starts, and stops moving
def convert_to_actual_movement_times(schedule):
    output = []

    for i in range(len(schedule)):
        # we assume that the first input is the chandeliers current position
        if i==0: 
            output.append(schedule[i])
        else:
            # only calculate movement timestamps if the chandelier moves
            if (schedule[i-1][1] != schedule[i][1]):
                output.extend(convert_to_actual_movement_time(schedule[i-1], schedule[i]))

    return output

if __name__ == "__main__":
    schedule = read_schedule(SCHEDULE_FILE)
    output = convert_to_actual_movement_times(schedule)
    write_output(OUTPUT_FILE, output)
    
