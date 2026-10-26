
import pandas as pd
import math

n = 4
side = math.ceil(math.sqrt(n))

rows = []

for square_id in range(n):
    col = square_id % side
    row = square_id // side

    x = col + 0.5
    y = row + 0.5
    angle = 0.0

    rows.append({
        "n": n,
        "square_id": square_id,
        "x": x,
        "y": y,
        "angle": angle
    })

df = pd.DataFrame(rows)
print(df)

# Find the container boundaries

L = 2.0

# Competition scoring formula
score = L / math.sqrt(n) - 1

print("Number of squares:", n)
print("Container side length:", L)
print("Competition score:", score)
