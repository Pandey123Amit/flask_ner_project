import json

class database:
    def __init__(self, filename='user.json'):
        self.filename = filename

    def load_data(self):
        try:
            with open(self.filename, 'r') as rf:
                return json.load(rf)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def insert(self, name, email, ids, password):
        data = self.load_data()

        if email in data:
            return False  # Email already exists
        else:
            data[email] = [name, ids, password]
            with open(self.filename, 'w') as wf:
                json.dump(data, wf)
            return True  # Data inserted successfully

    def get_password(self, email):
        data = self.load_data()
        if email in data:
            return data[email][2]  # Return the password
        return 'Your are not in our Database'  # Email not found
