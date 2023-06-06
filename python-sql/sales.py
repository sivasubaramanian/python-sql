import sqlite3
import matplotlib.pyplot as plt

# Function to retrieve data from SQLite database
def fetch_data():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT month, sales FROM sales_data')
    data = cursor.fetchall()
    
    conn.close()
    
    return data


def visualize_sales(months, sales):
    plt.figure(figsize=(15,5))
    plt.bar(months, sales, color=['black', 'red', 'green', 'blue', 'cyan','orange'])
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly Sales Data')
    plt.show()


def main():
    try:
        data = fetch_data()
        
        if len(data) == 0:
            raise Exception("No data available.")
        
        months, sales = zip(*data)
        
        visualize_sales(months, sales)
        
    except Exception as e:
        print("Error:", str(e))

if __name__ == '__main__':
    main()
