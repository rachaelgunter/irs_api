This IRS website certainly leaves much to be desired.
Writing a program to be able to easily parse through
the information available was a fun and helpful use of 
my time. I thoroughly enjoyed this project.

# Program Description:

This program queries the IRS public API.

## PART ONE 
Taking in a list of tax form names and returning some 
information about the results. 
The information is returned in JSON formatting.
The information includes:
    -Form Number
    -Form Title
    -Maximum and minimum years the form is available for download    

##PART TWO
Taking in the name of a tax form and a range of years, you will
be returned all PDFS available with in that range. 

#Installation

```bash
pip install foobar
```

# How To Use:

## Part One
```python
pinwheel_query("Form W-2", "Form 1095-C")
```

## Part Two
```python
pdf_query("Form W-2", "2018-2020")
```
