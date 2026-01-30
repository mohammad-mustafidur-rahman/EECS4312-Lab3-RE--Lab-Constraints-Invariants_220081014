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

def test_enforces_max_daily_dose():
    #3. Each medication has a maximum daily dose.
    with pytest.raises(ValueError):
        DispenseEvent("p1", "testmed", 101, 1)

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