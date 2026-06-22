import sys
from typing import Generator
from contextlib import contextmanager

@contextmanager
def managed_transaction(session_name: str) -> Generator[str, None, None]:
    """A context manager to safely handle database or file state lifecycles."""
    print(f"\n[TRANSACTION] Opening secure stream session: '{session_name}'")
    try:
        # Pushing control to the 'with' statement block
        yield f"ACTIVE_SESSION_CONN_{session_name.upper()}"
        
        # Runs if no exceptions occur inside 'with' block
        print(f"[TRANSACTION] Committing all transactions safely for '{session_name}'.")
    except Exception as error:
        # Runs if runtime issues happen inside 'with' block
        print(f"[CRITICAL] Error detected: {error}. Rolling back changes for '{session_name}' instantly.")
        # Re-raise error if application flow control requires it
    finally:
        # Always runs no matter what
        print(f"[TRANSACTION] Closing and releasing resources for '{session_name}'.")

if __name__ == "__main__":
    # Test Case 1: Successful execution context
    print("--- Test Case 1: Smooth Flow ---")
    with managed_transaction("user_auth_db") as session:
        print(f"[WORKING] Writing metadata token using active channel: {session}")
        print("[WORKING] Data buffered successfully.")

    # Test Case 2: Failure context containing safe graceful rollback
    print("\n--- Test Case 2: Exception Handling and Rollback Flow ---")
    try:
        with managed_transaction("payment_gateway") as session:
            print(f"[WORKING] Processing balance updates via: {session}")
            # Simulating unexpected crash
            raise RuntimeError("Network Timeout / Dropped Packets")
            print("[WORKING] This line will never execute.")
    except RuntimeError:
        print("[SYSTEM] High-level runtime exception handled safely outside context.")