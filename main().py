
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
