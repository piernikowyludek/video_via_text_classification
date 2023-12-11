#!/bin/bash
mkdir /efs/data/
wget -o /efs/data/UCF50.rar https://www.crcv.ucf.edu/data/UCF50.rar --no-check-certificate
echo y | sudo apt install unrar-free
unrar /efs/data/UCF50.rar