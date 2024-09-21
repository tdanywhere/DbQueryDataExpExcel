import jpype
import jaydebeapi

class OracleDB:
    def __init__(self, username, password, dsn, mode=None):
        """
        Initialize database connection.

        :param username: Database username
        :param password: Database password
        :param dsn: Data Source Name (TNS entry or Easy Connect string)
        :param mode: Connection mode (e.g., cx_Oracle.SYSDBA)
        """
        self.username = username
        self.password = password
        self.dsn = dsn
        self.mode = mode
        self.connection = None

        jHome = jpype.getDefaultJVMPath()
        jpype.startJVM(jHome, '-Djava.class.path=./lib/jdbc/ojdbc8.jar', convertStrings=True)


    def connect(self):
        """Connect to the database."""
        try:
            if self.mode:
                print('connect, self_mode')
            else:
                print('connect, NOT self_mode')
            print("Database connection established.")
        except: 
            print(f"Database connection failed")

    def disconnect(self):
        """Disconnect from the database."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")


    def getConnection(self):
        """Connect to the database and return connection."""
        try:
            if self.mode:
                print("getConnection, self_mode")
                self.connection = jaydebeapi.connect('oracle.jdbc.driver.OracleDriver',f"jdbc:oracle:thin:{self.username}/{self.password}@{self.dsn}")
            else:
                print("getConnection, NOT self_mode")
                self.connection = jaydebeapi.connect('oracle.jdbc.driver.OracleDriver',f"jdbc:oracle:thin:{self.username}/{self.password}@{self.dsn}")

            print("Database connection established.")
        except:
            print(f"Database connection failed")
        return self.connection


# Usage example:
if __name__ == "__main__":
    print("Main")
    ## Your Oracle XE DSN (Data Source Name) format could look like this: [hostname]:[port]/[DB service name]
    # dsn = "localhost:1521/xepdb1"
    #db = OracleDB("sys", "master", dsn, mode=cx_Oracle.SYSDBA)
    #db.connect()
    ## Perform database operations
    #db.disconnect()
