import os
from appointment import Appointment
# ================================================================
# create_weekly_calendar()
# ================================================================
def create_weekly_calendar(appt_list):
  appt_list.clear()
  MIN_AVAILABLE_HOUR=9
  MAX_AVAILABLE_HOUR=16
  days_order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  for day in days_order:
    for hour in range(MIN_AVAILABLE_HOUR,MAX_AVAILABLE_HOUR+1):
      appt=Appointment(day,hour)
      appt_list.append(appt)
# ==========================================================
# load_scheduled_appointments(appt_list)
# ==========================================================
def load_scheduled_appointments(appt_list):
  filename=input("Enter appointment filename: ")
  while not os.path.exists(filename):
    print("File not found.")
    filename=input("Re-enter appointment filename: ")
  file=open(filename,"r")
  count=0
  for line in file:
    line=line.strip()
    if line=="":
      continue
    parts=line.split(",")
    if len(parts)!=5:
      continue
    client_name=parts[0]
    client_phone=parts[1]
    appt_type=int(parts[2])
    day_of_week=parts[3]
    start_time_hour=int(parts[4])
    appt=find_appointment_by_time(appt_list,day_of_week,start_time_hour)
    if appt is not None:
      appt.schedule(client_name,client_phone,appt_type)
      count +=1
  file.close()
  return count

# ==========================================================
# print_menu()
# ==========================================================
def print_menu():
  print("="*40)
  print("Hair Salon Appointment Manager")
  print("="*40)
  print("1) Schedule an appointment")
  print("2) Find appointment by name")
  print("3) Print calendar for a specific day")
  print("4) Cancel an appointment")
  print("5) Change an appointment")
  print("6) Calculate total fees for a day")
  print("7) Calculate total weekly fees")
  print("9) Exit the system")
  valid_choices = ["1", "2", "3", "4", "5", "6", "7", "9"]
  choice = input("Enter your selection: ")
  while choice not in valid_choices:
      print("Invalid option.")
      choice = input("Enter your selection: ")
  return choice
# ==========================================================
# find_appointment_by_time(appt_list, day, hour)
# ==========================================================
def find_appointment_by_time(appt_list,day_of_week,start_time_hour):
  if day_of_week=="":
    return None
  for appt in appt_list:
    if(appt.get_day_of_week().lower()==day_of_week.lower() and appt.get_start_time_hour()==int(start_time_hour)):
      return appt
  return None
# ==========================================================
# show_appointments_by_name(appt_list, name)
# ==========================================================
def show_appointments_by_name(appt_list,search_name):
  print(f"Appointments for {search_name}")
  print(f"{'Client Name':<15} {'Phone':<15} {'Day':<10} {'Start':<6} {'End':<6} {'Type'}")
  print("-" * 75)
  found=False
  for appt in appt_list:
    if search_name.lower() in appt.get_client_name().lower():
      print(appt)
      found=True
  if not found:
    print("No appointments found.")
# ==========================================================
# show_appointments_by_day(appt_list, day)
# ==========================================================
def show_appointments_by_day(appt_list,search_day):
  print(f"Appointments for {search_day.capitalize()}")
  print("")
  print(f"{'Client Name':<15} {'Phone':<15} {'Day':<10} {'Start':<6} {'End':<6} {'Type'}")
  print("-" * 65)
  found=False
  for appt in appt_list:
    if (search_day !="" and appt.get_day_of_week().lower()==search_day.lower()):
      print(appt)
      found=True
