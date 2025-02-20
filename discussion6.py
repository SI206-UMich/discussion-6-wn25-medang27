#lecture work
import unittest
import os
import csv

def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    '''
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    
    data = {}
    
    with open(full_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip header
        
        for row in reader:
            year, month, value = row
            if year not in data:
                data[year] = {}
            data[year][month] = value  # Keep values as strings, per instructions
    
    return data

def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
    '''
    result = []
    
    for year, months in d.items():
        max_month = max(months, key=lambda m: int(months[m]))  # Find month with max value
        max_value = int(months[max_month])  # Convert to int
        result.append((year, max_month, max_value))
    
    return result

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and values are rounded averages.
    '''
    avg_dict = {}
    
    for year, months in d.items():
        values = [int(v) for v in months.values()]  # Convert all values to int
        avg_dict[year] = round(sum(values) / len(values))  # Compute average and round
    
    return avg_dict
    

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
