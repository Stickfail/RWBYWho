import os

folder = "Characters"

print("const images = [")

for file in sorted(os.listdir(folder)):
    if file.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
        print(f'    "Characters/{file}",')

print("];")
