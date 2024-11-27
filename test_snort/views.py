import re
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
import os

def parse_snort_log(log_file_path):
    events = []
    with open(log_file_path, 'r') as file:
        content = file.read()
        event_blocks = content.split('(Event)')[1:]

        for block in event_blocks:
            event_data = {}
            
            # Extract required fields using regular expressions
            event_second_match = re.search(r'event second: (\d+)', block)
            sig_id_match = re.search(r'sig id: (\d+)', block)
            classification_match = re.search(r'classification: (\d+)', block)
            ip_source_match = re.search(r'ip source: ([\d.]+)', block)
            ip_destination_match = re.search(r'ip destination: ([\d.]+)', block)
            src_port_match = re.search(r'src port: (\d+)', block)
            dest_port_match = re.search(r'dest port: (\d+)', block)
            protocol_match = re.search(r'protocol: (\d+)', block)
            msg_match = re.search(r'msg: "(.*?)"', block)  # 추가: msg 필드 파싱

            if all([event_second_match, sig_id_match, classification_match, ip_source_match,
                    ip_destination_match, src_port_match, dest_port_match, protocol_match]):
                
                event_second = int(event_second_match.group(1))
                event_time = datetime.utcfromtimestamp(event_second).strftime('%H:%M:%S')
                
                # XSS 공격 여부 확인 (sig_id 기반)
                is_xss = sig_id_match.group(1) in ['1000001', '1000002', '1000003', '1000004', '1000005', '1000006']
                
                event_data = {
                    'event_time': event_time,
                    'sig_id': sig_id_match.group(1),
                    'classification': classification_match.group(1),
                    'ip_source': ip_source_match.group(1),
                    'ip_destination': ip_destination_match.group(1),
                    'src_port': src_port_match.group(1),
                    'dest_port': dest_port_match.group(1),
                    'protocol': protocol_match.group(1),
                    'is_xss': is_xss,
                    'msg': msg_match.group(1) if msg_match else ''  # 추가: msg 정보 저장
                }
                events.append(event_data)

    return events

def snort_log_view(request):
    log_file_path = '/home/kali/test_forensic/test_snort/snort_logs.txt'
    events = parse_snort_log(log_file_path)
    recent_events = events[-30:][::-1]

    return render(request, 'test_snort/snort_log.html', {'events': recent_events})

#def get_latest_logs(request):
#    log_file_path = '/home/kali/test_forensic/test_snort/snort_logs.txt'
#    events = parse_snort_log(log_file_path)
#    return JsonResponse({'events': events})
