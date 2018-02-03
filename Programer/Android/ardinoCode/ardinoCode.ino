
void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  digitalWrite(13, LOW);
  // initialize the LED pins:
  for (int thisPin = 2; thisPin < 7; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }
}

void loop() {
  // read the sensor:
  if (Serial.available() > 0) {
    int inByte = Serial.read();
    // do something different depending on the character received.
    // The switch statement expects single number values for each case; in this
    // example, though, you're using single quotes to tell the controller to get
    // the ASCII value for the character. For example 'a' = 97, 'b' = 98,
    // and so forth:

    switch (inByte) {
     case 'i':
        digitalWrite(2, LOW);
        break;
     case 'I':
        digitalWrite(2, HIGH);
        break;
     case 'k':
        digitalWrite(4, LOW);
        break;
     case 'K':
        digitalWrite(4, HIGH);
        break;
     case 'j':
        digitalWrite(3, LOW);
        break;
     case 'J':
        digitalWrite(3, HIGH);
        break;
     case 'm':
        digitalWrite(6, LOW);
        break;
     case 'M':
        digitalWrite(6, HIGH);
        break;
     case 'l':
        digitalWrite(5, LOW);
        break;
     case 'L':
        digitalWrite(5, HIGH);
        break;
     case 'o':
        digitalWrite(8, LOW);
        break;
     case 'O':
        digitalWrite(8, HIGH);
        break;
     case 'n':
        digitalWrite(7, LOW);
        break;
     case 'N':
        digitalWrite(7, HIGH);
        break;
     case 'q':
        digitalWrite(10, LOW);
        break;
     case 'Q':
        digitalWrite(10, HIGH);
        break;
     case 'p':
        digitalWrite(9, LOW);
        break;
     case 'P':
        digitalWrite(9, HIGH);
        break;
     case 's':
        digitalWrite(12, LOW);
        break;
     case 'S':
        digitalWrite(12, HIGH);
        break;
     case 'r':
        digitalWrite(11, LOW);
        break;
     case 'R':
        digitalWrite(11, HIGH);
        break;
     case 'z':
        digitalWrite(13, LOW);
        break;
     case 'Z':
        digitalWrite(13, HIGH);
        break;
      
      default:
        // turn all the LEDs off:
        for (int thisPin = 1; thisPin < 13; thisPin++) {
          digitalWrite(thisPin, LOW);
        }
    }
  }
}
