
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

n = 25
side = math.ceil(math.sqrt(n))

fig, ax = plt.subplots(figsize=(7, 7))

for square_id in range(n):
    col = square_id % side
    row = square_id // side

    x = col + 0.5
    y = row + 0.5

    # Square bottom-left corner
    square = Rectangle(
        (x - 0.5, y - 0.5),
        1, 1,
        fill=False,
        edgecolor="blue"
    )

    ax.add_patch(square)
    ax.text(x, y, str(square_id),
            ha="center", va="center", fontsize=9)

ax.set_xlim(0, side)
ax.set_ylim(0, side)
ax.set_aspect("equal")
ax.set_xticks(range(side + 1))
ax.set_yticks(range(side + 1))
ax.grid(True)
ax.set_title("25 Unit Squares - Grid Packing")

plt.show()
