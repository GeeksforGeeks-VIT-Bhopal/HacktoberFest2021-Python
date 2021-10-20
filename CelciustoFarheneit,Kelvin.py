a=int(input("enter temp in celcius"))
b=int(input('''press 1 to convert to farenheit scale
press 2 to convert to kelvin scale'''))
#we will use if else statements
if b==1:
                c=(a*9/5)+32 
                #formula to convert to degree farenheit
                print(c,"degree farenheit")
else:
                d=a+273.15
                #formula to convert to Kelvin
                print(d,"kelvins")