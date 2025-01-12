import os

def change_directory():
    path = input("Enter the path to navigate to: ").strip()
    try:
        os.chdir(path)
        print(f"Changed working directory to: {os.getcwd()}\n")
    except FileNotFoundError:
        print(f"Path '{path}' not found.\n")
    except Exception as e:
        print(f"Error: {e}\n")

if __name__ == "__main__":
    change_directory()