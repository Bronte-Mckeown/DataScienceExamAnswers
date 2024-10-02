# MCQ and Coding evaluation

This file contains all my answers to the MCQ and Coding evaluation.

## MCQ

Q1. A

Q2. C

Q3. D

Q4. C

Q5. B

Q6. B

Q7. B

Q8. A

Q9. B

Q10. A

## Query Evaluation

Part 1.

Identify and correct any errors in the code.

- The sub query includes the 'OR department_name' = NULL' which isn't right because the goal is to view patients
data from the cardiology department specifically. Needs removing:
```
department_id = (SELECT department_id FROM departments WHERE department_name = 'Cardiology')
```

- Even if this was what they wanted, it should be 'IS NULL' and not '= NULL'
```
department_name = (SELECT department_name FROM departments WHERE department_name = 'Cardiology' OR department_name IS NULL)
```

- LIMIT 1 is problematic as it will only return one row and the aim is to identify patients (plural) with the highest number
of admissions. Needs removing:
```
ORDER BY admission_count DESC;
```

Improving or optimising the code:

- The sub query uses a combination of department_id instead of just using department_name, which could lead to inconsistencies
and is potentially redundant.
```
department_name = (SELECT department_name FROM departments WHERE department_name = 'Cardiology')
```

- To speed query up, you could create an index on department_name.
```
CREATE INDEX idx_department_name ON departments(department_name);
```

- Admission_data evaluation statement might not work because it supplies a string, rather than a date object. Would
be better to explicitly convert to date object.
```
STR_TO_DATE('2015-01-01', '%Y-%m-%d')
```

- Instead of using COUNT(*), might be better to specify specific column (e.g., admission_id)
```
COUNT(admission_id) as admission_count
```
