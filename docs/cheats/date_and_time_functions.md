# Date and Time Functions in Python

## Introduction to Date and Time Functions

| Title                               | Concept                                                           | Codes                                         |
|-------------------------------------|-------------------------------------------------------------------|-----------------------------------------------|
| Importance of Date and Time Functions | Essential for managing temporal data and operations in programming. |                                           |
| Overview of Date and Time in Python | Utilization of date and time modules, formats, and operations in Python. |                                             |

### Importing Date and Time Modules

1. **Date and Time Modules in Python:** 
    - `datetime`: Handles date and time values.
    - `time`: Focuses on time-related operations.
    - `calendar`: Aids in calendar-related functionality.

2. **Common Use Cases:**
    - Scheduling tasks at specific times.
    - Calculating durations between two dates or times.
    - Displaying dates and times in different formats.

## Working with Dates in Python

### Date Objects

| Title                               | Concept                                                           | Codes                                         |
|-------------------------------------|-------------------------------------------------------------------|-----------------------------------------------|
| Creating Date Objects               | Generating date instances in Python.                             | `import datetime`<br>`date_obj = datetime.date(year, month, day)` |
| Accessing Date Components           | Retrieving individual date components like day, month, and year. | `year = date_obj.year`<br>`month = date_obj.month`<br>`day = date_obj.day` |

### Date Formatting

| Title                               | Concept                                                         | Codes                                         |
|-------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Formatting Dates with `strftime()`  | Converting date objects into custom string representations.     | `formatted_date = date_obj.strftime("%Y-%m-%d")` |
| Parsing Dates with `strptime()`     | Interpreting strings to create date objects based on formats.    | `date_str = "2023-05-15"`<br>`parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")` |

### Date Arithmetic

| Title                               | Concept                                                         | Codes                                         |
|-------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Adding and Subtracting Dates        | Performing arithmetic operations on date objects.                | `new_date = date_obj + datetime.timedelta(days=7)`<br>`difference = date_obj2 - date_obj1` |
| Calculating Date Differences        | Determining the duration between two date points.                | `days_difference = (date2 - date1).days` |

## Working with Times in Python

### Time Objects

| Title                               | Concept                                                         | Codes                                         |
|-------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Creating Time Objects               | Creating time instances in Python.                               | `time_obj = datetime.time(hour, minute, second)` |
| Accessing Time Components           | Accessing individual time elements like hour, minute, second.   | `hour = time_obj.hour`<br>`minute = time_obj.minute`<br>`second = time_obj.second` |

### Time Formatting

| Title                               | Concept                                                         | Codes                                         |
|-------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Formatting Times in Different Timezones | Presenting time values in specific time zone formats.         | `formatted_time = time_obj.strftime("%H:%M:%S")` |
| Converting Time Formats             | Transforming time objects to alternate representations.         | `time_str = "15:30:00"`<br>`new_time = datetime.datetime.strptime(time_str, "%H:%M:%S").time()` |

### Time Arithmetic

| Title                               | Concept                                                         | Codes                                         |
|-------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Adding and Subtracting Times        | Performing arithmetic operations on time representations.       | `new_time = time_obj + datetime.timedelta(hours=3)`<br>`difference = time2 - time1` |
| Calculating Time Differences        | Calculating the time interval between two time instances.       | `time_difference = datetime.datetime.combine(date, time2) - datetime.datetime.combine(date, time1)` |

## Combining Dates and Times

### Datetime Objects

| Title                               | Concept                                                         | Codes                                         |
|-------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Creating Datetime Objects           | Generating datetime values by combining dates and times.        | `datetime_obj = datetime.datetime(year, month, day, hour, minute, second)` |
| Manipulating Datetime Objects       | Modifying and adjusting datetime objects as needed.             | `new_datetime = datetime_obj.replace(year=2023)` |

### Datetime Formatting

| Title                               | Concept                                                         | Codes                                         |
|-------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Formatting Datetimes                | Representing datetime values in various predefined formats.    | `formatted_datetime = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")` |
| Handling Timezones in Datetimes     | Managing and converting datetime objects across different time zones. | `tz_datetime_obj = datetime_obj.astimezone(timezone_object)` |

## Working with Timezones

### Timezone Handling in Python

| Title                               | Concept                                                         | Codes                                         |
|-------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Timezone Localization               | Adapting datetime representations to specific time zones.       | `localized_datetime = datetime_obj.astimezone(pytz.timezone('America/New_York'))` |
| Timezone Conversion                 | Converting datetime values between different time zones.       | `converted_datetime = datetime_obj.astimezone(pytz.timezone('Asia/Tokyo'))` |

### Dealing with Daylight Saving Time

| Title                               | Concept                                                         | Codes                                         |
|-------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Daylight Saving Time Adjustments    | Handling changes in time offset due to daylight saving shifts.  | `localize = pytz.timezone('America/New_York').localize(datetime_obj, is_dst=None)` |
| Handling Ambiguous Datetimes        | Managing ambiguous datetime representations during transitions. | `normalized_datetime = tzinfo_obj.normalize(datetime_obj, is_dst=None)` |

## Date and Time Functions in Python Standard Library

### datetime Module

| Title                               | Concept                                                         | Description                                   |
|-------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Date and Time Functions in the `datetime` module | Key functions for date and time operations in Python.          | Includes methods for creation, manipulation, and comparison of datetime objects. |
| Commonly Used Methods in the `datetime` module | `datetime.now()`, `datetime.strptime()`, `datetime.strftime()`. | Enables date parsing, formatting, and retrieval operations. |

### time Module

| Title                               | Concept                                                         | Description                                   |
|-------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Time-related Functions in the `time` module | Functions dedicated to time-specific operations.              | Offers precision timing and clock functions for time management. |
| Managing Time in Python              | Time management utilities like sleep, performance analysis, etc. | Supports controlling time delays, performance measuring, and calibration tasks. |

By mastering these date and time functions in Python, you can efficiently handle temporal data and enhance the functionality of your Python programs.