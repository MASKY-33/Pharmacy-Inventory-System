# P.S.) This System took me 30min or so. I wanted to test if I understood the architecture (datastreaming), And yes, I do.


medicine_stock = {
    "paracetamol" : "cabinet 1",
    "ibuprofen" : "cabinet 2",
    "amoxicilline" : "cabinet 3"
}

def night_pharmacy(medicine):

    # Check (if) medicine is in stock
    if medicine in medicine_stock:

        # cabinet check, in which cabinet the medicine is in
        cabinet_check = medicine_stock[medicine]
        return f"{medicine} sits inside {cabinet_check}"
    else:
        return f"{medicine} not yet in stock!"
        

# Continue looping headprogram for searching mecicine and in which cabinet they sit in
while True:
    search_medicine = input("Give in the name of the medicine, (or type 'stop' to stop): ").lower()

    # Checking (if) person types "stop", (if) so, end the System by (break)
    if search_medicine == "stop":
        print("Bye, see you next time!")
        break
    
    # Call the function to give the asked medicine
    system_result = night_pharmacy(search_medicine)
    print(system_result)
