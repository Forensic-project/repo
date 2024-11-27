1. 스노트 실행
sudo snort -c /etc/snort/snort.conf -i eth0

sudo systemctl restart snort

2. 로그 자동 변환 프로그램 실행
sudo python ~/test_forensic/test_snort/snort_monitor.py

3. 정상 핑 공격
ping 8.8.8.8

4. 실제 공격
sudo hping3 -1 -i u9000 192.168.209.129
