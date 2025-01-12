"""
This project is a utility tool for managing files and directories on your system. It leverages Python's os module to perform various operations like listing files, creating directories, renaming files, deleting files or directories, and navigating through the file system.

"""
import Listing
import Creating
import Deleting
import ChangeDirectory
import Rename
import CheckProperties
import Search
def main_menu():
    print("File and Directory Management System".center(80, "-"))
    while True:
        print("\nMenu:")
        print("1. List Files and Directories")
        print("2. Create a Directory")
        print("3. Rename a File or Directory")
        print("4. Delete a File or Directory")
        print("5. Change Current Working Directory")
        print("6. Check File/Directory Properties")
        print("7. Search for a File or Directory")
        print("8. Exit\n")

        choice  = int(input("Enter your choice: ").strip())
        match choice:
            case 1:
                 Listing.list_files_and_directories()
            case 2:
                Creating.create_directory()
            case 3:
                Rename.rename_file_or_directory()
            case 4:
                Deleting.delete_file_or_directory()
            case 5:
                ChangeDirectory.change_directory()
            case 6:
                CheckProperties.check_properties()
            case 7:
                Search.search_file_or_directory()
            case 8:
                print("Goodbye! Have a nice day.")
                exit()
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()