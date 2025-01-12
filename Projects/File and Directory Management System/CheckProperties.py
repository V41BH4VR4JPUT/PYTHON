import os
import time

def check_properties():
    name = input("Enter the file or directory name: ").strip()
    if os.path.exists(name):
        print(f"\nProperties of '{name}':")
        print(f"- Size: {os.path.getsize(name)} bytes")
        print(f"- Created: {time.ctime(os.path.getctime(name))}")
        print(f"- Last Modified: {time.ctime(os.path.getmtime(name))}\n")
    else:
        print(f"'{name}' does not exist.\n")

if __name__ == "__main__":
    check_properties()