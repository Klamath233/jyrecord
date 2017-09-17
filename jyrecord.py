import subprocess as sp
import datetime as dt
import shutil
import time

# JY's room link
room_url = 'https://www.panda.tv/888888'

# Streamlink command's template to be filled in main loop
cmd_template = 'streamlink -o {} {} best'

# Retry timeout - 1, 2, 4, 8, 16, 32, 32, 32...
timeout = 1

filename = "temp.flv"

# Main loop
while True:

  # Get date time of now
  start_time = dt.datetime.now()
  start_time_str = start_time.strftime('%Y%m%d-%H%M%S')

  # Try to run the command
  result = sp.run(cmd_template.format(filename, room_url), shell=True)

  if result.returncode == 0 or result.returncode == 127:
    end_time = dt.datetime.now()
    end_time_str = end_time.strftime('%Y%m%d-%H%M%S')
    shutil.move(filename, 'JY-{}-{}.flv'.format(start_time_str, end_time_str))
    timeout = 1
  else:
    if timeout < 30:
      timeout = timeout * 2
  
  time.sleep(timeout)

    
  