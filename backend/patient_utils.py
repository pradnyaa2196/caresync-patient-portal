def is_valid_patient_id(patient_id: str) -> bool:
    """
    Checks whether a patient ID follows the required format.
    
    A valid patient ID must:
        - Start with the letters PT followed by a hyphen
        - Be followed by exactly 6 digits
        - Example: PT-000123
    
    Parameters:
        patient_id (str): The patient ID string to validate
    
    Returns:
        bool: True if the ID is valid, False otherwise
    """
    import re
    
    # Strip whitespace from both ends of the input
    # This handles cases where a user pastes an ID with an accidental space
    patient_id = patient_id.strip()
    
    pattern = r"^PT-\d{6}$"
    return bool(re.match(pattern, patient_id))
