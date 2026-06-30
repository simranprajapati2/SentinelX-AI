from time import time

request_history = {}

MAX_REQUESTS = 10
WINDOW_SECONDS = 60

def is_rate_limited(ip_address):


 now = time()

 if ip_address not in request_history:
    request_history[ip_address] = []

 request_history[ip_address] = [
    t for t in request_history[ip_address]
    if now - t < WINDOW_SECONDS
]

 if len(request_history[ip_address]) >= MAX_REQUESTS:
    return True

 request_history[ip_address].append(now)

 return False

