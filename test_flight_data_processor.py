import unittest
from flight_data_processor import FlightDataProcessor

class TestFlightDataProcessor(unittest.TestCase):
    """
    Unit tests for the FlightDataProcessor class.
    """
    def setUp(self):
        """
        Initializes a FlightDataProcessor instance before each test.
        """
        self.processor = FlightDataProcessor()
        self.sample_flight = {
            "flight_number": "AZ001",
            "departure_time": "2025-02-19 15:30",
            "arrival_time": "2025-02-20 03:45",
            "duration_minutes": 615,
            "status": "ON_TIME"
        }
        self.processor.add_flight(self.sample_flight)

    def test_add_flight(self):
        """
        Tests adding a new flight.
        """
        self.assertEqual(len(self.processor.flights), 1)

        with self.assertRaises(ValueError):
            self.processor.add_flight(self.sample_flight)

    def test_remove_flight(self):
        """
        Tests removing an existing flight.
        """
        self.processor.remove_flight("AZ001")
        self.assertEqual(len(self.processor.flights), 0)

        with self.assertRaises(ValueError):
            self.processor.remove_flight("AZ002")

    def test_flights_by_status(self):
        """
        Tests retrieving flights by status.
        """
        flights = self.processor.flights_by_status("ON_TIME")
        self.assertEqual(len(flights), 1)
        self.assertEqual(flights[0]["flight_number"], "AZ001")

    def test_get_longest_flight(self):
        """
        Tests getting the longest flight.
        """
        longest_flight = self.processor.get_longest_flight()
        self.assertEqual(longest_flight["flight_number"], "AZ001")

        self.processor.remove_flight("AZ001")
        with self.assertRaises(ValueError):
            self.processor.get_longest_flight()

    def test_update_flight_status(self):
        """
        Tests updating the flight status.
        """
        self.processor.update_flight_status("AZ001", "DELAYED")
        self.assertEqual(self.processor.flights[0]["status"], "DELAYED")

        with self.assertRaises(ValueError):
            self.processor.update_flight_status("AZ002", "CANCELLED")


if __name__ == "__main__":
    unittest.main()
