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

