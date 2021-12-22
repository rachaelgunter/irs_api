This IRS website certainly leaves much to be desired.
Writing a program to be able to easily parse through
the information available was a fun and helpful use of 
my time. I thoroughly enjoyed this project.

# Program Description:

This program queries the IRS public API.
Written in Python 3.9.1

## PART ONE 
Taking in a list of tax form names and returning some 
information about the results. 
The information is returned in JSON formatting.
The information includes:
    -Form Number
    -Form Title
    -Maximum and minimum years the form is available for download    

## PART TWO
Taking in the name of a tax form and a range of years, you will
be returned all PDFS available with in that range. 

#Installation

```bash
$ pip3 install requirements.txt
```

# How To Use:

## Part One
Example of how to enter the parameters for the first function:
```python
pinwheel_query("Form W-2", "Form 1095-C")
```
JSON output example:
```python
[{'form_number': 'Form W-2', 'form_title': 'Wage and Tax Statement (Info Copy Only)', 'min_year': 1954, 'max_year': 2022}, {'form_number': 'Form 1095-C', 'form_title': 'Employer-Provided Health Insurance Offer and Coverage', 'min_year': 2014, 'max_year': 2021}]
```

## Part Two
Example of how to enter the parameters for the first function:
```python
pdf_query("Form W-2", "2018-2020")
```
