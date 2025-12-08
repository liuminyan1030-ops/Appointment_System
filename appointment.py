class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        # hidden properties
        self.__client_name = ""
        self.__client_phone = ""
        # 0 = Available
        self.__appt_type = 0            
        self.__day_of_week = day_of_week
        self.__start_time_hour = int(start_time_hour)

    # ======================
    # Getter Methods
    # ======================
    def get_client_name(self):
        return self.__client_name

    def get_client_phone(self):
        return self.__client_phone

    def get_appt_type(self):
        return self.__appt_type

    def get_day_of_week(self):
        return self.__day_of_week

    def get_start_time_hour(self):
        return self.__start_time_hour

    # ======================
    # Setter Methods
    # ======================
    def set_client_name(self, new_name):
        self.__client_name = new_name

    def set_client_phone(self, new_phone):
        self.__client_phone = new_phone

    def set_appt_type(self, new_type):
        self.__appt_type = int(new_type)

    # ======================
    # Appointment Type Description
    # ======================
    def get_appt_type_desc(self):
        if self.__appt_type == 0:
            return "Available"
        elif self.__appt_type == 1:
            return "Mens Cut"
        elif self.__appt_type == 2:
            return "Ladies Cut"
        elif self.__appt_type == 3:
            return "Mens Colouring"
        elif self.__appt_type == 4:
            return "Ladies Colouring"
        else:
            return "Unknown"

    # ======================
    # End time = start time + 1 hour
    # ======================
    def get_end_time_hour(self):
        return self.__start_time_hour + 1

    # ======================
    # Schedule an appointment
    # ======================
    def schedule(self, client_name, client_phone, appt_type):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = int(appt_type)

    # ======================
    # Cancel an appointment
    # ======================
    def cancel(self):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0

    # ======================
    # Format record for CSV file
    # ======================
    def format_record(self):
        return f"{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour}"

    # ======================
    # String representation for printing appointment
    # ======================
    def __str__(self):
        start = f"{self.__start_time_hour:02d}:00"
        end = f"{self.get_end_time_hour():02d}:00"
        return f"{self.__client_name:<15} {self.__client_phone:<15} {self.__day_of_week:<10} {start} - {end}   {self.get_appt_type_desc()}"
