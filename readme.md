# PSU Roar Collab HPC Example Files for Job Submission

This example includes 3 components:

1. CSV file of data
2. Python script that models data from the CSV and reports the results
3. Bash script that handles resource allocation, job submission, result exporting, and user notification

## Usage

1. Go to the RCPortal ([rcportal.psu.edu](https://rcportal.hpc.psu.edu/pun/sys/dashboard/)) and log in with your PSU credentials
2. In the taskbar, click on "Jobs" and then "Job Composer"
3. In the "Jobs" window, click "Edit Files" and upload the .csv, .py, and .sh files (may have to delete old .sh file)
4. Return to the job composer and click "Submit"
5. Wait for email notification of job completion
6. Open the file manager to view or download any output and error files

## Careful

- be sure the environment is properly set up on the cluster (error handling is tedious)
  
- be sure the LF line breaks are enabled in VS Code for the .sh file (CRLF will cause errors)...I had to drag in a local .sh file that I edited in VS Code to get it to work sometimes

- dragging and dropping on the file manager page is the easiest way to transfer files from your local machine, but there is no warning if you are replacing an existing file so be careful and when creating files, try to use the job ID in the file name with "%j" to avoid unintentional overwriting

## Details and Documentation

- SLURM is used to manage the job scheduling and resource allocation on the cluster.
  - [SLURM Documentation](https://slurm.schedmd.com/documentation.html)

- SLURM batch script breakdown:
  - #!/bin/bash : specifies the shell the system should use (bash here)
- #SBATCH : specifies the options for the job scheduler including number of nodes/tasks/CPUs-per-task, the time limit, and where to send the output/error
- "%j" : the job ID
- "--mail-type=BEGIN,END,FAIL" : send an email when the job starts, ends, or fails

the email includes an "exit code"

- 0 : successful completion
- 1 : generic failure
- 2 : invalid usage (shell syntax error)

## To-do

- [ ] figure out how to deal with python libraries in the job script (just make sure they're installed on the cluster for my account?  import them as modules with the bash script?)

- [ ] if a job does not complete before the time limit, do the output and error files still get made or should the script account for this possibility by routinely updating its progress and be coded such that it can resume from where it left off?

- [ ] if I load a required module in the bash script, will it be available to the python script?  And does it stay loaded until deallocation?