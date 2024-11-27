#!/bin/bash

# 필요한 디렉토리 생성
sudo mkdir -p /var/log/snort
sudo chmod 777 /var/log/snort

sudo snort -A console -q -i eth0 -c /etc/snort/snort.conf -l /var/log/snort -K ascii
