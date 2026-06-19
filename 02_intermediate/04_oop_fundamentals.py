"""
Module: OOP Fundamentals
Topic: Blueprinting clean architecture using Classes, Inheritance, and Encapsulation.
"""

# Base Class (Parent)
class DigitalAsset:
    def __init__(self, name: str, valuation: float):
        self.name = name           # Public attribute
        self._valuation = valuation # Protected attribute (convention)
        self.__asset_id = "DSA-9921" # Private attribute (Encapsulation)

    # Getter method to access private data safely
    def get_asset_id(self) -> str:
        return self.__asset_id

    def get_details(self) -> str:
        return f"Asset: {self.name} | Value: ${self._valuation}"


# Derived Class (Child Inheritance)
class SaaSProduct(DigitalAsset):
    def __init__(self, name: str, valuation: float, tech_stack: list):
        # Inherit constructor properties from parent
        super().__init__(name, valuation)
        self.tech_stack = tech_stack

    # Method Overriding (Polymorphism)
    def get_details(self) -> str:
        parent_details = super().get_details()
        return f"{parent_details} | Stack: {', '.join(self.tech_stack)}"


# --- Execution ---
if __name__ == "__main__":
    print("--- Object-Oriented Programming ---")
    
    # Instantiate Base Class
    generic_asset = DigitalAsset("Domain Bundle", 1500)
    print(generic_asset.get_details())
    print(f"Encapsulated Asset ID: {generic_asset.get_asset_id()}\n")
    
    # Instantiate Inherited SaaS Class
    my_saas = SaaSProduct("Music Analytics API", 12000, ["Next.js", "Python", "PostgreSQL"])
    print("--- SaaS Subclass Output ---")
    print(my_saas.get_details())