import paramiko
import time
from retry import retry

HOST = "localhost"
PORT = 2222
USERNAME = "demo"
PASSWORD = "demo"


@retry(max_retries=3, delay=5)
def connect_sftp():
    """Connect to SFTP server."""
    transport = paramiko.Transport((HOST, PORT))
    transport.connect(username=USERNAME, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)
    print("✅ Connected to SFTP")
    return sftp, transport


def close_sftp(sftp, transport):
    """Safely close SFTP connection."""
    try:
        if sftp:
            sftp.close()
        if transport:
            transport.close()
    except Exception:
        pass


@retry(max_retries=3, delay=15)
def poll_for_file(target_file, directory=".", interval=5, timeout=10):
    """Poll SFTP server for a specific file.

    Args:
        target_file: Name of the file to look for.
        directory: Directory to search in.
        interval: Seconds between each poll.
        timeout: Max seconds to wait before giving up.
    """
    elapsed = 0

    while elapsed < timeout:
        sftp, transport = connect_sftp()
        try:
            files = sftp.listdir(directory)
            print(f"🔍 Polling... Found files: {files}")

            if target_file in files:
                print(f"✅ File '{target_file}' found!")
                return True
        finally:
            close_sftp(sftp, transport)

        print(f"⏳ Waiting {interval}s... ({elapsed}/{timeout}s elapsed)")
        time.sleep(interval)
        elapsed += interval

    raise TimeoutError(f"'{target_file}' not found after {timeout}s")


if __name__ == "__main__":
    try:
        poll_for_file("report.csv", directory="upload", interval=5, timeout=10)
    except TimeoutError as e:
        print(f"❌ {e}")