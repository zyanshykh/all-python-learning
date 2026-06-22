import asyncio
import time
from typing import Any

async def fetch_api_endpoint(endpoint_name: str, delay: int) -> dict[str, Any]:
    """Simulates an asynchronous network request to an API endpoint."""
    print(f"[API] Fetching data from /{endpoint_name}...")
    # asyncio.sleep execution block nahi karta, context doosre task ko de deta hai
    await asyncio.sleep(delay) 
    print(f"[API] Successfully received data from /{endpoint_name}!")
    return {"endpoint": endpoint_name, "status": "200 OK", "data_packet": delay * 10}

async def main() -> None:
    start_time = time.perf_counter()
    
    # 3 Parallel requests queue up kar rahay hain
    # Aggregated delay sequential hoti to 3 + 2 + 1 = 6 seconds lagte
    task_1 = fetch_api_endpoint("user-profile", 3)
    task_2 = fetch_api_endpoint("auth-token", 2)
    task_3 = fetch_api_endpoint("metrics-analytics", 1)
    
    print("\n--- Triggering Concurrent Network Tasks ---")
    # Concurrently running tasks using gather
    results = await asyncio.gather(task_1, task_2, task_3)
    
    end_time = time.perf_counter()
    
    print("\n--- All Responses Settled ---")
    for response in results:
        print(response)
        
    print(f"\n[SUCCESS] Total Asynchronous Execution Time: {end_time - start_time:.4f} seconds!")

if __name__ == "__main__":
    # Event loop run karne ka standard wrapper
    asyncio.run(main())