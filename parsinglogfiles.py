
''''
write a python fxn to parse a log file with entries in the format timestamp: message.
extract the timestamps and messages into separate sheet
'''
def parsinglogfiles(logfile):
    timestamps = []
    messages = []
    
    with open (logfile, "r") as f:
        for line in f:
            print(line)
            a= print(f.read().strip().split(": ",1))
            print(type(a))
    #     if len(a)==2:
    #         timestamp, message = a
    #         timestamps.append(timestamp)
    #         messages.append(message)
    #     else:
    #         print(f"skipping line: {line}")
    # return timestamps, messages


parsinglogfiles("metlogs.txt")

