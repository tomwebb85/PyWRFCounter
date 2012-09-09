import numpy as np


def wrftime(logFileName, cpuNum):
	"""
	Returns the time taken for WRF to execute in seconds
	
	@param logFileName (str): The name of the logfile WRF has redirected
	its output to via wrf.exe > wrf.log
	@param cpuNum (int): The number of CPU's used 
	
	@return: sumtime (float): The number of seconds taken for execution
	
	@example: sumtime=wrftime('wrf.log',8)
	"""
 	f=open(logFileName,'r')
 	phrase = 'Timing for main:'
 	sumtime=float(0.0)
 	with f as myFile:
		for num, line in enumerate(myFile, 1):
        		if phrase in line:
            			test=line.split()
	    			sumtime=float(sumtime)+float(test[8])
	sumtime=sumtime/cpuNum 
	return sumtime	    
	f.close()


