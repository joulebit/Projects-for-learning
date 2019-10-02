  /*
  Button
 
 Turns on and off a light emitting diode(LED) connected to digital  
 pin 13, when pressing a pushbutton attached to pin 2. 
 
 
 The circuit:
 * LED attached from pin 13 to ground 
 * pushbutton attached to pin 2 from +5V
 * 10K resistor attached to pin 2 from ground
 */

const int buttonPin = 2;     // the number of the pushbutton pin
const int ledShort =  13;      // the number of the LED pin for short signal
const int ledLong =  10;      // the number of the LED pin for long signal
const int ledPause = 7;       // the number of the LED pin for pause signal
const int ledPauseWord = 4;
const int t = 300;           // the base konstant for milliseconds of one intervall
const int j = 10;            // anti-jitter constant to not update button status too fast

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int ledStateShort = LOW;          // State of LED.
int ledStateLong = LOW; 
int ledStatePause = LOW;
int ledStatePauseWord = LOW;
int prevoiusButtonState = LOW; // State of button at previous read. 
int ms_count = 0;            // variable for keeping track of how long a state has been active

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledShort, OUTPUT);    
  pinMode(ledLong, OUTPUT);     
  pinMode(ledPause, OUTPUT);
  pinMode(ledPauseWord,OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);  
  // connect to band 9600   
  Serial.begin(9600);
}

void loop(){
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);
  
  // check if the pushbutton is not being pressed.
  // if it was previously pressed, use the timer to figure out..
  // ..if the press was long or short, and reset the timer
  if (buttonState == LOW) {     
    ledStateShort = LOW;           // if button is not pressed, ledtstate goes low
    ledStateLong = LOW;
    
    if (prevoiusButtonState == HIGH){
      if(ms_count >= 3*t){      // Long presses are longer than 3 times time constant, just around a second or longer
        Serial.print(1);        // Serial.println(1) causes problems in the python program because of newline \n
      }
      else{
        Serial.print(0);
      }

      ms_count = 0;             // reset timer to controll how long the next pause is
    }

    if(ms_count >= 10*t){
      ledStatePause = LOW;
      ledStatePauseWord = HIGH;
    }
    else if(ms_count >= 3*t){
      ledStatePause = HIGH;
    }
  }
  
  // check if the pushbutton is being pressed.
  // if it was previously not pressed, use the timer to figure out..
  // ..if the pause was long or medium or short, and reset the timer
  else if (buttonState == HIGH){
    
    ledStatePause = LOW;
    ledStatePauseWord = LOW;
    
    if (prevoiusButtonState == LOW){    // Only updates counter and sends a signal if we change state on the button, and not when we hold it in
      if(ms_count >= 10*t){           // Long pauses for between words are considered more than 3 seconds (10*T)
        Serial.print(3);    
      }

      else if(ms_count >= 3*t){      //Medium long pause for between letters
        Serial.print(2);             
      }

                                     // Smaller pauses are considered as pauses between dots and slashes in the same letter, so no signal is sent
      
      ms_count = 0;                  // Reset the timer
  }

    if(ms_count >= 3*t){             // Update yellow light on and red light off when we get a long press
      ledStateLong = HIGH;
      ledStateShort = LOW;
    }

    else{                            // Else have red light while button is pressed
      ledStateShort = HIGH;
    }
  
  }
  
  digitalWrite(ledLong, ledStateLong);    // Update LED status to match the button status
  digitalWrite(ledShort, ledStateShort); 
  digitalWrite(ledPause, ledStatePause); 
  digitalWrite(ledPauseWord, ledStatePauseWord); 
  prevoiusButtonState = buttonState; // update previous button state constant
  ms_count += j;                     // tick the timer up as much as the delay is
  delay(j);                          // delay with anti-debounce constant to reduce debounce

  // Må jeg ha med flere lys for å blinke for lang/kort trykk og pause?
}
