# Starting Out
I've been loving the terminal these days - been looking into code using the `cat` keyword in the terminal instead of opening up the IDE. 
I also use `touch` to create new files (also learned that we can just use the `nano` keyword)
I'm trying to build this mini project by only using the terminal, commands, command-line tools (that are not Claude code)
The most AI I will use is for guidance (perplexity chat bot to guide me in the right direction)

# Goal
The goal is to learn more about the lower-level linux command operations, how the process management is done, and how I can create tools that trigger these advanced terminal commands!


# Framework Choice
* using CustomTkinter (Python)
* built on top of Tkinter, so skill transfers over

# Day 1: Understanding the Core: `psutil`
`psutil` = a Python library that wraps OS-level process APIs into clean Python objects  
```
import psutil

for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'terminal', 'create_time']):
	print(proc.info)
```

`terminal` = session / console handle; zombie processes don't have an associated terminal => `None`

`create_time` = when the process staretd (useful when flagging old ones)

### Zombie Detection Logic
```
def is_zombie(proc):
	try:
		cmd = ' '.join(proc.info['cmdline'] or [])
		is_nextjs = 'next' in cmd or 'next-server' in cmd
		is_detached = proc.info['terminal'] is None
		return is_nextjs and is_detached
	# processes can die between the moment we list & when we read
	# to avoid race condition, we need try except in systems programming
	except (psutil.NoSuchProcess, psutil.AccessDenied):
		return False
```

# Day 2: Understanding CustomTkinter Layout System
CustomTkinter operates kind of similar to CSS Flexbox but more explicit



