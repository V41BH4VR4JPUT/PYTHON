import os
def list_files_and_directories():
    print("\nFiles and Directories in Current Directory:")
    for item in os.listdir():
        print(f"- {item}")
    print("\n")

if __name__ == "__main__":
    list_files_and_directories()