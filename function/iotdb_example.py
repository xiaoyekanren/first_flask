from iotdb.Session import Session


class IoTDBExample:
    def __init__(self):
        self.user = 'root'
        self.password = 'root'
        self.host = '127.0.0.1'
        self.port = '6667'

    def connect(self):
        return Session(
            self.host,
            self.port,
            self.user,
            self.password
        )

    def query(self, sql):
        conn = self.connect()
        conn.open(False)
        data = conn.execute_query_statement(sql)
        format_data = self.format_query_results(data)
        conn.close()
        return format_data

    @staticmethod
    def format_query_results(query_results):
        list_ = []
        while query_results.has_next():
            row = query_results.next()
            fields = [str(field) for field in row.get_fields()]
            ts = row.get_timestamp()
            list_ += [[str(ts)] + fields]
        return list_


if __name__ == '__main__':
    abc = IoTDBExample()
    results = abc.query('show cluster')
    print(results)




