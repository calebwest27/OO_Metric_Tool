# OO Metric Tool

## Overview
The OO Metric Tool is a Python application that analyzes Python classes and calculates four object-oriented software metrics:

- **WMC (Weighted Methods per Class):** Counts the methods defined in each class.
- **Cohesion (TCC):** Measures how closely methods within a class share attributes.
- **Coupling (CBO):** Counts the distinct external classes referenced by a class.
- **RFC (Response for a Class):** Counts the distinct methods defined and called by a class.

## Requirements
- Python 3.12 or later
- No external Python packages required.

## Project Files
- `main.py` – Runs the graphical user interface.
- `parser.py` – Parses Python code and identifies classes, methods, attributes, and dependencies.
- `wmc.py` – Calculates WMC.
- `cohesion.py` – Calculates cohesion.
- `coupling.py` – Calculates coupling.
- `rfc.py` – Calculates RFC.
- `hospital.py` – Sample Python program for testing the tool.

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code or a terminal.
3. Run the following command:

   ```bash
   py main.py
   ```

4. The OO Metric Tool graphical interface will open.

## How to Test

### Test 1: Upload a Python File
1. Click **Upload Python File**.
2. Select `hospital.py`.
3. Click **Analyze Code**.
4. Review the calculated metrics for each class.

### Test 2: Paste Python Code
1. Copy the code from the Book, Library, and Librarian example.
2. Paste it into the code input area.
3. Click **Analyze Code**.
4. Review the metrics displayed for all three classes.

### Test 3: Analyze a Simple Class
Paste the following example:

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grade = 0

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade
```

Click **Analyze Code** and verify that the Student class and its metrics appear.

### Test 4: No Classes Found
Paste the following:

```python
def say_hello():
    print("Hello!")
```

Click **Analyze Code**. The application should display a message indicating that no Python classes were found.

## Expected Behavior
The application should:
- Accept Python code pasted into the input area.
- Allow users to upload `.py` files.
- Identify classes and their methods.
- Calculate and display all four object-oriented metrics.
- Handle empty input and code containing no classes.
- Display an error message when invalid Python syntax is provided.

## Notes
The metrics use simplified implementations:
- WMC assigns each method a weight of 1.
- Cohesion uses Tight Class Cohesion (TCC).
- Coupling counts distinct referenced external classes.
- RFC counts distinct method names defined and called within the class.

A cohesion result of N/A means the class does not have enough methods to calculate the metric.
