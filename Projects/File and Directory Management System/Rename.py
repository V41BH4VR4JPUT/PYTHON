import os

def rename_file_or_directory():
    old_name = input("Enter the name of the file or directory to rename: ").strip()
    new_name = input("Enter the new name: ").strip()
    try:
        os.rename(old_name, new_name)
        print(f"'{old_name}' renamed to '{new_name}'.\n")
    except FileNotFoundError:
        print(f"'{old_name}' not found.\n")
    except Exception as e:
        print(f"Error: {e}\n")


if __name__ == "__main__":  
    rename_file_or_directory()