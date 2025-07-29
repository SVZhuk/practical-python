# bounce.py
#
# Exercise 1.5
# A rubber ball is dropped from a height of 100 meters and each time it hits the
# ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py
# that prints a table showing the height of the first 10 bounces.

starting_height: float = 100.0  # meters
bounce_ratio: float = 3 / 5
bounces: int = 1
current_height: float = starting_height

while bounces <= 10:
    current_height = current_height * (bounce_ratio)
    print(f"Bounce {bounces}: Height = {current_height:.4f} meters")
    bounces += 1
print("Done with bounce calculations.")
