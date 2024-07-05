import serial
import speech_recognition as sr

# Définir le port série pour la communication avec Arduino
ser = serial.Serial('COM6', 9600)  # Remplacer 'COMX' par le bon port série

# Fonction pour reconnaître la commande vocale
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dites 'allumer' ou 'éteindre' pour contrôler la lampe :")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='fr-FR')
        return text.lower()
    except sr.UnknownValueError:
        print("Je n'ai pas compris ce que vous avez dit.")
        return ""
    except sr.RequestError as e:
        print("Erreur lors de la requête vers le service Google Speech Recognition; {0}".format(e))
        return ""

# Fonction pour envoyer la commande à Arduino
def send_command(command):
    if command == "allumer":
        ser.write(b'1') # Envoyer '1' à Arduino pour allumer la lampe
    elif command == "éteindre":
        ser.write(b'0') # Envoyer '0' à Arduino pour éteindre la lampe
    else:
        print("Commande non reconnue.")

# Boucle principale
while True:
    command = recognize_speech()
    if command:
        send_command(command)
