#! /usr/bin/env python

# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import drivers



# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()

# Main body of code
           
            
            
if __name__ == "__main__":
    try:
            # Remember that your sentences can only be 16 characters long!
           statement = "Escribe lo que quieras imprimir: "
           display.show_lines(statement,len(statement))
           message=input(statement)
           display.lcd_clear()
           long = len(message)
           display.show_lines(message,long)
           
            # Give time for the message to be read
    except KeyboardInterrupt:
        # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        display.lcd_clear()
        
    

