import os
import time

#查找并删除90天以前的日志文件
def print_old_logs(dir_path):
    current_time = time.time()
    thirty_days_ago = current_time - 90 * 24 * 60 * 60

    for root, dirs, files in os.walk(dir_path,onerror=None):
        for filename in files:
            if not filename.endswith('.log'):
                continue

            file_path = os.path.join(root, filename)
            file_modified_time = os.path.getmtime(file_path)

            if file_modified_time < thirty_days_ago:
                print(file_path)
                os.remove(file_path)

print_old_logs("/dir_path")