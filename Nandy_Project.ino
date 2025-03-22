#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // Set the LCD address to 0x27 for a 16 chars and 2 line display
const int ledPin = 13; // LED connected to digital pin 13

void setup() {
  Serial.begin(9600);
  lcd.init();                       
  lcd.backlight();  
  lcd.setCursor(1, 0);
  lcd.print("System Ready..");

  pinMode(ledPin, OUTPUT); 
}

void loop() {
  if (Serial.available() > 0) {
    char incomingByte = Serial.read();
    if (incomingByte == '1') {
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Alert! Drowsiness");
      lcd.setCursor(3, 1);
      lcd.print("Detected..");
      digitalWrite(ledPin, HIGH);
      delay(50);
    } else if (incomingByte == '0') {
      lcd.clear();
      lcd.setCursor(2, 0);
      lcd.print("All is well!");
      digitalWrite(ledPin, LOW);
      delay(50);
    }
  }
}
