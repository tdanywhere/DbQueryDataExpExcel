import cx_Oracle

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

    def connect(self):
        """Connect to the database."""
        try:
            if self.mode:
                self.connection = cx_Oracle.connect(self.username, self.password, self.dsn, mode=self.mode)
            else:
                self.connection = cx_Oracle.connect(self.username, self.password, self.dsn)
            print("Database connection established.")
        except cx_Oracle.DatabaseError as e:
            print(f"Database connection failed: {e}")

    def disconnect(self):
        """Disconnect from the database."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")


    def getConnection(self):
        """Connect to the database and return connection."""
        try:
            if self.mode:
                self.connection = cx_Oracle.connect(self.username, self.password, self.dsn, mode=self.mode)
            else:
                self.connection = cx_Oracle.connect(self.username, self.password, self.dsn)
            print("Database connection established.")

        except cx_Oracle.DatabaseError as e:
            print(f"Database connection failed: {e}")

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
