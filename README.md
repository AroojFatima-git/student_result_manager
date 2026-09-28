# Student Result Manager

A console-based Python application to manage student results. It calculates total marks, percentage and grade, and stores everything in a CSV file.

## Features
- Add students with marks for 5 subjects (input validation included)
- Automatic total, percentage and grade calculation
- View all records in a formatted table
- Search a student by roll number
- Find the class topper and class average
- Delete a record
- Data is saved permanently in `results.csv`

## Concepts Used
- Functions and modular code
- Lists, dictionaries and list comprehensions
- File handling with the `csv` module
- Input validation using `try/except`

## How to Run
```bash
python result_manager.py
```
Requires Python 3.8 or above. No extra libraries needed.

## Sample Output
```
Roll    Name                Total   %       Grade
--------------------------------------------------
1       Ayesha              410.0   82.0    A+
2       Sana                355.0   71.0    A
```

## Author
Arooj Fatima, BS Artificial Intelligence, GSCWU Bahawalpur
