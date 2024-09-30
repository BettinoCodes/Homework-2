# Open the file in read mode
# with open("payroll", "r") as file:
#     payroll_line = file.readline()
#     print(payroll_line)
from datetime import datetime

working_times = []
dict_data = {}
active_number = ''
total_pay = 0

rate_before_9 = 0
rate_9_to_midnight = 5
rate_after_midnight = 10


time_9_pm = datetime.strptime("21:00", "%H:%M")
time_midnight = datetime.strptime("00:00", "%H:%M")
time_6_am = datetime.strptime("06:00", "%H:%M")

time_6am = "6:00 AM"
time_6am_24hr = datetime.strptime(time_6am, "%I:%M %p").strftime("%H:%M")
print("6 AM in 24-hour format:", time_6am_24hr)  # Output: 06:00

# 6 PM
time_6pm = "6:00 PM"
time_6pm_24hr = datetime.strptime(time_6pm, "%I:%M %p").strftime("%H:%M")
print("6 PM in 24-hour format:", time_6pm_24hr)

with open("payroll", "r") as file:
    while True:
        line = file.readline()
        if len(line) == 5:
            active_number = line.strip()

        if len(line) == 5 and line not in dict_data and line != active_number:
            dict_data[line.strip()] = []
        else:
            if len(line) > 2:
                dict_data[active_number].append(line.strip().split())
                times_working =  line.strip().split()
                print(f"TW {times_working}")
                start = times_working[0]
                end = times_working[1]

                if len(start) < 5:
                    start = "0" + start
                if len(end) < 5:
                    end = "0" + end

                first_two_start = f"{start[0]}{start[1]}"
                first_two_end= f"{end[0]}{end[1]}"

                print(f"first two start time: {first_two_start}")
                print(f"first two end time: {first_two_end}")

                if int(first_two_start) < 6:
                    start = start + " AM"
                else:
                    start = start + " PM"
                if int(first_two_end) < 6:
                    end = end + " AM"
                else:
                    end = end + " PM"

                starttime_24hr = datetime.strptime(start, "%I:%M %p").strftime("%H:%M")
                endtime_24hr = datetime.strptime(end, "%I:%M %p").strftime("%H:%M")

                start = datetime.strptime(starttime_24hr, "%H:%M")
                end = datetime.strptime(endtime_24hr, "%H:%M")

                print(f"start time: {starttime_24hr}")
                print(f"end time: {endtime_24hr}")

                #Assume all times are between 6:00 PM a
                # if end < start:
                #     end = datetime.strptime(f"{int(end.split(':')[0]) + 24}:{end.split(':')[1]}", "%H:%M")
                total_pay = 0
                if start < time_9_pm:
                    if end <= time_9_pm:
                        total_pay += (end - start).seconds / 3600 * rate_before_9
                    else:
                        total_pay += (time_9_pm - start).seconds / 3600 * rate_before_9
                        start = time_9_pm

                if start < time_midnight:
                    if end <= time_midnight:
                        total_pay += (end - start).seconds / 3600 * rate_9_to_midnight
                    else:
                        total_pay += (time_midnight - start).seconds / 3600 * rate_9_to_midnight
                        start = time_midnight

                if start >= time_midnight and start <= time_6_am:
                    total_pay += (end - start).seconds / 3600 * rate_after_midnight

                print(total_pay)
        
        print(f"active: {active_number}")
        if not line:
            print("file is done")
            break  # End of file reached

        print(f"line: {line.strip()}")
        if (len(line) > 5):
            line = line.strip().split()
            working_times.append(line)
            
                


# for i in working_times:
#     print(i)

print(dict_data)
# print(working_times)
# filename = "payroll"
# reader = line_reader(filename)# Initialize the reader (generator)
# reader_time = line_reader(filename)


# try:
#     while True:
#         empty = 0
#         user_input = input("Press Enter to read the next line, or type 'exit' to stop: ")
#         if user_input.lower() == 'exit':
#             break
#         print(next(reader))
#         print(next(reader_time))# Reads and prints the next line
# except StopIteration:
#     print("End of file reached.")
