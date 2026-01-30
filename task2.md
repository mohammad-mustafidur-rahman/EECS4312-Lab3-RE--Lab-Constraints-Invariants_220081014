# Task 2 — Requirement Classification (8 items)

1) <What kind of patient ID should the system accept (non-empty, numbers only, etc.)?, Constraint>  
   Justification: This is basically an input rule — it tells us what’s valid and what should be rejected.

2) <How should medications be identified (case-sensitive or not, free text vs standard codes, allowed characters)?, Constraint>  
   Justification: This sets boundaries on what the medication field can look like, so it’s a validation constraint.

3) <What exactly counts as “one day” (calendar day vs last 24 hours, timezone)?, Constraint>  
   Justification: We can’t apply “per day” rules unless we define what a day means. That definition limits how the system behaves.

4) <Do we need to record the date/time for each dispensing event, and is it entered or auto-generated?, Functional Requirement>  
   Justification: This is a feature the system may need to provide (recording and saving timestamps), not just a restriction.

5) <If a medication isn’t in the max daily dose list, what should the system do (reject, override, default)?, Constraint>  
   Justification: This tells the system how to handle an invalid/unknown medication input, so it’s part of the input handling rules.

6) <Should the max daily dose be checked per event or as a total across the whole day for that patient?, Invariant>  
   Justification: If the rule is cumulative, it becomes something that must always remain true across the system’s stored events for the day.

7) <Are decimal doses allowed (like 2.5 mg), and what rounding rules should we follow?, Constraint>  
   Justification: This limits what dose values are acceptable and how precise they can be, so it’s a constraint.

8) <Can a pharmacist override the safety rules, and if yes what must be recorded (who, why, when)?, Functional Requirement>  
   Justification: Allowing overrides + logging details is system behavior the software must support, so it