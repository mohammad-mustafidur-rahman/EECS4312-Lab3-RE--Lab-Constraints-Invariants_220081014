# EECS 4312 — Lab 3 (Constraints, Invariants, and Tests)

Name: Mohammad Mustafidur Rahman
Student ID: 220081014

## System (Medication Dispensing)
This project models a simple medication dispensing system for a pharmacy.  
Each dispensing event records:
- `patient_id` (who received it)
- `medication` (what was dispensed)
- `dose_mg` (dose per unit, in milligrams)
- `quantity` (number of units dispensed)

## Constraints (checked when creating a DispenseEvent)
These are input rules that must be true for an event to be accepted:
1. **Dose must be positive** (`dose_mg > 0`)
2. **Quantity must be a positive integer** (`quantity` is an `int` and `> 0`)
3. **Each medication has a max daily dose**, and `dose_mg` must not exceed it
4. **Doses are in milligrams** (stored as `dose_mg`)

## Invariant (system-wide rule)
This must always hold across recorded events (for the same day):
- A patient **cannot receive the same medication more than once per day**.

> Note: Since the starter code does not include a date field, the invariant check assumes the list of `existing_events` represents events for the same day.

## Tests → Requirements mapping
The tests in `tests/test_requirements.py` validate requirements directly:

- `test_rejects_zero_or_negative_dose` → Constraint: dose must be positive  
- `test_rejects_invalid_quantity` → Constraint: quantity must be a positive integer  
- `test_enforces_max_daily_dose` → Constraint: dose must not exceed medication max dose  
- `test_prevents_duplicate_dispense_same_day` → Invariant: no duplicate same patient + medication in a day




EECS4312 Winter26:Lab3

# Title: FROM ELICITATION TO CONSTRAINTS, INVARIANTS, AND TESTS

# Medication Dispensing System Documentation

## System Description

The system is a **medication dispensing system** for a pharmacy. Its primary function is to **record each dispensing event**, capturing:

* `patient_id` (who receives the medication)
* `medication` (what is dispensed)
* `dose_mg` (amount per dose)
* `quantity` (number of doses dispensed)

The system operates under **safety, consistency, and policy rules**, ensuring no overdosing or duplicate dispensing occurs within a single day.

---

## Identified Constraints and Invariants

### Constraints (checked during dispensing)

1. `dose_mg` must be **positive**.
2. `quantity` must be a **positive integer**.
3. `dose_mg` must not exceed the **maximum daily dose** for the medication.

### Invariants (system-wide rules that must always hold)

1. A patient may **not receive the same medication more than once per day**.
2. All doses are expressed in **milligrams** (standardized units).

### Functional Requirements

* Record dispensing events.
* Track patient-medication associations.
* Automatically enforce constraints and invariants.

---

## Mapping Tests to Requirements

| Test Case                   | Requirement Validated                                    | Description                                                                                     |
| --------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Test negative or zero dose  | Constraint: dose must be positive                        | Attempt to create a `DispenseEvent` with `dose_mg ≤ 0` → should be rejected                     |
| Test quantity validity      | Constraint: quantity must be positive integer            | Attempt to create a `DispenseEvent` with `quantity ≤ 0` → should be rejected                    |
| Test duplicate dispensing   | Invariant: same medication cannot be dispensed twice/day | Attempt to add a second event for the same patient and medication on the same day → should fail |
| Test exceeding maximum dose | Constraint: max daily dose                               | Attempt to dispense a dose exceeding max daily limit → should be rejected                       |

---

This document links **system rules → constraints/invariants → requirement-driven tests**, ensuring each requirement is directly validated through testing.
