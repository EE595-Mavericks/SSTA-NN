#!/usr/bin/env bash

# Slurm configuration
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=20G
#SBATCH --gres=gpu:1
#SBATCH --constraint=2080ti
#SBATCH --time=24:00:00
#SBATCH --output=tuning.log

# Run the program
./train.sh