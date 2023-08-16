import os
import shutil

source_directory = r"C:\Riot Games\League of Legends\Config"
backup_directory = r"C:\backup\Config"

def create_backup():
    # Create the backup directory if it doesn't exist
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    # Copy the contents of the source directory to the backup directory
    try:
        for item in os.listdir(source_directory):
            source_item = os.path.join(source_directory, item)
            backup_item = os.path.join(backup_directory, item)
            
            if os.path.isdir(source_item):
                shutil.copytree(source_item, backup_item)
            else:
                shutil.copy2(source_item, backup_item)  # Use copy2 to preserve metadata
                
        print("Backup created successfully!")
    except Exception as e:
        print("An error occurred:", e)

def restore_backup():
    # Restore the backup by overwriting the source directory
    try:
        for item in os.listdir(backup_directory):
            source_item = os.path.join(backup_directory, item)
            target_item = os.path.join(source_directory, item)
            
            if os.path.isdir(source_item):
                shutil.rmtree(target_item)  # Remove existing directory
                shutil.copytree(source_item, target_item)
            else:
                os.remove(target_item)  # Remove existing file
                shutil.copy2(source_item, target_item)
                
        print("Backup restored successfully!")
    except Exception as e:
        print("An error occurred:", e)

# Main menu
while True:
    print("1. Create Backup")
    print("2. Restore Backup")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_backup()
    elif choice == "2":
        restore_backup()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please choose again.")