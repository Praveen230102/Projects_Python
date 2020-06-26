import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


# ------------------ this function is for voice ------------------


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

def take_command():

    # this will input the command from user and output this in form of string
    
    r = sr.Recognizer()

    # assigning a variable for inputing the speech

    with sr.Microphone() as source:

        # this will input from microphone as source
        # and print this statement as he is listning

        print("Listening .......")

        r.pause_threshold = 1

        # what this function will do

        # when a person is speaking it the command will listen and if user takes
        # a break then system will consider that the command is complete
        # initially the time command is 0.8
        # we have been changed it to 1
        # so it will give us more time

        # now we will use listen module of speech recognition

        audio = r.listen(source)

        # this audio is coming from source as we have been assigned it earlier

    # now lets try this
    # by using try function

    try:

        print("Recognizing....")
        
        # we have been used this r because above we have been defined as recognizer


        query = r.recognize_google(audio, language= "en-in")

        # now the input is firstly recognized by google in language enlish
        # en-in ---> english - india

        # now we are going to print what user said

        print("User said: ", query)

    # now if didn't listen it
    # then it will through an error

    except Exception as e:

        # this will accept the exception and input it in variable e

        # and print that
        # if you are a proper coder then you will not give the error to user

        # so we will not print the exception

        # print(e)

        # now if recognizer didn't listen it then firstly it will print error
        # then print a message

        print("Sorry please say again ....")

        return "None"

    return query


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

    speak("I am jarvis Sir. Please tell how may I help you .")

    


def chota_jarvis():
    # this will send all the messages to other function and for that we
    # just have to call this function

    # speak("Praveen is badass !!!!")

    wish()

    # now we will use a infinte loop
    # for input

    # for the best we will use while loop

    while True:

        query = take_command().lower()

        # it will take the command in lower string and perform it

        # we have been print it above but now we want to execute this task

        
        # now we will search on the basis of input query

        # now we will search "wikipedia" in query if this is present
        # then it will use wikipedia module

        if "wikipedia" in query:

            speak("Searching wikipedia .....")
            query = query.replace("wikipedia", "")
            # replacing the word wikipedia with ""

            result = wikipedia.summary(query, sentences=1)

            # now we will use wikipedia module for getting the summary
            # of the query in one line

            # we have been replaced wikipedia word because we want
            # to give that query to wikipedia to search it and provide us answer
                  
            # now we will print the output using speak function

            speak("According to wikipedia ....")
            speak(result)
            # now this will just speak it
            # this will not print it
            print(result)


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

# for sending email firstly read about SMTP



chota_jarvis()
