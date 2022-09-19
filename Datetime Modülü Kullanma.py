from datetime import datetime
import os
os.getenv("Home")
print(os.stat("Badem.txt"))
print(datetime.fromtimestamp(os.stat("Badem.txt").st_atime))
