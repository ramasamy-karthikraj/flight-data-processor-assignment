from typing import List, Dict, Any

class FlightDataProcessor:
    """
    A class to process and manage flight data.
    """

    def __init__(self) -> None:
        """
        Initializes the FlightDataProcessor with an empty list of flights.
        """
        self.flights: List[Dict[str, Any]] = []

    def add_flight(self, data: Dict[str, Any]) -> None:
        """
        Adds a new flight to the list, ensuring no duplicates by flight number.

        :param data: Dictionary containing flight details.
        :raises ValueError: If a flight with the same flight number already exists.
        """
        if any(flight["flight_number"] == data["flight_number"] for flight in self.flights):
            raise ValueError(f"Flight {data['flight_number']} already exists.")
        self.flights.append(data)

    def remove_flight(self, flight_number: str) -> None:
        """
        Removes a flight based on the flight number.

        :param flight_number: The flight number to remove.
        :raises ValueError: If the flight number does not exist.
        """
        if not any(flight["flight_number"] == flight_number for flight in self.flights):
            raise ValueError(f"Flight {flight_number} not found.")
        self.flights = [flight for flight in self.flights if flight["flight_number"] != flight_number]

    def flights_by_status(self, status: str) -> List[Dict[str, Any]]:
        """
        Returns all flights with a given status.

        :param status: The flight status to filter by.
        :return: List of flights matching the given status.
        """
        return [flight for flight in self.flights if flight["status"] == status]

    def get_longest_flight(self) -> Dict[str, Any]:
        """
        Returns the flight with the longest duration in minutes.

        :return: Dictionary containing the longest flight details, or an empty dictionary if no flights exist.
        """
        if not self.flights:
            raise ValueError("No flights available to determine the longest flight.")
        return max(self.flights, key=lambda flight: flight.get("duration_minutes", 0))

    def update_flight_status(self, flight_number: str, new_status: str) -> None:
        """
        Updates the status of a flight.

        :param flight_number: The flight number to update.
        :param new_status: The new status to be assigned.
        :raises ValueError: If the flight number is not found.
        """
        for flight in self.flights:
            if flight["flight_number"] == flight_number:
                flight["status"] = new_status
                return
        raise ValueError(f"Flight {flight_number} not found.")
