import subprocess
import os
import sys
import threading
import time


def run_script(script_path):
    """Runs a Python script and checks for errors."""
    try:
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return_code = process.returncode

        if return_code == 0:
            print(f"Script '{script_path}' executed successfully.")
            if stdout:
                print(f"Standard Output of '{script_path}':\n{stdout.decode(sys.getdefaultencoding(), errors='ignore')}") # Decode output
        else:
            print(f"Script '{script_path}' failed with return code {return_code}.")
            if stderr:
                print(f"Standard Error of '{script_path}':\n{stderr.decode(sys.getdefaultencoding(), errors='ignore')}") # Decode error

    except FileNotFoundError:
        print(f"Error: Script '{script_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred while running '{script_path}': {e}")
    return return_code


if __name__ == "__main__":
    script1_path = r'main-1.py'
    script2_path = r'main-2.py'
    script3_path = r'main-3.py'
    script4_path = r'main-4.py'
    script5_path = r'main-5.py'


    # Run scripts concurrently using threads
    thread1 = threading.Thread(target=run_script, args=(script1_path,))
    thread2 = threading.Thread(target=run_script, args=(script2_path,))
    thread3 = threading.Thread(target=run_script, args=(script3_path,))
    thread4 = threading.Thread(target=run_script, args=(script4_path,))
    thread5 = threading.Thread(target=run_script, args=(script5_path,))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    print("Both scripts have finished (or encountered errors).")


