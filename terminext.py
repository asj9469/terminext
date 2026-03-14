import psutil

def is_zombie(proc):
	try:
		cmd = ' '.join(proc.info['cmdline'] or [])
		is_nextjs = 'next' in cmd or 'next-server' in cmd
		is_detached = proc.info['terminal'] is None
		return is_nextjs and is_detached
	except (psutil.NoSuchProcess, psutil.AccessDenied):
		return False

for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'terminal', 'create_time']):
	print(proc.info)

