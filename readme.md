# Anamoly Detection Project: Curriculum Logs

## Project Description
 - The purpose of this project is to explore the codeup database containing the curriculum access logs for different user_id's and their corresponding IP addresses.

## Project Goals
 - Create a Final Jupyter Notebook that reads like a report and follows the methodolgies for anamoly detection
 - Answer the five following question about the dataframe
    - 1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
    - 2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
    - 3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
    - 4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
    - 5. Which lessons are least accessed?


### Executive Summary

The purpose of this notebook is to find anomalous activity in a dataset that monitors the Codeup curriculum access. We will be using pages accessed, user_id, timestamps, and other columns to find anomalous activity

#### Key Findings:
 
##### Lesson Traffic
 - Most Accessed Lessons:
     - MySQL: Tables Lesson: 7922 pings
     - Javascript I: Introduction Working With Data Types Operators and Variables Lesson: 8302 pings
     - Javasvript I: Javascrip-with-html : 8199 pings
 
 - Least Accessed Lessons:
     - anomaly-detection/discrete-probabilistic-methods
     - storytelling/create
     - clustering/kmeans-part1
     - python/series
     - slides/exceptions_and_error_handling

##### Suspicious Activity
 - Suspicious IP Adress: 204.44.112.76
     - Accessed several pages at machine like speeds according to time stamps corresponding with pages accessed

##### Data Science Cohort Lesson Differences

Looking at the lessons accessed by the data science cohorts from Bayes to Florence it was determined that pre-Easley the most accessed lessons were for the regression methodology. Whereas Easley and Florence glossed over regression more and spent more time with classifcation.

##### Inactive Students

We were also able to pinpoint students that had the least curriculum activity and were able to determine those students most likely left the program at an early date because of their access pings consisted of one day's worth of access.

#### Data Dictionary


| Column        | Description               | Data_type  |
|---------------|---------------------------|------------|
| date          | date of curriculum access | datetime64 |
| time          | time of curriculum access | datetime64 |
| endpoint/page | webpage accessed          | object     |
| user_id       | ID of user                | int64      |
| cohort_id     | ID of cohort              | float64    |
| source_ip     | IP address of user        | object     |
| name          | cohort name               | object     |
| start_date    | start date of cohort      | datetime64 |
| end_date      | end date of cohort        | datetime64 |
| created_at    | time of record creation   | object     |
| updated_at    | time of record update     | object     |
| program_id    | ID of program             | float64    |
