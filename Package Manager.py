#!/usr/bin/env python
# coding: utf-8

# # Package Manager

# In[3]:


# Import necessary modules
from datetime import datetime
import pytz

# Define the UTC and IST time zones
utc = pytz.utc
ist = pytz.timezone("Asia/Kolkata")

# Get the current time in UTC
now = datetime.now(tz=utc)

# Convert the UTC time to IST
ist_now = now.astimezone(ist)

# Print the time zone information and the converted time
print("Time zone for IST:", ist)
print("Current time in IST:", ist_now)

