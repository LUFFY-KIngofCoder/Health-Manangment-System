# Health Management System

The Health Management System is a Python-based GUI application built using the `tkinter` library. This system helps individuals log and retrieve data related to their health activities. It allows users to log and store information about food and exercise routines and view the logs later.

## Features

- **Log Data**: Users can log health-related information such as food intake and exercise routines. The information is saved in a text file.
- **Retrieve Data**: Users can retrieve and view their logged data from the text files.
- **Date and Time**: Each entry is saved with the current date and time.

## How It Works

1. **User Input**: Users enter their name, select a task (either "Food" or "Exercise"), and input data related to the task.
2. **Logging Data**: When the "Log Data" button is clicked, the data is saved into a text file named using the user's name and selected task.
3. **Retrieving Data**: When the "Retrieve Data" button is clicked, the app fetches the contents of the relevant text file and displays it.

## Files

- The data for each user is saved in a text file named `[name]'s [task].txt`. The file is stored in the same directory as the script.

## Requirements

Ensure you have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

This script uses `tkinter`, which is included with Python by default.

## Installation

Clone or download the repository:

```bash
git clone https://github.com/your-username/health-management-system.git
```

## Usage

**1. Log Data:**
- Enter your name, select the task (Food/Exercise), and enter the data.
- Click "Log Data" to save your entry.
**2. Retrieve Data:**
- Enter your name and select the task.
- Click "Retrieve Data" to view your saved entries.

## Example:
**1. User logs data for food:**

- Name: John Doe
- Task: Food
- Data: Ate a balanced breakfast.

**2. User retrieves data:**

- Name: John Doe
- Task: Food
- The entry appears as:
```css
[2025-02-01 08:30:00] Ate a balanced breakfast.
```
