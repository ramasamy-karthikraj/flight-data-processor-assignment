# Flight Data Processor

## Overview
The Flight Data Processor is a Python-based system that manages flight data efficiently. It allows users to add, remove, filter, and update flight information while ensuring data integrity and robustness through unit testing.

## Features
- Add a new flight while preventing duplicates.
- Remove a flight using its flight number.
- Retrieve flights based on their status.
- Identify the longest flight based on duration.
- Update flight status dynamically.
- Comprehensive unit tests for reliability.

## Technologies Used
- Python 3.x
- `unittest` framework
- JSON format for flight data storage

## Installation
1. Clone this repository:
   ```sh
   git clone --branch master --single-branch https://github.com/ramasamy-karthikraj/flight-data-processor-assignment.git
   ```
2. Navigate to the project directory:
   ```sh
   cd flight-data-processor-assignment
   ```
3. Ensure you have Python 3 installed.

## Usage
1. Run the main script to interact with the flight data processor.
2. Execute unit tests to verify functionality:
   ```sh
   python -m unittest test_flight_data_processor.py
   ```