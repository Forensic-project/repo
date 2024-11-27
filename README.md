1. 스노트 실행<br>
sudo snort -c /etc/snort/snort.conf -i eth0<br>
sudo systemctl restart snort

2. 로그 자동 변환 프로그램 실행<br>
sudo python ~/test_forensic/test_snort/snort_monitor.py

3. 정상 핑 공격<br>
ping 8.8.8.8

4. 실제 공격<br>
sudo hping3 -1 -i u9000 192.168.209.129
