def calculate_bacteria_growth(target_bacteria):
  bacteria_count = 1
  time_elapsed = 0
  minutes_in_hour = 60
  minutes_in_day = minutes_in_hour * 24

  while bacteria_count < target_bacteria:
    bacteria_count *= 2
    time_elapsed += 1
    if time_elapsed >= minutes_in_day:
      days = time_elapsed // minutes_in_day
      time_elapsed %= minutes_in_day
      if days > 0:
        return f"{days} days {time_elapsed} minutes"
    elif time_elapsed >= minutes_in_hour:
      hours = time_elapsed // minutes_in_hour
      time_elapsed %= minutes_in_hour
      if hours > 0:
        return f"{hours} hours {time_elapsed} minutes"
  return f"{time_elapsed} minutes"


target_bacteria = 1000000
time_str = calculate_bacteria_growth(target_bacteria)
print(f"It takes {time_str} for a single bacteria to multiply to {target_bacteria} bacteria.")

