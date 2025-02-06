import os
files = os.listdir("Projects/Clear the Clutter")
for file in files:
    print(file)

print("---------------------------------------------------------")
print("After optimization")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"Projects/Clear the Clutter/{file}", f"Projects/Clear the Clutter/{i}.png")
    i = i + 1
# os.rename("Projects/Clear the Clutter/Description.txt", "Projects/Clear the Clutter/Description.md")
for file in files:
   if file.endswith(".pdf"):
      os.remove(f"Projects/Clear the Clutter/{file}")