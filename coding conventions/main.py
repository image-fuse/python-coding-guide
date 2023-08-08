import json

class StudentRecordsManager:
    """Class to manage student records."""
    
    def __init__(self, records_file):
        """
        Initialize the records manager.

        Parameters:
        records_file (str): Path to the JSON file for storing records.
        """
        self.records_file = records_file
        self.records = self._load_records()
    
    def _load_records(self):
        """Load records from the JSON file."""
        try:
            with open(self.records_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def _save_records(self):
        """Save records to the JSON file."""
        with open(self.records_file, 'w') as file:
            json.dump(self.records, file, indent=4)
    
    def add_student(self, student_id, name, age, grade):
        """
        Add a new student to the records.

        Parameters:
        student_id (int): Student's ID.
        name (str): Student's name.
        age (int): Student's age.
        grade (str): Student's grade.

        Returns:
        None
        """
        student = {
            'student_id': student_id,
            'name': name,
            'age': age,
            'grade': grade
        }
        self.records.append(student)
        self._save_records()
    
    def search_student(self, query):
        """
        Search for a student by student_id or name.

        Parameters:
        query (str or int): Student ID or name to search.

        Returns:
        dict or None: Student information if found, otherwise None.
        """
        for student in self.records:
            if query == student['student_id'] or query == student['name']:
                return {
                    'age': student['age'],
                    'grade': student['grade']
                }
        return None
    
    def update_student(self, query, age=None, grade=None):
        """
        Update a student's information by student_id or name.

        Parameters:
        query (str or int): Student ID or name to update.
        age (int): New age value (optional).
        grade (str): New grade value (optional).

        Returns:
        bool: True if the student's information was updated, False otherwise.
        """
        for student in self.records:
            if query == student['student_id'] or query == student['name']:
                if age is not None:
                    student['age'] = age
                if grade is not None:
                    student['grade'] = grade
                self._save_records()
                return True
        return False

# Example usage
if __name__ == "__main__":
    records_manager = StudentRecordsManager("student_records.json")
    
    records_manager.add_student(1, "Alice", 18, "A")
    records_manager.add_student(2, "Bob", 19, "B")
    
    print(records_manager.search_student("Alice"))
    print(records_manager.search_student(2))
    
    records_manager.update_student("Bob", age=20)
    print(records_manager.search_student("Bob"))
