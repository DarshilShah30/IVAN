import aiml
import os
# Creating the kernel and Aiml File

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
        # kernel.saveBrain("bot_brain.brn")
        
# kernel = aiml.Kernel()
# kernel.learn("std-startup1.xml")
# kernel.respond("load aiml b")


while True:
    print (kernel.respond(input("Enter Your Message")))
