import os
import subprocess
from datetime import datetime

def create_backup():

    backup_dir = "backups"

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    filename = (
        "backup_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".sql"
    )

    filepath = os.path.join(
        backup_dir,
        filename
    )

    command = [
        r"C:\xampp\mysql\bin\mysqldump.exe",
        "-u", "root",
        "-P", "3307",
        "-h", "localhost",
        "sentinelx_ai"
    ]

    with open(filepath, "w", encoding="utf-8") as f:
        result = subprocess.run(
            command,
            stdout=f
        )

    if result.returncode != 0:
        raise Exception("MySQL backup failed.")

    return filename