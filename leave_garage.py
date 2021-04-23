def leaveGarage(self): #Felix's Baby

        #Make sure their ticket is paid, if it is display "thank you, have a nice day"
    current_ticket = self.payForParking()
    
        #If ticket is not paid, bring them back to payment
    if current_ticket == "Paid":
        print("Thank you and have a nice day!")
        self.parking_spaces.add()
        self.available_tickets.add()
        self.active_tickets.remove()
    else:
        print("You still have a balance of {total}")
            self.payForParking
        #Update the parking spaces + 1
    #self.parking_spaces.add()
        #Update the available tickets + 1
    #self.available_tickets.add()
        #Take their ticket out of the active_tickets list
    ##self.active_tickets.remove()