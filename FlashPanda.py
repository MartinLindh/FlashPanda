#FlashPanda.py

doc  = '''
Names:
FlashPanda


This script generates Pandas exercises

pandas methods
pd.read_csv
pd.dataframe

df.head
df.tail
df.sample
df.dtypes
df.index
df.columns
df.values
df.to_csv
df.rename

Append rows of DataFrame
pd.concat([df1,df2], axis=0)


df.describe
df.sort_values
df.loc
df.iloc
df.isin
df.rename
df.iterrows

df.ix has been deprecated (fasats ut)
df.isna
df.notna
df.drop(columns=['a','b'])

df.pivot

Order rows by values of a column (low to high)
df.sort_values('mpg')

Order rows by values of a column (high to low)
df.sort_values('mpg'
Gather coloumns inro rows
pd.melt(df)

Append rows of DataFrame
pd.concat([df1,df2], axis=0)

Append columns of DataFrame
pd.concat([df1,df2],axis=1

inplace = True/False

subjects to ask about
category data type
df.describe(include=['object'])


Development Ideas:
 Move to a Jupyter notebook X
 Put notebook on Github X
 Read one csv-file, write another
 implement the tracking of questions

 set limit on how many times a question can arrise
 make aswers into a [list] with multiple correct answers

 https://mybinder.org/
 Ask for questions on /r/learnpython
 categorise the questions - topic, ought it be inclusive or exclusinve categories?
    super basic
    plotting
    timeseries
 categorise the questions - source
 create a way for useers to chose categories they like to train.
 Connect to youtube lecturers
 export the questions to excell-file
'''

#imports

import pandas as pd
import random
import os
import sys

def header(msg):
    print('-'* 50)
    print('[ ' + msg + ' ]\n')

def question(msg):
    print('   || ')
    print('   || '+ msg)
    print('   || \n')

def get_question_number(questions_df):
    limit_num_question = 1

    #Check if all questions are answered
    if questions_df['grading'].sum() >= len(questions_df) * limit_num_question:
        print('All questions have been answered.')
        shutdown(questions_df)

    question_number = random.randint(0, len(questions_df)-1)
    if questions_df.loc[question_number, 'grading'] >= limit_num_question:
        question_number = get_question_number(questions_df)
    return question_number

def random_question(questions_df):
    question_number = get_question_number(questions_df)

    header('Question: ' + str(question_number))

    question(questions_df.loc[question_number,'question'])

    answer = input('Answer:')

    return answer, question_number

def grade_answer(answer, question_number, questions_df):
    #print(questions_df.loc[question_number,'answer'])

    if answer.strip() == str(questions_df.loc[question_number,'answer'].strip()):
        print('\nCorrect\n')

        if DEBUG:
            print(question_number)
            print(type(question_number))

        grade = questions_df.loc[question_number, 'grading']


        if DEBUG:
            print(grade)
        questions_df.at[question_number, 'grading'] = grade++1
    else:
        print('The correct answer is: '+ questions_df.loc[question_number,'answer'])

    return questions_df

def startup():
    os.system('cls')
    header('Starting game')

    #Check if DEBUG-mode
    if DEBUG:
        print('DEBUG MODE')

    #Loads questions_local.csv if it exist
    fname1 = 'questions_local.csv'
    fname2 = 'questions.csv'


    if os.path.isfile(fname1):
        questions_df = pd.read_csv(fname1, ';')
        if DEBUG:
            print('opened ',fname1)
    else:
        questions_df = pd.read_csv(fname2,';')
        print('opened ', fname2)

    print('Use q to quit')
    print('Code used: \nimport padas as pd')
    print('-' * 50)

    return questions_df


def shutdown(questions_df):
    #shutdown procedure

    questions_df.to_csv('questions_local.csv',sep = ';',index = False)
    print('-' * 50)
    sys.exit()

def main():

    global DEBUG
    DEBUG = True

    questions_df = startup()

    #Question loop
    answer = ''
    while(answer != 'q' and answer != 'Q'):
        answer, question_number = random_question(questions_df)
        questions_df = grade_answer(answer,question_number, questions_df)

    shutdown(questions_df)

    return None


if __name__ == '__main__':
    main()