'''
此版本有待优化
'''

import platform
import wmi
cpuinfo = wmi.WMI()
import time

def deadloop():
	i = 0 
	while True:
		i += 1
		for cpu in cpuinfo.Win32_Processor():
            if int(cpu.LoadPercentage) > 50:
				time.sleep(0.1)
	pass
	
deadloop()