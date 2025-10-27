# utils/request_utils.py
import requests

def send_post_request(url: str, data: dict):
    """Wrapper around requests.post with basic error handling."""
    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")
    return response
