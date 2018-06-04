import time

timeout=time.time()+3
while time.time()<timeout:
    print("yo")
    time.sleep(0.3)

print("gedaan")

