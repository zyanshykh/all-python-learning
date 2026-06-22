import time
from typing import Callable, Any, Generator

# 1. PRACTICAL DECORATOR: Execution Timer & Logger
def monitor_performance(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to measure execution time and log function calls."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"\n[LOG] Executing '{func.__name__}' with args: {args}...")
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        print(f"[LOG] '{func.__name__}' finished in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@monitor_performance
def process_heavy_data(n: int) -> list[int]:
    """Simulates a processing task that consumes time."""
    return [x**2 for x in range(n)]

# 2. PRACTICAL GENERATOR: Large Data Streamer
def stream_large_dataset(num_records: int) -> Generator[dict[str, Any], None, None]:
    """Generates mock log data on-the-fly to save memory."""
    for i in range(1, num_records + 1):
        yield {
            "event_id": f"EVT-{i:05d}",
            "status": "SUCCESS" if i % 2 == 0 else "FAILED",
            "timestamp": time.time()
        }

if __name__ == "__main__":
    # Test Decorator
    process_heavy_data(5_000_000)
    
    # Test Generator (Streaming 1 Million records without exhausting memory)
    print("\n[LOG] Starting Data Stream via Generator:")
    log_stream = stream_large_dataset(1_000_000)
    
    # Just printing first 3 items to verify stream works
    for _ in range(3):
        print(next(log_stream))