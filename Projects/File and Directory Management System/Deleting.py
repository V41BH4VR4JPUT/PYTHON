import os

def delete_file_or_directory():
    name = input("Enter the name of the file or directory to delete: ").strip()
    if os.path.isdir(name):
        try:
            os.rmdir(name)
            print(f"Directory '{name}' deleted successfully.\n")
        except Exception as e:
            print(f"Error: {e}\n")
    elif os.path.isfile(name):
        try:
            os.remove(name)
            print(f"File '{name}' deleted successfully.\n")
        except Exception as e:
            print(f"Error: {e}\n")
    else:
        print(f"'{name}' not found.\n")

if __name__ == "__main__":
    delete_file_or_directory()