#!/usr/bin/env bash

# Slurm configuration
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=15G
#SBATCH --gres=gpu:1
#SBATCH --constraint=a6000
#SBATCH --time=24:00:00
#SBATCH --output=tuning.log

# Run the program
./train.sh