#!/usr/bin/python3
#Project 1: Run Microarchitecture ARM A76 with diferent workloads
import os
import itertools

print("¡¡START SIMULATION!!")

# Memory Options
l1i_size = ['32kB', '128kB']
l1i_lat = [2,4]
l1d_size = ['128kB', '256kB']
l1d_lat = [2,4]
l2_size = ['1MB', '2MB']
l2_lat = [9, 12]
# CPU Options
fetch_width = [8,12]
decode_width = [8]
fb_entries = [16,64]
fq_entries = [16]
num_fu_intALU = [2,4]


gem5_path = "/home/administrador/gem5/"
cmd_path = "build/ARM/gem5.opt"
config_file_path = "/configs/CortexA76/CortexA76.py"

#Workloads Options
enc_workload = "workloads/mp3_enc/mp3_enc"
enc_resources = "workloads/mp3_enc/mp3enc_testfile.wav workloads/mp3_enc/mp3enc_outfile.mp3"

cpu_features = list(itertools.product(l1i_size, l1i_lat, l1d_size, l1d_lat, l2_size,l2_lat,fetch_width,decode_width, fb_entries,fq_entries,num_fu_intALU))

def run_command(cmd,config_file,workload,resources,cpu_features,index,sim_name="mp3"):
	command_enc = f"pwd && {cmd} --stats-file=stats_{sim_name}_{index}.txt --json-config=config_sim_{index}.json {config_file} --cmd={workload} --options='{resources}' --l1i_size={combo[0]} --l1i_lat={combo[1]} --l1d_size={combo[2]} --l1d_lat={combo[3]} --l2_size={combo[4]} --l2_lat={combo[5]} --fetch_width={combo[6]} --decode_width={combo[6]} --fb_entries={combo[8]} --fq_entries={combo[9]} --num_fu_intALU={combo[10]}"

	os.command(command)

	extracted_metrics = []
	with open(f"m5out/{sim_name}/stats_sim_{index}.txt", 'r') as stats_file:
        for line in stats_file:
            if "system.cpu.cpi" in line:
                extracted_metrics.append(line.strip())
                break

print("Select Workload Option")
opt = input("Select Workload Option")
try:
	run_command(gem5_path+cmd_path,gem5_path+config_file_path,gem5_path+workload_path,gem5_path+resources_path,cpu_features)
	
