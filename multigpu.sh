#!/bin/bash

# Array of GPU instance IPs
gpu_instances=("gpu-instance-ip1" "gpu-instance-ip2" "gpu-instance-ip3")

# Loop through each GPU instance
for instance in "${gpu_instances[@]}"
do
    # Copy data and script to GPU instance
    scp /path/to/data-part-${instance} [user]@${instance}:/data/location
    scp /path/to/script.sh [user]@${instance}:/script/location

    # Execute the script on GPU instance
    ssh [user]@${instance} "bash /script/location/script.sh /data/location/data-part-${instance}"
done