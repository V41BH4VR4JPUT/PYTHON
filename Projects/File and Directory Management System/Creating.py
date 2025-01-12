import os
def create_directory():
    dir_name = input("Enter the name of the directory to create: ").strip()
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully.\n")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists.\n")
    except Exception as e:
        print(f"Error: {e}\n")


if __name__ == "__main__":
    create_directory()