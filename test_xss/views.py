from django.shortcuts import render
from django.http import HttpResponse
import re

def test_xss(request):
    # GET과 POST 모두에 대해 XSS 탐지
    if request.method == 'POST':
        xss_payload = request.POST.get('xss_field', '')
    else:
        xss_payload = request.GET.get('xss', '')

    xss_patterns = [
        r'<script',
        r'javascript:',
        r'onerror=',
        r'base64',
        r'alert\(',
        r'document\.cookie'
    ]

    # XSS 탐지 여부만 확인
    is_xss = any(re.search(pattern, xss_payload, re.IGNORECASE) for pattern in xss_patterns) if xss_payload else False

    return render(request, 'test_xss/test_xss.html', {'is_xss': is_xss})
