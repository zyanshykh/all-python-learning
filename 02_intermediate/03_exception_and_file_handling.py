"""
Module: Exception & File Handling
Topic: Robust error catching, custom exceptions, and secure file operations.
"""
import os

# Custom Exception for domain logic
class InvalidConfigError(Exception):
    pass

def manage_system_logs(filename: str = "app_log.txt"):
    # 1. Safe File Writing & Error Handling
    try:
        print("Writing setup logs...")
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Initialization: Success\n")
            file.write("Environment: Production\n")
            
        # 2. Safe File Reading
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"\n--- File Content ---\n{content}")
            
    except FileNotFoundError:
        print(f"[Error]: The file {filename} could not be found.")
    except IOError:
        print("[Error]: Input/Output operation failed on the file.")
    finally:
        # Runs no matter what (Great for cleanup actions)
        print("File operation process finished.")


def validate_environment(env_name: str):
    try:
        if env_name.lower() != "production" and env_name.lower() != "development":
            raise InvalidConfigError(f"Unauthorized Environment state: '{env_name}'")
    except InvalidConfigError as error:
        print(f"[Custom Exception Caught]: {error}")


if __name__ == "__main__":
    print("--- Exception & File Handling ---")
    manage_system_logs()
    
    print("\n--- Triggering Custom Exception ---")
    validate_environment("staging") # Will trigger custom error
    
    # Cleanup log file after execution
    if os.path.exists("app_log.txt"):
        os.remove("app_log.txt")