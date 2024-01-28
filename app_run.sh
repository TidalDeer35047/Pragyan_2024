#!/bin/bash

username=$(whoami)

# Define the paths to your Python programs
program1_path="/home/$username/pragyan/app.py"
program2_path="/home/$username/pragyan/update_realtime.py"

# Function to run program1.py
run_program1() {
    echo "Running program1.py..."
    python3 "$program1_path" &
    program1_pid=$!
}

# Function to run program2.py
run_program2() {
    echo "Running program2.py..."
    python3 "$program2_path" &
    program2_pid=$!
}

# Run program2 initially
echo "("
run_program2

wait "$program2_pid" >/dev/null 2>&1
kill "$program2_pid" >/dev/null 2>&1
echo ")"

# Main loop to alternate between program1 and program2
while true; do
    # Kill program1 before running program2
    echo "("
    run_program1

    sleep 1500

    kill "$program1_pid" >/dev/null 2>&1
    # Wait for program1 to terminate
    wait "$program1_pid" >/dev/null 2>&1

    echo ")"
    sleep 2
    # Wait for 30 seconds

    echo "("
    # Run program2
    run_program2

    # Wait for program2 to finish
    kill "$program2_pid" >/dev/null 2>&1

    wait "$program2_pid" >/dev/null 2>&1
    echo ")"

    sleep 1
done

trap kill "$program2_pid" >/dev/null 2>&1
trap kill "$program1_pid" >/dev/null 2>&1
