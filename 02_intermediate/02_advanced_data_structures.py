"""
Module: Advanced Data Structures
Topic: List/Dict Comprehensions, Sets operations, and performance-friendly data handling.
"""

def process_data():
    # Raw user earnings or project metrics
    raw_revenues = [1200, 2500, 800, 4300, 9500, 3100]
    
    # 1. List Comprehension (Filter & Transform efficiently)
    # Filter revenues > 2000 and apply a 10% bonus
    premium_revenues = [revenue * 1.10 for revenue in raw_revenues if revenue > 2000]
    print(f"Premium Revenues (10% Bonus applied): {premium_revenues}")
    
    # 2. Dictionary Comprehension
    # Mapping usernames to their platform status
    users = ["Frank", "Shayar", "Ali"]
    user_status = {user: "Active" if user != "Ali" else "Suspended" for user in users}
    print(f"User Status Map: {user_status}")
    
    # 3. Sets for Unique Operations (e.g., Filtering duplicate tags)
    stack_one = {"Next.js", "React", "Python", "PostgreSQL"}
    stack_two = {"Python", "FastAPI", "PostgreSQL", "Docker"}
    
    common_tech = stack_one.intersection(stack_two)
    all_tech = stack_one.union(stack_two)
    
    print(f"Common Stack: {common_tech}")
    print(f"Combined Stack: {all_tech}")


if __name__ == "__main__":
    print("--- Advanced Data Structures & Comprehensions ---")
    process_data()