import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser





# now creating a function which will speak

engine = pyttsx3.init("sapi5")
# sapi5 is APi of microsoft this api is used for speech recognision

voices = engine.getProperty("voices")

# now using engine variable for speaking it

engine.setProperty("voice", voices[0].id)
# i am using voice for index number 0 because at index number 0 male voice is present
# if I will use index number 1 then female voice will used

# --------------------------------------------------------------

# now creating a function which input the argument and speaks it

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

# this function is used for getting voice as argument as pronouncing it

# now we are defining the main function


# now if I want my chota jarvis to wish me
# i have to give create a funcion which will wish me
def wish():

    hour = int(datetime.datetime.now().hour)

    # this will give the right time in form of hours

    # now if jarvis want to wish us then there will be some time

    # for instance if there is after noon then this will wish me good afternoon
    

    if hour >= 0 and hour < 12:
        speak("Good Morning !!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good evening !!")


    # now the basic question arises is that if we wish someone
    # then we will also say our name

    # now we will create a speak function which will speak
    # about jarvis

    speak("I am JARVIS Sir. Please tell how may I help you .")

    
def take_command():
  string = input("Enter the command you wanna to perform > ")
  string.lower()
  return string



def chota_jarvis():
    # this will send all the messages to other function and for that we
    # just have to call this function

    # speak("Praveen is badass !!!!")

    wish()

    # now we will use a infinte loop
    # for input

    # for the best we will use while loop

    while True:

        query = take_command()

        # it will take the command in lower string and perform it

        # we have been print it above but now we want to execute this task

        
        # now we will search on the basis of input query

        # now we will search "wikipedia" in query if this is present
        # then it will use wikipedia module

        if "wikipedia" in query:

            speak("Searching wikipedia .....")
            query = query.replace("wikipedia", "")
            # replacing the word wikipedia with ""

            result = wikipedia.summary(query, sentences=5)

            # now we will use wikipedia module for getting the summary
            # of the query in one line

            # we have been replaced wikipedia word because we want
            # to give that query to wikipedia to search it and provide us answer
                  
            # now we will print the output using speak function

            speak("According to wikipedia ....")
            print(result)
            speak(result)
            # now this will just speak it
            # this will not print it
            


        # now let say if user want to open google or youtube
        # then for this case we have to inport web browser module

        elif "open youtube" in query:


          webbrowser.open("youtube.com")
        
        elif "open google" in query:

          webbrowser.open("google.com")

        elif "open twitter" in query:

          webbrowser.open("twitter.com")

        elif "open github" in query:

          webbrowser.open("github.com")

        elif "open spotify" in query or "open music" in query:

          webbrowser.open("spotify.com")


        elif "open instagram" in query:

          webbrowser.open("instagram.com")


        elif "open stackoverflow" in query:

          webbrowser.open("stackoverflow.com")

        elif "the time" in query:
          strtime = datetime.datetime.now().strftime("%H:%M:%S")
          speak("The time is ", strtime)

        elif "chota jarvis" in query:

            speak("Chota jarvis is created by Sir Praveen Kumar singh for his friend !!")

        elif "who made you" in query:
            speak("Sir Praveen, made me !!")

# for sending email firstly read about SMTP



chota_jarvis()

