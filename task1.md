# Task 1 — Requirements Elicitation Questions (8 additional)

1) What kind of patient ID should the system accept (must it be non-empty, numbers only, etc.)?
2) How should medications be identified (case-sensitive vs case-insensitive and what characters are allowed)?
3) What exactly counts as “one day” for the rules (calendar day vs last 24 hours, and which timezone should be used)?
4) Do we need to store the date/time for each dispensing event?
5) If a medication is not in the “maximum daily dose” list, what should the system do (reject it or allow it with an override)?
6) Is the “maximum daily dose” limit checked per single dispensing event, or should the system add up all doses for that medication for the same patient in a day?
7) Can doses be decimal values (like 2.5 mg)?
8) Can a pharmacist override safety rules in special cases? If yes, what must be recorded (who approved it, reason and date/time)?