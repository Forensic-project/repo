1. run snort
sudo snort -c /etc/snort/snort.conf -i eth0

2. update snort_logs.txt
sudo python ~/test_forensic/test_snort/snort_monitor.py

3. run server
python ~/test_forensic/manage.py runserver

4. attack(in WSL2 Kali Linux)
sudo hping3 -1 -i u9000 192.168.209.129
