import time
from functools import wraps


def retry(max_retries=3, delay=5, exceptions=(Exception,)):
    """Decorator that retries a function on failure.

    Args:
        max_retries: Number of retry attempts.
        delay: Seconds to wait between retries.
        exceptions: Tuple of exception types to catch and retry on.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"⚠️ Attempt {attempt}/{max_retries} failed: {e}")
                    if attempt < max_retries:
                        print(f"🔄 Retrying in {delay}s...")
                        time.sleep(delay)
                    else:
                        print(f"❌ Failed after {max_retries} attempts")
                        raise
        return wrapper
    return decorator
