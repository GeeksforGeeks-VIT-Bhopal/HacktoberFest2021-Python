# import the module for speech recognition
import speech_recognition as sr 

# create the recognizer 
u = sr.Recognizer() 

# define the microphone 
mic = sr.Microphone(device_index=0) 

# record your speech 
with mic as source: 
   audio = u.listen(source) 

# speech recognition 
result = u.recognize_google(audio)

# export the result output
with open('my_result.txt',mode ='w') as file: 
   file.write("Recognized text:") 
   file.write("\n") 
   file.write(result) print("Exporting process completed!")
