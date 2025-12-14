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
