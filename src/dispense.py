class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.

    System Rules: For the remainder of the lab, assume the following rules apply:
    1. The dose must be a positive value.
    2. The quantity dispensed must be a positive integer.
    3. Each medication has a maximum daily dose.
    4. A patient may not receive the same medication more than once per day. (checked by invariant_holds)
    5. All doses are expressed in milligrams.

    """

    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    #Maximum daily dose.
    MAX_DAILY_DOSE_MG = {
        "testmed": 100
    }

    def __init__(self, patient_id, medication, dose_mg, quantity):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.

        """

         #Identifier constraints (valid identifiers)
        if not isinstance(patient_id, str) or patient_id.strip() == "":
            raise ValueError("patient_id must be a non-empty string")

        if not isinstance(medication, str) or medication.strip() == "":
            raise ValueError("medication must be a non-empty string")

        #<edication key for consistent checks (case-insensitive)
        med_key = medication.strip().lower()

        #1. The dose must be a positive value.
        if not isinstance(dose_mg, (int, float)) or isinstance(dose_mg, bool):
            raise ValueError("dose_mg must be a number (int or float)")
        if dose_mg <= 0:
            raise ValueError("dose_mg must be a positive value")

        #2. The quantity dispensed must be a positive integer.
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("quantity must be an integer")
        if quantity <= 0:
            raise ValueError("quantity must be a positive integer")

        #3. Each medication has a maximum daily dose.
        if med_key not in DispenseEvent.MAX_DAILY_DOSE_MG:
            raise ValueError("Unknown medication: no maximum daily dose defined")

        max_daily = DispenseEvent.MAX_DAILY_DOSE_MG[med_key]
        if dose_mg > max_daily:
            raise ValueError("dose_mg exceeds maximum daily dose for this medication")

        # Store fields (5. All doses are expressed in milligrams.)
        self.patient_id = patient_id.strip()
        self.medication = medication.strip()
        self.medication_key = med_key
        self.dose_mg = float(dose_mg)
        self.quantity = quantity

    # TODO Task 4: Define and check system invariants 
    
    @staticmethod #This function belongs to the class for organization, but it does NOT receive self automatically.
    def invariant_holds(existing_events, new_event):
        """
        Check whether adding a new dispense event preserves all system invariants.
      
        4. A patient may not receive the same medication more than once per day. 

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
            
        """
        if new_event is None or not isinstance(new_event, DispenseEvent):
            raise TypeError("new_event must be a DispenseEvent")

        if existing_events is None:
            return True

        for ev in existing_events:
            if not isinstance(ev, DispenseEvent):
                raise TypeError("existing_events must contain only DispenseEvent objects")

            same_patient = (ev.patient_id == new_event.patient_id)
            same_med = (ev.medication_key == new_event.medication_key)

            if same_patient and same_med:
                return False

        return True