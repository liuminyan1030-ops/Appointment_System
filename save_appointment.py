
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
