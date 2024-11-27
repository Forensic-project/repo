import requests
import time

def test_xss():
    target_url = "http://127.0.0.1:8000/test-xss"
    
    # XSS 테스트 페이로드
    payloads = [
        "<script>alert('XSS Test 1')</script>",
        "javascript:alert('XSS Test 2')",
        "<img src=x onerror=alert('XSS Test 3')>",
        "<svg/onload=alert('XSS Test 4')>",
        "<body onload=alert('XSS Test 5')>",
        "<iframe onload=alert('XSS Test 6')>",
        "'-alert('XSS Test 7')-'",
        "<scr<script>ipt>alert('XSS Test 8')</scr</script>ipt>"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    print("Starting XSS tests...")
    
    for payload in payloads:
        print(f"\nTesting payload: {payload}")
        try:
            # GET 요청으로 테스트
            print("Sending GET request...")
            response = requests.get(f"{target_url}?input={payload}", headers=headers)
            print(f"GET Status: {response.status_code}")
            
            # 잠시 대기하여 로그 확인 시간 제공
            time.sleep(1)
            
            # POST 요청으로 테스트
            print("Sending POST request...")
            response = requests.post(target_url, data={"input": payload}, headers=headers)
            print(f"POST Status: {response.status_code}")
            
            # 다음 테스트 전 잠시 대기
            time.sleep(1)
            
        except Exception as e:
            print(f"Error during test: {e}")
        
        print("-" * 50)

if __name__ == "__main__":
    test_xss()
