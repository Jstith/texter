import ezgmail

# List of domain names for SMTP gateways for wireless providers
domainNames = {
    "AT&T": "txt.att.net",
    "Boost-Mobile": "sms.myboostmobile.com",
    "Cricket": "sms.cricketwireless.com",
    "Google-Fi": "msg.fi.google.com",
    "Metro-PCS": "mymetropcs.com",
    "Republic-Wireless": "text.republicwireless.com",
    "Sprint": "messaging.sprintpcs.com",
    "T-Mobile": "tmomail.net",
    "U.S.-Cellular": "email.uscc.net",
    "Verizon": "vtext.com",
    "Virgin-Mobile": "vmobl.com",
    "XFinity-Mobile": "vtext.com"
}

# Gets carrier and number from user
print("Enter provider of target number (0 if unknown/force):")
for x in domainNames:
    print('\t', x)
carrier = input()
number = input("Enter target number:\t")

# Formats the number to get rid of extraneous characters
number = number.replace('-', '')
number = number.replace('(', '')
number = number.replace(')', '')
number = number.replace(' ', '')

# Gets message to send
message = input("Enter message:\t")

# Formats address and sends email
if(carrier == '0'):
    # Brute forces all domains (phone numbers are unique so only one will work)
    # Fair warning, you'll get your email flodded with failed message announcements if you do this
    for x in domainNames:
        address = "" + number + "@" + domainNames[x]
        ezgmail.send(address, "/", message)
else:    
    address = "" + number + "@" + domainNames[carrier]
    ezgmail.send(address, "/", message)
