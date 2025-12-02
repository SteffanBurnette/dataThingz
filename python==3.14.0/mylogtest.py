import logging

logging.basicConfig(
    level = logging.DEBUG,  
    format="{asctime} - {levelname} - {message}", #Outputs the timestamp, log name and message
    style="{",  #Uses the {} style over the default () style
    datefmt="%Y-%m-%d %H:%M", #used to get the current timestamp
    filename = "mylogfile.log", # Will store the log messages in the mylogfile.log file
    filemode = "w", # Will interact with the file in write mode
    )

##Configuring the basic logging settimgs
logging.debug("This is a debugging log message")
logging.info("This is an info log message")
logging.warning("This is a warning")
logging.error("This is an error log message")
logging.critical("This is a critical log message")