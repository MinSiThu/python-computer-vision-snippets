from colorthief import ColorThief
import matplotlib.pyplot as plt

color_theif = ColorThief("marvel.jpeg")

dominant_color = color_theif.get_color(quality=1)
print(dominant_color)

plt.imshow([[dominant_color]])
plt.show()

palette = color_theif.get_palette(color_count=5)
print(palette)

plt.imshow([palette])
plt.show()