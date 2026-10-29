"""Compare plain HTTP and a fresh browser through the same proxy."""
import os
from urllib.parse import urlencode, urlsplit
import requests
from playwright.sync_api import sync_playwright

url = 'https://scholar.google.com.hk/citations?' + urlencode({'user': os.environ['GOOGLE_SCHOLAR_ID'], 'hl': 'en'})
proxy = 'http://127.0.0.1:7890'
def endpoint(url):
    p = urlsplit(url)
    return p.netloc + p.path  # Do not log query tokens, cookies or exit addresses.

s = requests.Session()
s.trust_env = False
s.proxies = {'http': proxy, 'https': proxy}
try:
    r = s.get(url, timeout=25)
    print('HTTP redirect chain:', [(x.status_code, endpoint(x.url)) for x in [*r.history, r]], flush=True)
    print('HTTP profile present:', 'gsc_prf_in' in r.text, flush=True)
    print('HTTP unusual-traffic page:', 'unusual traffic' in r.text.lower() or '/sorry/' in r.url, flush=True)
except requests.RequestException as exc:
    print('HTTP connection error:', type(exc).__name__, flush=True)
finally:
    s.close()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, proxy={'server': proxy})
    context = browser.new_context()
    page = context.new_page()
    page.on('response', lambda r: print('Browser navigation:', r.status, endpoint(r.url), flush=True) if r.request.is_navigation_request() and r.frame == page.main_frame else None)
    try:
        page.goto(url, wait_until='domcontentloaded', timeout=45000)
        print('Browser final endpoint:', endpoint(page.url), flush=True)
        print('Browser profile present:', page.locator('#gsc_prf_in').count() > 0, flush=True)
        body = page.locator('body').inner_text(timeout=5000).lower()
        print('Browser unusual-traffic page:', 'unusual traffic' in body or '/sorry/' in page.url, flush=True)
        print('Browser CAPTCHA present:', page.locator('iframe[src*="recaptcha"], #captcha-form, .g-recaptcha').count() > 0, flush=True)
    except Exception as exc:
        print('Browser navigation error:', type(exc).__name__, flush=True)
    finally:
        browser.close()
