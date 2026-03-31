# Quantium role
This repo contains everything you need to get started on the program! Good luck!
# Quantium Data Processing & Dashboard

Built using Python, Pandas, Dash, Plotly and Pytest.

This project is part of the Quantium Data Analytics Virtual Experience.

---

## What I did

- Combined multiple CSV files into one dataset  
- Filtered data for "pink morsel"  
- Cleaned price column (removed $ and converted to float)  
- Calculated total sales using price × quantity  
- Generated a final structured output CSV  

---

## Dashboard

Created a simple interactive dashboard using Dash:

- Line chart showing sales over time  
- Region filter (north, south, east, west, all)  
- Basic styling with dark theme  
- Dynamic updates using callbacks  

---

## Testing

Used pytest to verify UI components:

- Checked header is present  
- Checked graph is present  
- Checked region filter exists  
- Ensured layout structure is correct  

---

## CI (Automation)

- Created a bash script (`run_tests.sh`)  
- Automatically runs test suite  
- Returns exit code:
  - 0 → success  
  - 1 → failure  

This can be integrated into CI tools like GitHub Actions.

---

## How to run

### 1. Install dependencies

pip install pandas dash plotly pytest

---

### 2. Run dashboard

python improved_dash_app.py

Then open: http://127.0.0.1:8050/

---

### 3. Run tests

pytest

---

### 4. Run CI script

bash run_tests.sh

---

## Project Structure

quantium-project/

- improved_dash_app.py → dashboard  
- test_app.py → tests  
- output.csv → processed data  
- run_tests.sh → automation script  
- README.md  

---

## What I learned

- Data cleaning and transformation using pandas  
- Building dashboards with Dash and Plotly  
- Creating interactive filters using callbacks  
- Writing basic tests with pytest  
- Understanding CI concepts (automated testing)  

---

## Summary

This project covers an end-to-end workflow:
data processing → visualization → testing → automation

It helped me understand how real-world data projects are structured.
