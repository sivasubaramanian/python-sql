import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Function to connect to the SQLite database
def connect_to_database():
    conn = sqlite3.connect('grade.db')
    print (conn)
    if conn :
        print ("sucess")
    else:
        print("fail")
    return conn




# Function to execute an SQL query
def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Function to plot the grade distribution
def plot_grade_distribution(data):
    grades = data['Grade']
    grade_counts = data['GradeCount']

    plt.bar(grades, grade_counts)
    plt.xlabel('Grades')
    plt.ylabel('Count')
    plt.title('Grade Distribution')
    plt.show()

try:
    # Connect to the database Grade, COUNT(*) as GradeCount FROM Grades GROUP BY Grade
    conn = connect_to_database()

    # Execute an SQL query to retrieve the grade distribution
    query = "SELECT StudentId from Student"
    result = execute_query(conn, query)

    # Create a pandas DataFrame from the result
    data = pd.DataFrame(result, columns=['StudentId'])

    # Plot the grade distribution
    #plot_grade_distribution(data)
    print(data)

except sqlite3.Error as e:
    print("Database error:", e)

except Exception as e:
    print("Error:", e)

finally:
    # Close the database connection
    if conn:
        conn.close()
