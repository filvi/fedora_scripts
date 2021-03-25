import time
def progress_bar(length):
    total_len = length + 2
    for i in range(length):
            print("[" + i*"=" + (length - 1  - i)*" " + "]" , end="\r")
            time.sleep(0.2)
    print(" "*total_len, end="\r")
    print("Done")
progress_bar(20)