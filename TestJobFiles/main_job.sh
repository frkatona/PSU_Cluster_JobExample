#!/bin/bash
#SBATCH --job-name=APK_jobTest
#SBATCH --output=output_%j.txt
#SBATCH --error=error_%j.txt
#SBATCH --time=01:00:00
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=apk5101@psu.edu
module load anaconda/2023.09
echo "Starting job at $(date)"
python analyze_data.py
echo "Job finished at $(date)"