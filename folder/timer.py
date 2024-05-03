class Time:
  """
  This class represents a time with hours, minutes, and seconds.
  """

  def __init__(self, hours, minutes, seconds):
    """
    Initializes a Time object.

    Args:
        hours: The initial hours (0-23).
        minutes: The initial minutes (0-59).
        seconds: The initial seconds (0-59).
    """

    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds

  def increment_hour(self):
    """
    Increments the hour by 5, handling overflow to the next day.
    """

    self.hours = (self.hours + 5) % 24

  def increment_minute(self):
    """
    Increments the minute by 5, handling overflow to the next hour.
    """

    self.minutes = (self.minutes + 5) % 60
    if self.minutes == 0:
      self.increment_hour()

  def increment_second(self):
    """
    Increments the second by 5, handling overflow to the next minute.
    """

    self.seconds = (self.seconds + 5) % 60
    if self.seconds == 0:
      self.increment_minute()

  def __str__(self):
    """
    Returns a string representation of the time in HH:MM:SS format.
    """

    return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

def main():
  """
  Reads time data from a file (simulated by example inputs), creates Time objects, increments their units, and prints the results.
  """

  # Sample input data (replace with actual file reading)
  time_data = [
      "23:59:59",
      "05:30:50"
  ]

  for time_str in time_data:
    hours, minutes, seconds = map(int, time_str.split(":"))
    time_obj = Time(hours, minutes, seconds)

    # Increment hours
    time_obj.increment_hour()
    print(f"Hour: {time_obj}")

    # Increment minutes
    time_obj.minutes = minutes  # Reset minutes for separate test
    time_obj.increment_minute()
    print(f"Minute: {time_obj}")

    # Increment seconds
    time_obj.seconds = seconds  # Reset seconds for separate test
    time_obj.increment_second()
    print(f"Second: {time_obj}")
    print()

if __name__ == "__main__":
  main()

