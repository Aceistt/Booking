import time
import csv

# Functie om de booking ID te valideren
def validate_booking_id(booking_id):
    with open('bookings_DX28.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['booking_id'] == str(booking_id):
                return row
    return None

# Functie om ingecheckte ID's op te slaan in een bestand
def save_checked_in_ids(checked_in_ids):
    with open('checked_in.txt', 'w') as file:
        for id in checked_in_ids:
            file.write(f"{id}\n")

def main():
    checked_in_ids = []  # Lijst om ingecheckte IDs op te slaan
    print("Welkom bij de incheckbalie!\n")
    
    # Vluchtgegevens
    flight_id = "DX28"
    check_in_closes = "20:01:59"
    current_time = time.strftime("%H:%M:%S")
    
    # Start scherm
    print(f"Inchecken voor vlucht: {flight_id}")
    print(f"Inchecken sluit om: {check_in_closes}")
    print(f"Het is nu: {current_time}")
    
    input("Druk op Enter om door te gaan...\n")
    
    # Start inchecken loop
    while True:
        booking_id_input = input("Booking ID: ")
        booking_data = validate_booking_id(booking_id_input)
        
        if booking_data is not None:
            print("\nControleer gegevens:")
            print(f"Vlucht: {flight_id}")
            print(f"Booking ID: {booking_data['booking_id']}")
            print(f"Passagier: {booking_data['name']}")
            print(f"Geslacht: {booking_data['gender']}")
            
            inchecken = input("Inchecken? ja/nee: ").strip().lower()
            if inchecken == 'ja':
                checked_in_ids.append(booking_data['booking_id'])
                print(f"\nPassagier {booking_data['name']} is ingecheckt voor vlucht {flight_id}!\n")
            elif inchecken == 'nee':
                print("Check-In geloten, houdoe!")
                save_checked_in_ids(checked_in_ids)  # Sla alle ingecheckte ID's op in een bestand
                break
            else:
                print("Ongeldige keuze. Typ 'ja' of 'nee'.")
        else:
            print("Ongeldige Booking ID. Probeer opnieuw.")
        
        # Vraag of we verder moeten gaan
        next_action = input("Druk op Enter om door te gaan of typ 'X' om af te sluiten: ").strip().lower()
        if next_action == 'x':
            print("Check-In geloten, houdoe!")
            save_checked_in_ids(checked_in_ids)  # Sla alle ingecheckte ID's op in een bestand
            break

if __name__ == "__main__":
    main()
