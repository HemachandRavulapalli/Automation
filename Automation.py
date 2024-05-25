import os

def rename_files(directory, pattern):
    """
    Rename files in the specified directory based on the given pattern.
    
    Args:
        directory (str): Path to the directory containing the files.
        pattern (str): Pattern for renaming files. Use "{}" as a placeholder for the index.
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Get list of files in the directory
    try:
        files = os.listdir(directory)
    except Exception as e:
        print(f"Error accessing directory '{directory}': {e}")
        return
    
    # Iterate through each file and rename it
    for index, filename in enumerate(files, start=1):
        # Generate new filename using the pattern
        new_filename = pattern.format(index)
        
        # Construct full paths for old and new filenames
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file
        try:
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
        except Exception as e:
            print(f"Error renaming '{old_path}' to '{new_path}': {e}")

# Example usage:
directory = r"C:\Users\ravul\OneDrive\Desktop\TestFiles"  # Make sure this path exists
pattern = "document_{}.txt"
rename_files(directory, pattern)
