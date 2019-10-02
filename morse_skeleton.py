import arduino_connect  # This is the key import so that you can access the serial port.

# Codes for the 5 signals sent to this level from the Arduino

_dot = 0
_dash = 1
_symbol_pause = 2
_word_pause = 3



# Morse Code Class
class mocoder():

    _morse_codes = {'01':'a','1000':'b','1010':'c','100':'d','0':'e','0010':'f','110':'g','0000':'h','00':'i','0111':'j',
               '101':'k','0100':'l','11':'m','10':'n','111':'o','0110':'p','1101':'q','010':'r','000':'s','1':'t',
               '001':'u','0001':'v','011':'w','1001':'x','1011':'y','1100':'z','01111':'1','00111':'2','00011':'3',
               '00001':'4','00000':'5','10000':'6','11000':'7','11100':'8','11110':'9','11111':'0'}

	# Connection is set up with sereial port from the helper class arduino_connect
    def __init__(self,sport=True): # sport = True?? -------------------------
        if sport:
            self.serial_port = arduino_connect.pc_connect()
        self.reset()

    def reset(self):
        self.current_message = ''
        self.current_word = ''
        self.current_symbol = ''

    # This should receive an integer in range 0-3 from the Arduino via a serial port
    def read_one_signal(self,port=None):    # hva gjør port?--------------
        connection = port if port else self.serial_port
        while True:
            # Reads the input from the arduino serial connection
            data = connection.readline()
            if data:
                return data
                
    # The signal returned by the serial port is one (sometimes 2) bytes, that represent characters of a string.  So,
    # a 2 looks like this: b'2', which is one byte whose integer value is the ascii code 50 (ord('2') = 50).  The use
    # of function 'int' on the string converts it automatically.   But, due to latencies, the signal sometimes
    # consists of 2 ascii codes, hence the little for loop to cycle through each byte of the signal.

    # kan jeg bruke komenteringen til skjelettet?-------------------------

    def decoding_loop(self):
        while True:
            s = self.read_one_signal(self.serial_port)
            
            # Used in cases when there is multiple bytes in one read
            for byte in s:
                self.process_signal(int(chr(byte)))
                
                
    # Add a dash or dot to the current symbol variable
    def update_current_symbol(self,signal):
        self.current_symbol += str(signal)
        
    #Add the finished symbol to current word and clear current symbol
    def handle_symbol_end(self): 
        self.char =  self._morse_codes.get(self.current_symbol)
        self.update_current_word(self.char)
        self.current_symbol = ''
    
    #Add letter to current word
    def update_current_word(self,letter):
        self.current_word += str(letter)
    
    #Print out when a word is finished and set current word to empty
    def handle_word_end(self):
        self.handle_symbol_end()
        print(self.current_word)
        self.current_word = ''
        
     
     # Assign the recieved signal to the correct action         
    def process_signal(self,sig):
        if((sig == 0) or (sig == 1)):
            self.update_current_symbol(sig)
        
        if(sig == 2):
            self.handle_symbol_end()
        
        if(sig == 3):
            self.handle_word_end()
        
        
    

    

    
''' To test if this is working, do the following in a Python command window:

> from morse_skeleton import *
> m = mocoder()
> m.decoding_loop()

If your Arduino is currently running and hooked up to the serial port, then this
simple decoding loop will print the raw signals that the Arduino sends to
the serial port.  Each time you press (or release) your morse-code device, a signal should
appear in your Python window. In Python, these signals typically look like this:
 b'5' or b'1' or b'3', etc.
'''

# hvorfor så mye self, hvor mange kommentarer trenger man/ hvor basic ting må man forklare