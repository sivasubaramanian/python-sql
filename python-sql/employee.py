import sqlite3
import matplotlib.pyplot as plt

# Function to retrieve data from SQLite database
def fetch_data():
    conn = sqlite3.connect('grade.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT StudentId ,Age FROM Student')
    data = cursor.fetchall()
    
    conn.close()
    
    return data

# Function to visualize sales data
def visualize_sales(StudentId, Age):
    plt.figure(figsize=(15,5))
    plt.bar(StudentId, Age, color=['black', 'red', 'green', 'blue', 'cyan','orange'])
    plt.xlabel('StudentId')
    plt.ylabel('Age')
    plt.title('student Data')
    plt.show()

# Main function to execute the project
def main():
    try:
        data = fetch_data()
        
        if len(data) == 0:
            raise Exception("No data available.")
        
        StudentId, Age = zip(*data)
        
        visualize_sales(StudentId, Age)
        
    except Exception as e:
        print("Error:", str(e))

if __name__ == '__main__':
    main()
