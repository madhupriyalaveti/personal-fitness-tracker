# 🏃 Personal Fitness Tracker

A simple Python command-line application for recording and viewing personal fitness and workout data.

The application stores fitness records in a CSV file and provides an easy-to-use menu for adding and viewing workout information.

## 🚀 Features

- 📝 Add new fitness and workout entries
- 📅 Record workout dates
- 🏋️ Record different workout types
- ⏱️ Record workout duration or calories burned
- 👣 Record daily steps
- ⚖️ Record weight
- 📊 View saved fitness records
- 💾 Store data locally in a CSV file
- 🖥️ Simple command-line interface

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| CSV | Local data storage |
| `datetime` | Date handling |

## 📋 Requirements

- Python 3.x
- No external Python packages are required

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/personal-fitness-tracker.git
cd personal-fitness-tracker
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Run the Application

```bash
python main.py
```

## 🖥️ How to Use

When you start the application, you will see:

```text
====== PERSONAL FITNESS TRACKER ======
1. Add New Entry
2. View All Entries
3. Exit
```

### Add a New Entry

Select option `1` and enter your information.

Example:

```text
Enter date (YYYY-MM-DD) or leave blank for today:
Workout type (e.g., Running, Cycling, Yoga): Running
Duration or calories burned: 30 minutes
Steps (optional): 5000
Weight (optional): 65 kg

✅ Fitness entry added successfully!
```

### View Entries

Select option `2` to display your saved fitness records.

Example:

```text
========== FITNESS RECORDS ==========
Date | Workout Type | Duration/Calories | Steps | Weight
2026-09-26 | Running | 30 minutes | 5000 | 65 kg
```

### Exit

Select option `3` to close the application.

```text
👋 Exiting. Stay healthy!
```

## 📂 Project Structure

```text
personal-fitness-tracker/
│
├── main.py
├── README.md
├── .gitignore
└── fitness_data.csv
```

> `fitness_data.csv` is created automatically when the application is run.

## 💾 Data Storage

Fitness records are stored locally in:

```text
fitness_data.csv
```

The CSV file contains the following fields:

```text
Date
Workout Type
Duration/Calories
Steps
Weight
```

No external database is required.

## 🔒 Privacy

This application stores fitness information locally on your computer.

Because fitness information can be personal, avoid uploading your real `fitness_data.csv` to a public GitHub repository.

## 🔮 Future Improvements

Possible improvements include:

- Add weekly and monthly workout summaries
- Calculate total workout duration
- Track calories burned
- Add BMI calculation
- Add progress charts
- Add search and filtering
- Export fitness reports
- Add a graphical user interface
- Add SQLite database support
- Add automated tests

## 🎯 Learning Objectives

This project demonstrates:

- Python functions
- File handling
- CSV file operations
- User input
- Loops and conditional statements
- Exception handling
- Date and time handling
- Building a command-line application

## 📄 License

This project is intended for educational and personal use.
