import psycopg2


#1.) retrieves and displayes all records from the students table
def getAllStudents():
    print('\n')
    #SQL query to select all records
    statement.execute('SELECT * FROM students')
    #fetches all results from the query and then prints it
    for record in statement.fetchall():
        print(record)
    print('\n')

#2.) Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    sqlCommand = 'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s,%s,%s,%s)'
    #tuple containing data to be added
    newRecord = (first_name, last_name, email, enrollment_date)
    #execute the sqlCommand along with its tuple data
    statement.execute(sqlCommand, newRecord)
    print("student added successfully")
    #just added so we can view the update
    getAllStudents() 

#3.) Updates the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email): 
    sqlCommand = 'UPDATE students SET email = %s WHERE students_id = %s'
    updateRecord = (new_email, student_id)
    statement.execute(sqlCommand, updateRecord)
    print("email updated successfully")
    #view the update
    getAllStudents() 

#4.) Deletes the record of the student with the specified student_id
def deleteStudent(student_id): 
    sqlCommand = 'DELETE FROM students WHERE students_id = %s'
    deleteRecord = (student_id,)
    statement.execute(sqlCommand, deleteRecord)
    print("record deleted successfully")
    #view the update
    getAllStudents() 


#establishing the connection and interaction between the python application and the database
try:
    #establish connection with database
    connection = psycopg2.connect(host= "localhost", port="5432", database= "Assignment3", user= "postgres", password= "password" )
    #create cursor object to interact with database
    statement = connection.cursor()
  
    #application functions being executed

    #1.) 
    getAllStudents() 

    #2.) 
    addStudent(input('what is the student first name: '), input('what is the student last name: '), input('what is the student email: '), input('date student enrolled: '))

    #3.)
    updateStudentEmail(int(input('student id for email update: ')), input('update student email to: '))

    #4.)
    deleteStudent(int(input('student id you want to delete: ')))
    
    #commit the changes to  database
    connection.commit()

#handling any errors
except Exception as error: 
    print(f'An error has occured: {error}')

#closing the connection to the database when program closes
finally: 
    if connection is not None: 
        connection.close()



    



