import pandas as pd
import random
import time

allowed_jobs = ['Door Holder', 'Computer Tech/Chromies', 'Messenger', 'Teacher Assistant', 
             'Librarian', 'Calendar Clerk', 'Lunch Monitor', 'Substitute', 'Mailbox Attendant',
             'Desk Monitor', 'Supply Manager', 'Pencil Monitor', 'New Absent Helper', 'Book Ends', 
             'Phone Assistant', 'Hallway Monitor girl', 'Hallway Monitor boy', 
             'Morning Announcer', 'Clean up', 'Banker', 'Paper Assistant' ]
# Load the Excel file
df = pd.read_excel(r'C:\Users\dr3am\Downloads\Job Application Responses.xlsx')

# Extract the necessary columns
job_options = df['What classroom job are you applying for?\n(please list 3 options)'].str.split(',', expand=True)
emails = df['Email Address']

# List to keep track of assigned jobs
assigned_jobs = []

def assign_unique_job(options):
    random.shuffle(options)  # Shuffle job options for randomness
    for job in options:
        if job in allowed_jobs and job not in assigned_jobs:  # Ensure the job hasn't been assigned yet
            assigned_jobs.append(job)
            return job
    return None  # If all jobs are taken, return None

def job_assignment_process():
    assigned_jobs.clear()  # Clear previous assignments
    assignments = {}  # Initialize the assignments dictionary
    
    for index, row in job_options.iterrows():
        email = emails[index]
        options = [row[0], row[1], row[2]]
        job = assign_unique_job(options)
        if job:
            assignments[email] = job  # Assign job to the email
        else:
            print(f"No available jobs for {email}")

    # Print the final assignments
    for email, job in assignments.items():
        print(f'{email} has been assigned to {job}')

# Run the assignment process once initially
job_assignment_process()

# Repeat the process every 4 months
while True:
    time.sleep(4 * 30 * 24 * 60 * 60)  # Wait for 4 months
    job_assignment_process()
