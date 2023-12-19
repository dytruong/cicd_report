from pathlib import Path
from datetime import datetime


def record_log(log_str, log_name, log_path, show_log=True):
    try:
        Path(log_path).mkdir(parents=True, exist_ok=True)
        Path(f"{log_path}/{log_name}").touch(exist_ok=True)
        timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        log_frame = f"[{timestamp} UTC +7] - {log_str}\n"
        # show log to the screen
        if show_log:
            print(log_str)

        with open(f"{log_path}/{log_name}", "a") as file:
            file.write(log_frame)
    except PermissionError as e:
        print(f"Error: {e} - Unable to write to the file.")
