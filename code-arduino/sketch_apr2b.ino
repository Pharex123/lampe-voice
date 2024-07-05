#define RELAY_PIN 5 // Définir la broche de relais

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW); // Éteindre la lampe au démarrage
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(RELAY_PIN, HIGH); // Allumer la lampe
    } else if (command == '0') {
      digitalWrite(RELAY_PIN, LOW); // Éteindre la lampe
    }
  }
}
