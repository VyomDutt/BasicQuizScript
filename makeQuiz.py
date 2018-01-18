# This script makes 20 different quizzes from a single database.

import random
import os

# Define the database nicely

captains = {'India' : 'Virat Kohli', 'Australia' : 'Steve Smith','Bangladesh':'Mashrafe Mortaza','England':'Eoin Morgan'}

# Generate the Directories for the Quiz

currentDir = os.getcwd()
os.makedirs(os.path.join(currentDir,'Quiz'))
os.makedirs(os.path.join(currentDir,'Quiz','Quizzes'))
os.makedirs(os.path.join(currentDir,'Quiz','Answer Keys'))
quizPath = os.path.join(currentDir,'Quiz','Quizzes')
answerPath = os.path.join(currentDir,'Quiz','Answer Keys')


for index in range(20):

    #Creates the folder for Quiz & Answers Files
    
    quizFile = open(os.path.join(quizPath,'QuizNo%s.txt') %(index+1),'w')
    answersFile = open(os.path.join(answerPath,'AnswerNo%s.txt')%(index+1),'w')

    #Write out a "template" for the Quizzes (for details for students)

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(('-'*20) + 'Team-Captain Quiz (Form #%s)'%(index +1) + ('-'*20))
    quizFile.write('\n\n')

    #Randomize the order

    teams = list(captains.keys())
    random.shuffle(teams)

    #Loop through all the captains
    for question in range(4):

        #Get right and wrong answers
        correctAnswer = captains[teams[question]]
        wrongAnswers = list(captains.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,1)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #Write the question and the options to the quiz file

        quizFile.write('%s. Who is the captain of %s?\n'%(question+1,teams[question]))

        for i in range(2):
            quizFile.write('%s. %s\n' % ('AB'[i],answerOptions[i]))

        quizFile.write('\n')
        answersFile.write('%s.%s\n'%(question+1,'AB'[answerOptions.index(correctAnswer)]))

    #Close the files
                                     
    quizFile.close()
    answersFile.close()
    
#end of script
        
