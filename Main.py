import datetime

#Yes or no function (for simplicity)
def yes_or_no(question):
    reply = input(question + ":").lower().strip()
    if reply[0] == "y":
        return True
    elif reply[0] == "n":
        return False

#document for notes on patients (PLEASE NOT THIS DOCUMENT HAS TO BE IN THE SAME FOLDER AS THE PROGRAM)
doc = "notes.txt"

#introduction
print("Hello! Welcome to AloneTogether. I am the ChatBot.")
name = input("Please enter your name:")
age = str(input("Please enter your age:"))

#Patient number:
now = datetime.datetime.now()
pnum = str(str(now.day) + str(now.month) + str(now.year) + str(now.hour) + str(now.minute))


#Patient sheet for generation
def pat_known_effects(pnum, name, age, illness, medication, side_effects, document):
    f = open(document, "r+")
    f.readlines()
    f.write("Patient Number:" + " " + pnum)
    f.write(str("\nName:" + " " + name))
    f.write(str("\nAge:" + " " + age))
    f.write(str("\n\n*****" + "PATIENT KNOWS HIS SICKNESS AND HAS SIDE EFFECTS DUE TO MEDICINE" + "*****\n"))
    f.write(str("\nIllness:" + " " + illness))
    f.write(str("\nMedication currently on:" + " " + medication))
    f.write(str("\nSide effects:" + " " + side_effects))
    f.close()

def pat_known(pnum, name, age, illness, medication, document):
    f = open(document, "r+")
    f.readlines()
    f.write("Patient Number:" + " " + pnum)
    f.write(str("\nName:" + " " + name))
    f.write(str("\nAge:" + " " + age))
    f.write(str("\n\n*****" + "PATIENT KNOWS HIS SICKNESS" + "*****\n"))
    f.write(str("\nIllness:" + " " + illness))
    f.write(str("\nMedication currently on:" + " " + medication))
    f.close()

def pat_unknown(pnum, name, age, symp, med, cause, document):
    f = open(document, "r+")
    f.readlines()
    f.write("Patient Number:" + " " + pnum)
    f.write(str("\nName:" + " " + name))
    f.write(str("\nAge:" + " " + age))
    f.write(str("\n\n*****" + "PATIENT DOES NOT KNOW HIS SICKNESS" + "*****\n"))
    f.write(str("\nSymptomes:" + " " + symp))
    f.write(str("\nMedication:" + " " + med))
    f.write(str("\nCauses for feeling bad?:" + " " + cause))
    f.close()

#option
print("\n")
print("Hello", name, "how can I help you?")
print("[1] I am feeling ill")
print("[2] How do I prevent getting COVID-19?")
print("[3] I have other, general questions about COVID-19")
print("\n")

opt = int(input("Make a selection:"))

#illness branch
if opt==1:

    illq = yes_or_no("Do you know what illness you are suffering from?")

    if illq == True:
        illness = str(input("Please describe what illness you have:"))
        medication = str(input("Are you on any medication? If so, which?"))
        side_effq = yes_or_no("Are you suffering from any side effects?")
        
        if side_effq == True:
            side_effects = str(input("Can you describe your side effects?"))
            appq = yes_or_no("Would you like to make an appointment?")

            #Generate sheet for known_effects
            if appq == True:
                print("Making an appointment")
                pat_known_effects(pnum, name, age, illness, medication, side_effects, doc)
                
            elif appq == False:
                print("Opening a website for your possible symptomes")
                

        elif side_effq == False:
            appq = yes_or_no("Would you like to make an appointment?")

            #Generate sheet for known_noeffects
            if appq == True:
                print("Making an appointment")
                pat_known(pnum, name, age, illness, medication, doc)
            elif appq == False:
                print("Opening a website for your possible symptomes")
                

    elif illq == False:
        symp = str(input("Can you describe your symptomes?"))
        med = str(input("Are you on any medication? If so, which?"))
        cause = str(input("Can you describe any possible causes for why you are feeling like this?"))
        appq = yes_or_no("Would you like to make an appointment?")
        
        #Generate sheet for unknown
        if appq == True:
            print("Making an appointment")
            pat_unknown(pnum, name, age, symp, med, cause, doc)
        elif appq == False:
            print("Opening a website for your possible symptomes")
            
  
        
#Precaution and Prevention branch 
elif opt==2:
    print("[1] I would like to know more about hygiene")
    print("[2] Stay at home")
    print("[3] Social distancing")
    print("[4] Alert others")
    print("\n")

    opt5 = int(input("Make a selection:"))

    if opt5==1:
        print("Here's some info on hygiene")
    elif opt5==2:
        print("Here's some info on staying at home")
    elif opt5==3:
        print("Here's some info on social distancing")
    elif opt5==4:
        print("Here's some info on alerting others")

#General Branch
elif opt==3:
    print("Here is an overview of some information we can provide you with")
    print("[1] Home remedies")
    print("[2] Myths")
    print("[3] Future of the virus")
    print("[4] Covid or the flu")
    print("\n")
    print("What exactly would you like to know?")
