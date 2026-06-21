from typing import Any

class PremiumConfig:
    """A clean, professional Configuration Object mimicking modern library components."""
    
    def __init__(self, environment: str, debug: bool, version: float):
        self.environment = environment
        self.debug = debug
        self.version = version

    def __repr__(self) -> str:
        """Developer-friendly string representation."""
        return f"PremiumConfig(env='{self.environment}', debug={self.debug}, v={self.version})"

    def __str__(self) -> str:
        """User-friendly clean output."""
        return f"[{self.environment.upper()}] Environment Config v{self.version}"

    def __eq__(self, other: Any) -> bool:
        """Checks structural equality between two config objects."""
        if not isinstance(other, PremiumConfig):
            return False
        return (self.environment == other.environment and 
                self.debug == other.debug and 
                self.version == other.version)

if __name__ == "__main__":
    config_dev_1 = PremiumConfig(environment="development", debug=True, version=1.2)
    config_dev_2 = PremiumConfig(environment="development", debug=True, version=1.2)
    config_prod = PremiumConfig(environment="production", debug=False, version=1.0)
    
    # Testing __repr__ and __str__
    print("--- Representation Testing ---")
    print(f"Developer style (repr): {repr(config_dev_1)}")
    print(f"Clean style (str): {config_dev_1}")
    
    # Testing Object Equality (__eq__)
    print("\n--- Structural Equality Testing ---")
    print(f"Are dev configurations identical? -> {config_dev_1 == config_dev_2}")
    print(f"Is dev configuration equal to production? -> {config_dev_1 == config_prod}")