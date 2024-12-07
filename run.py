import time
import signal
import sys
from main import app

# Định nghĩa timeout
def timeout_handler(signum, frame):
    print("Timeout reached, stopping script...")
    sys.exit(1)

# Thiết lập timeout 3 giây
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(3)  # Chạy trong 3 giây

# Chạy ứng dụng Flask
try:
    app.run(debug=True)
except KeyboardInterrupt:
    pass
finally:
    signal.alarm(0)  # Hủy bỏ alarm sau khi ứng dụng kết thúc
