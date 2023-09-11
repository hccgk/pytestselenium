"""
Created by HE on 2023/9/11.
该方法替换header里面的时间戳
This is a description of the file.
"""

import time

timestamp = int(time.time())
timestamp_str = str(timestamp)
print(timestamp_str)
new_string = f"expire_in={timestamp};"

