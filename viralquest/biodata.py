from dataclasses import dataclass

@dataclass
class BioSequence:
    """valid biological sequence"""
    id: str
    sequence: str
    length: int  
    
