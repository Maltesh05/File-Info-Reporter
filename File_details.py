import sys
import os
import time

total_size = 0
dir_path = input("Enter the directory path: ")

#To display last modified date/time
def last_modified_fileinfo(modified_date):
    # Extract year, month and day from the date
    year = str(modified_date[0])
    month = modified_date[1]
    day = modified_date[2]
    # Extract hour, minute, second
    hour = modified_date[3]
    minute = modified_date[4]
    second = modified_date[5]
    # Year
    strYear = str((year)[0:])
    # Month
    if (month <= 9):
        strMonth = '0' + str(month)
    else:
        strMonth = str(month)
    # Date
    if (day <= 9):
        strDay = '0' + str(day)
    else:
        strDay = str(day)
    return (strYear + "-" + strMonth + "-" + strDay + " " + str(hour) + ":" + str(minute) + ":" + str(second))


#To get size of files in current directory
def filesize_readableformat(total_size):

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if total_size < 1024.0:
            return "%3.1f %s" % (total_size, x)
        total_size = (total_size/1024.0)

#To get size of current directory
def get_size(dir_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += (os.path.getsize(fp)/1024.0)
    return total_size


print('File Name', " "*(17), '|','File Type','|','Modified Date', " "*(6),'|','Size in bytes', " "*(2),'|','Readable Size')

for path, dirs, files in os.walk(dir_path):
    for name in files:
        fp = os.path.join(path,name)
        total_size = os.path.getsize(fp)
        file_stat = os.stat(dir_path)
        modified_date = time.localtime(file_stat.st_mtime)
        file_name = os.path.join(name)
        file_name1 = os.path.splitext(file_name)[0]
        file_type = os.path.splitext(file_name)[1]

        modified_date_printable = last_modified_fileinfo(modified_date)
        size_readable = filesize_readableformat(total_size)

        print(file_name1, " "*(26-len(file_name1)), '|', file_type, " "*(len(file_type)), '|', modified_date_printable, " "*(8-len(modified_date_printable)), '|', total_size, " "*(13-len(str(total_size))), '|', size_readable)

print('Total Directory size: ',get_size(dir_path))