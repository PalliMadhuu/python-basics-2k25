import os

class FileHandling:
    def __init__(self, file_path):
        self.file_path = file_path

    @staticmethod
    def read_file():
        """Read the first line of the file."""
        try:
            print("Reading File")
            with open('D:\\holocaust.txt', 'r') as file:
                data = file.readlines()  # Reads all the lines as a list
                print(data[0])  # Prints the first line
        except FileNotFoundError:
            print("File not found. Please verify the file.")
        except Exception as e:
            print(f"Something went wrong: {e}")

    def write_mode(self):
        """Write to the file using 'w' mode."""
        try:
            print("Writing into file")
            with open(self.file_path, 'w') as file:
                file.write("This is a new line\n")  # Writing at the beginning of the file
                file.seek(0)  # Move cursor to the beginning of the file
                file.write("Overwriting the existing line just I wrote")  # Overwrites the line
            with open(self.file_path, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found. Please check.")
        except Exception as e:
            print(f"Something went wrong: {e}")

    def append_mode(self):
        """Append to the file using 'a' mode."""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'a') as file:
                    file.write("This is a new line\n")
            else:
                print("File does not exist.")
        except FileNotFoundError:
            print("File not found. Please check the file.")
        except Exception as e:
            print(f"Something went wrong: {e}")

    def read_write_r_plus(self):
        """Open the file for both reading and writing using 'r+' mode."""
        try:
            with open(self.file_path, 'r+') as file:
                # Read the existing content
                content = file.read()
                print("Existing Content:")
                print(content)

                # Move the file pointer to the beginning before writing
                file.seek(0)
                file.write("This is a new line at the beginning.\n")
                file.write(content)  # Re-write the original content after the new line
                print("New content written at the beginning of the file.")
        except FileNotFoundError:
            print("File not found. Please verify the file path.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def write_read_w_plus(self):
        """Open the file for both writing and reading using 'w+' mode."""
        try:
            with open(self.file_path, 'w+') as file:
                # Write new content; this will overwrite existing content
                file.write("This is new content.\n")
                print("New content written to the file.")

                # Move the file pointer to the beginning before reading
                file.seek(0)
                content = file.read()
                print("Reading the newly written content:")
                print(content)
        except Exception as e:
            print(f"An error occurred: {e}")

    def append_read_a_plus(self):
        """Open the file for both appending and reading using 'a+' mode."""
        try:
            with open(self.file_path, 'a+') as file:
                # Append new content at the end of the file
                file.write("This is an appended line.\n")
                print("New content appended to the file.")

                # Move the file pointer to the beginning before reading
                file.seek(0)
                content = file.read()
                print("Reading the entire content after appending:")
                print(content)
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage:
file_handler = FileHandling('D:\\holocaust.txt')

# Uncomment the method you want to test
# file_handler.read_file()
# file_handler.write_mode()
# file_handler.append_mode()
# file_handler.read_write_r_plus()
# file_handler.write_read_w_plus()
# file_handler.append_read_a_plus()
