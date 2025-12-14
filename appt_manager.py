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
# ==========================================================

# change_appointment_by_day_time(appt_list)

# ==========================================================

def change_appointment_by_day_time(appt_list):

  print("Change an appointment for:")

  day=input("What day: ")

  start_time_hour=input("Enter start hour (24 hour clock): ")

  if not start_time_hour.isdigit():

    print("Invalid hour. Please try again.")

    return

  hour=int(start_time_hour)

  old_appt=find_appointment_by_time(appt_list,day,hour)

  if old_appt is None:

    print("Sorry that time slot is not in the weekly calendar!")

    return

  if old_appt.get_appt_type()==0:

    print("That time slot isn't booked and doesn't need to be changed.")

    return

  old_name = old_appt.get_client_name()

  old_phone = old_appt.get_client_phone()

  old_type = old_appt.get_appt_type()

  new_day=input("Enter new day: ")

  new_start_hour=input("Enter start hour (24 hour clock): ")

  if not new_start_hour.isdigit():

     print("Invalid new start hour.")

     return

  new_hour=int(new_start_hour)

  new_appt=find_appointment_by_time(appt_list,new_day,new_hour)

  if new_appt is None:

     print("Sorry that time slot is not in the weekly calendar!")

     return

  if new_appt.get_appt_type()!=0:

     print("The new time slot is already booked.")

     return

  new_appt.schedule(old_name,old_phone,old_type)

  old_appt.cancel()

  print(f"Appointment for {old_name} has been changed to:")

  print(f"Day = {new_day.capitalize()}")

  print(f"Time = {new_hour}")

# ==========================================================

# calculate_fees_per_day(appt_list)

# ==========================================================

def calculate_fees_per_day(appt_list):

  print("Fees calculate per day....")

  day=input("What day:")

  valid = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

  if day.capitalize() not in valid:

      print(f"{day} is invalid day or salon is closed.")

      return

  total=0

  fee_map = {1: 40, 2: 60, 3: 40, 4: 80}

  for appt in appt_list:

    if appt.get_day_of_week().lower()==day.lower():

      t=appt.get_appt_type()

      if t in fee_map:

        total +=fee_map[t]

  print(f"Total fees for {day.capitalize()} is ${total}")

# ==========================================================

# calculate_weekly_fees(appt_list)

# ==========================================================

def calculate_weekly_fees(appt_list):

  total=0

  fee_map = {1: 40, 2: 60, 3: 40, 4: 80}

  for appt in appt_list:

    t=appt.get_appt_type()

    if t in fee_map:

      total +=fee_map[t]

  print(f"Total weekly fees is ${total}")
# ==========================================================
# save_scheduled_appointments(appt_list)
# ==========================================================
def save_scheduled_appointments(appt_list):
  filename=input("Enter appointment filename: ")
  while True:
    if os.path.exists(filename):
      answer=input("File already exists.Do you want to overwrite it(Y/N)? ")
      while answer.upper() not in ["Y","N"]:
        answer=input("File already exists.Do you want to overwrite it(Y/N)? ")
      if answer.upper()=="N":
        filename = input("Enter appointment filename: ")
        continue
    break
  file=open(filename,"w")
  count=0
  for appt in appt_list:
    if appt.get_appt_type()!=0:
      file.write(appt.format_record()+"\n")
      count +=1
  file.close()
  return count


# ==========================================================
# main()
# ==========================================================
def main():
   print("Starting the Appointment Manager System")
   appt_list=[]
   create_weekly_calendar(appt_list)
   print("Weekly calendar created")
   choice = input("Would you like to load previously scheduled appointments from a file (Y/N)? ")
   if choice.upper()=="Y":
      loaded=load_scheduled_appointments(appt_list)
      print(f"{loaded}  previously scheduled appointments have been loaded.")

   selection=print_menu()
   while selection !="9":
      if selection=="1":
          print("\n** Schedule an appointment **")
          day = input("What day: ")
          hour = int(input("Enter start hour (24 hour clock): "))

          appt = find_appointment_by_time(appt_list, day, hour)
          if appt is None:
                  print("Sorry that time slot is not in the weekly calendar!")
          elif appt.get_appt_type() != 0:
                  print("Sorry that time slot is booked already!")

          else:
                  name = input("Client Name: ")
                  phone = input("Client Phone: ")
                  print("Appointment types")
                  print("1: Mens Cut $40, 2: Ladies Cut $60, 3: Mens Colouring $40, 4: Ladies Colouring $80")

                  appt_type=input("Type of Appointment: ")
                  appt.schedule(name,phone,appt_type)
                  print(f"OK, {name}'s appointment is scheduled!")

      elif selection=="2":
           print("\n** Find appointment by name **")
           name=input("Enter Client Name: ")
           show_appointments_by_name(appt_list,name)
      elif selection=="3":
           print("\n** Print calendar for a specific day **")
           day=input("Enter day of week:")
           print("")
           show_appointments_by_day(appt_list,day)
      elif selection=="4":
           print("\n** Cancel an appointment **")
           day = input("What day: ")
           hour = int(input("Enter start hour (24 hour clock): "))
           appt=find_appointment_by_time(appt_list,day,hour)
           if appt is None:
              print("Sorry that time slot is not in the weekly calendar!")
           elif appt.get_appt_type()==0:
              print("There is no appointment booked at that time.")
           else:
              client_name = appt.get_client_name()
              start = f"{appt.get_start_time_hour():02d}:00"
              end = f"{appt.get_end_time_hour():02d}:00"
              day_formatted = day.capitalize()
              appt.cancel()
              print(f"Appointment: {day_formatted} {start} - {end} for {client_name} has been cancelled!")
      elif selection=="5":
           change_appointment_by_day_time(appt_list)
      elif selection=="6":
           calculate_fees_per_day(appt_list)
      elif selection=="7":
           calculate_weekly_fees(appt_list)
      selection=print_menu()
   print("\n** Exit the system **")
   save = input("Would you like to save all scheduled appointments to a file (Y/N)? ")
   if save.upper()=="Y":
     saved=save_scheduled_appointments(appt_list)
     print(f"{saved} scheduled appointments have been successfully saved")
   print("Good Bye!")

if __name__ == "__main__":
    main()
