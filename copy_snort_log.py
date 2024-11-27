import shutil
import time
import os

SOURCE_LOG = '/var/log/snort/snort.log'
DEST_LOG = '/home/kali/test_forensic/test_snort/snort_logs.txt'

def copy_log():
    try:
        shutil.copy2(SOURCE_LOG, DEST_LOG)
        print(f"Log copied at {time.ctime()}")
    except Exception as e:
        print(f"Error copying log: {e}")

if __name__ == "__main__":
    while True:
        copy_log()
        time.sleep(10)  # 10초마다 실행
