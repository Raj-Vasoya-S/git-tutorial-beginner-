# Python code to factory pattern for creating different types of data handlers
class DataHandler:
    """Base class for data handlers."""
    def read(self, source):
        raise NotImplementedError("Subclasses must implement this method")
    def write(self, destination, data):
        raise NotImplementedError("Subclasses must implement this method")
class CSVHandler(DataHandler):
    """Handler for CSV data."""
    def read(self, source):
        print(f"Reading data from CSV file: {source}")
        # Implement CSV reading logic here
    def write(self, destination, data):
        print(f"Writing data to CSV file: {destination}")
        # Implement CSV writing logic here
class JSONHandler(DataHandler):
    """Handler for JSON data."""
    def read(self, source):
        print(f"Reading data from JSON file: {source}")
        # Implement JSON reading logic here
    def write(self, destination, data):
        print(f"Writing data to JSON file: {destination}")
        # Implement JSON writing logic here
class XMLHandler(DataHandler):
    """Handler for XML data."""
    def read(self, source):
        print(f"Reading data from XML file: {source}")
        # Implement XML reading logic here
    def write(self, destination, data):
        print(f"Writing data to XML file: {destination}")
        # Implement XML writing logic here
class DataHandlerFactory:
    """Factory class to create data handlers."""
    @staticmethod
    def get_data_handler(handler_type):
        if handler_type == 'csv':
            return CSVHandler()
        elif handler_type == 'json':
            return JSONHandler()
        elif handler_type == 'xml':
            return XMLHandler()
        else:
            raise ValueError(f"Unknown handler type: {handler_type}")
# Usage example
def main(): 
    csv_handler = DataHandlerFactory.get_data_handler('csv')
    csv_handler.read('data.csv')
    csv_handler.write('data_out.csv', {'key': 'value'})
    json_handler = DataHandlerFactory.get_data_handler('json')
    json_handler.read('data.json')
    json_handler.write('data_out.json', {'key': 'value'})
    xml_handler = DataHandlerFactory.get_data_handler('xml')
    xml_handler.read('data.xml')
    xml_handler.write('data_out.xml', {'key': 'value'})
if __name__ == "__main__":
    main()
# End of Data.py module

# We will create a simple Python module named str.py that contains utility functions for string manipulation.
def reverse_string(s):
    """Returns the reverse of the input string."""
    return s[::-1]
def is_palindrome(s):
    """Checks if the input string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]
def count_vowels(s):
    """Counts the number of vowels in the input string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
def to_uppercase(s):
    """Converts the input string to uppercase."""
    return s.upper()
def to_lowercase(s):
    """Converts the input string to lowercase."""
    return s.lower()
def capitalize_string(s):
    """Capitalizes the first letter of each word in the input string."""
    return s.title()    
def main():
    test_string = "A man, a plan, a canal: Panama"
    print("Original string:", test_string)
    print("Reversed string:", reverse_string(test_string))
    print("Is palindrome:", is_palindrome(test_string))
    print("Vowel count:", count_vowels(test_string))
    print("Uppercase string:", to_uppercase(test_string))
    print("Lowercase string:", to_lowercase(test_string))
    print("Capitalized string:", capitalize_string(test_string))    
if __name__ == "__main__":
    main()
# End of str.py module