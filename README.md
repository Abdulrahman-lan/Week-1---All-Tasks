# Python Data Processing Portfolio

This repository contains a structured series of technical activities focused on data manipulation, statistical analysis, and file handling using Python and Pandas.

---

## Technical Activity Breakdown

### Task 01: Function Refactoring and Statistical Logic
* **Objective:** Replace repetitive statistical logic with reusable components.
* **Technical Details:** Implementation of a centralized `calculate_stats` function to process data categories, returning comprehensive dictionaries containing mean and maximum values.

### Task 02: Utility Library Development
* **Objective:** Building a modular utility library for data preprocessing.
* **Technical Details:** Developing a suite of reusable functions for data normalization (Min-Max), outlier removal, train-test splitting (80/20 ratio), and label encoding for categorical data.

### Task 03: Dataset Cleaning with Pandas and Lambda
* **Objective:** Streamlining data cleaning workflows using the Pandas library.
* **Technical Details:** Utilizing `.apply()` with lambda functions to sanitize currency strings (removing symbols and commas), handling missing values (imputation), and implementing feature engineering to categorize price points.

### Task 04: Nested Data Parsing (Student Database)
* **Objective:** Navigating and analyzing complex nested dictionary structures.
* **Technical Details:** Implementing logic to extract specific data points from deep hierarchies, calculating weighted GPAs based on course credits, and performing cross-student data aggregation to identify top performers.

### Task 05: JSON Integration and Persistence Workflow
* **Objective:** Establishing a robust I/O pipeline for configuration and results.
* **Technical Details:** Leveraging the `json` and `pathlib` libraries to load external training configurations and persist simulation results to disk using safe context management.

---

## Project Structure

As organized in this repository:

1. **All tasks/**
   * Contains the original source requirements and baseline templates provided for the activities.

2. **All tasks - solved/**
   * Contains the finalized implementations, optimized scripts, and verified solutions for each task.

---

## Core Competencies Demonstrated
* **Data Engineering:** Sanitizing and preparing raw datasets for analysis.
* **Functional Programming:** Writing DRY (Don't Repeat Yourself) code through modular functions.
* **Library Proficiency:** Practical application of `Pandas`, `JSON`, and `Pathlib`.
* **Analytical Logic:** Complex GPA calculation and data categorization.

---
**Developed by:** Abdulrahman