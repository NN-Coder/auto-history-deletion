import os
import sqlite3
import time
import shutil

CHROME_HISTORY_DB = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/History')

def clear_chrome_history():
    os.system("pkill -f 'Google Chrome'")  
    time.sleep(2)  

    backup_path = CHROME_HISTORY_DB + ".backup"
    shutil.copy2(CHROME_HISTORY_DB, backup_path)

    try:
        conn = sqlite3.connect(CHROME_HISTORY_DB)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM urls")
        conn.commit()
        conn.close()

        print("✅ Chrome history cleared successfully!")

    except Exception as e:
        print(f"❌ Error clearing history: {e}")

if __name__ == "__main__":
    clear_chrome_history()
