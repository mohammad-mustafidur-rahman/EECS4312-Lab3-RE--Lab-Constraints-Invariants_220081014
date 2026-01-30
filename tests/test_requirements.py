# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.dispense import DispenseEvent

def setup_module(module):
    #The medication used in tests must exist in the max-dose table
    DispenseEvent.MAX_DAILY_DOSE_MG.clear()
    DispenseEvent.MAX_DAILY_DOSE_MG.update({
        "testmed": 100
    })

def test_rejects_zero_or_negative_dose():
    #1. The dose must be a positive value.
    with pytest.raises(ValueError):
        DispenseEvent("p1", "testmed", 0, 1)
    with pytest.raises(ValueError):
        DispenseEvent("p1", "testmed", -5, 1)

def test_rejects_invalid_quantity():
    #2. The quantity dispensed must be a positive integer.
    with pytest.raises(ValueError):
        DispenseEvent("p1", "testmed", 10, 0)# zero
    with pytest.raises(ValueError):
        DispenseEvent("p1", "testmed", 10, -1)# negative
    with pytest.raises(ValueError):
        DispenseEvent("p1", "testmed", 10, 1.5)# not an integer

def test_rejects_invalid_identifiers():
    # Empty strings or non-strings should fail (edge cases)
    with pytest.raises(ValueError):
        DispenseEvent("", "testmed", 10, 1) # Empty patient (invalid patient)
    with pytest.raises(ValueError):
        DispenseEvent("p1", "", 10, 1) # Empty med (invalid med)
    with pytest.raises(ValueError):
        DispenseEvent(None, "testmed", 10, 1) # None type

def test_rejects_boolean_types():
    # Code specifically blocks booleans because we know True == 1 in Python
    with pytest.raises(ValueError):
        DispenseEvent("p1", "testmed", True, 1) # Dose as boolean
    with pytest.raises(ValueError):
        DispenseEvent("p1", "testmed", 10, True) # Quantity as boolean

def test_enforces_max_daily_dose():
    #3. Each medication has a maximum daily dose.
    with pytest.raises(ValueError):
        DispenseEvent("p1", "testmed", 101, 1)

def test_valid_dispense_event_creation():
    # Test valid creation at the exact max boundary (edge case)
    event = DispenseEvent("p1", "testmed", 100, 5) 
    
    assert event.patient_id == "p1"
    assert event.medication == "testmed"
    assert event.dose_mg == 100.0 # Should store as float
    assert event.quantity == 5

def test_invariant_case_insensitivity():
    #"TestMed" and "testmed" are the same thing, so it should be seen as same.
    e1 = DispenseEvent("p1", "testmed", 10, 1)
    e2 = DispenseEvent("p1", "TestMed", 10, 1) # Different case
    
    # This should return False because they are the same drug
    assert DispenseEvent.invariant_holds([e1], e2) is False

def test_invariant_allows_different_patients():
    #Same med, same day, but different patients must be Allowed
    e1 = DispenseEvent("p1", "testmed", 10, 1)
    e2 = DispenseEvent("p2", "testmed", 10, 1) 
    
    assert DispenseEvent.invariant_holds([e1], e2) is True

def test_unknown_medication_rejected():
    #Unknown medication (only if the medication is not in MAX_DAILY_DOSE_MG)
    with pytest.raises(ValueError, match="Unknown medication"):
        DispenseEvent("p1", "mystery_drug", 10, 1)

def test_prevents_duplicate_dispense_same_day():
    # 4. (Invariant): A patient may not receive the same medication more than once per day.
    e1 = DispenseEvent("p1", "testmed", 10, 1)
    e2 = DispenseEvent("p1", "testmed", 20, 1)  # dose can differ; still duplicate med for same patient/day

    assert DispenseEvent.invariant_holds([e1], e2) is False

    #Different medication should be allowed
    e3 = DispenseEvent("p1", "testmed", 10, 1)
    DispenseEvent.MAX_DAILY_DOSE_MG["othermed"] = 100
    e4 = DispenseEvent("p1", "othermed", 10, 1)
    assert DispenseEvent.invariant_holds([e3], e4) is True