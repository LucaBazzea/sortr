import os
import datetime


path = r"test.txt"

m_time = os.path.getmtime(path)

print(f"Modification Time: {m_time}")