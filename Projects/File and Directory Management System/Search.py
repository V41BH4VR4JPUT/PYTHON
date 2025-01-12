import os

def search_file_or_directory():
    search_name = input("Enter the name of the file or directory to search: ").strip()
    found = [item for item in os.listdir() if search_name in item]
    if found:
        print(f"\nFound: {', '.join(found)}\n")
    else:
        print(f"'{search_name}' not found in the current directory.\n")


if __name__ == "__main__":  
    search_file_or_directory()