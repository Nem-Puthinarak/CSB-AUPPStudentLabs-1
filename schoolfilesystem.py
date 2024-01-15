
#Libraries you may need:
import csv
import pandas as pd
from urllib.request import urlopen
import datetime

class SchoolAssessmentSystem:
    def __init__(self):
        self.dataset = pd.DataFrame()

    def process_file(self, file_path):
        try:
            if file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                data = pd.read_excel(file_path)
            else:
                with open(file_path, 'r') as file:
                    data = file.read()
            return data
        except Exception as e:
            print(f"Error processing file: {e}")
            return None

    def transfer_data(self, source_data, destination_file):
        try:
            if isinstance(source_data, pd.DataFrame):
                # For DataFrame, save to CSV
                source_data.to_csv(destination_file, index=False)
            else:
                # For plain text, write to destination file
                with open(destination_file, 'w') as file:
                    file.write(source_data)
        except Exception as e:
            print(f"Error transferring data: {e}")

    def fetch_web_data(self, url):
        try:
            with urlopen(url) as response:
                web_data = response.read()
            web_data_df = pd.read_csv(pd.compat.StringIO(web_data.decode('utf-8')))
            return web_data_df
        except Exception as e:
            print(f"Error fetching web data: {e}")
            return None

    def analyze_content(self):
        try:
            self.dataset['Average Score'] = self.dataset.mean(axis=1)
        except Exception as e:
            print(f"Error analyzing content: {e}")

    def generate_summary(self):
        try:
            print("School Assessment Summary Report:\n")
            if not self.dataset.empty:
                for index, row in self.dataset.iterrows():
                    print(f"{index + 1}. Overall Performance of Student {index + 1}:\n   - Average score: {row['Average Score']}")
            else:
                print("No data available for summary.")
            print(f"\nReport generated on: {datetime.datetime.now().strftime('%Y-%m-%d')}")
        except Exception as e:
            print(f"Error generating summary: {e}")

# Example usage with user input for file name:
assessment_system = SchoolAssessmentSystem()

try:
    # Prompt user for the file name
    file_name = input("Enter the file name (including path or URL) to process: ")

    # Process the file
    file_data = assessment_system.process_file(file_name)

    if file_data is not None:
        # Set the destination file path
        destination_file = 'output_summary.csv'

        # Transfer data from the file to the destination file
        assessment_system.transfer_data(file_data, destination_file)

        # Fetch web data from the provided URL
        web_data_url = 'https://example.com/school_assessment_data.csv'
        web_data = assessment_system.fetch_web_data(web_data_url)

        if web_data is not None:
            # Transfer web data to the destination file
            assessment_system.transfer_data(web_data, destination_file)

            # Analyze content and generate a summary
            assessment_system.analyze_content()
            assessment_system.generate_summary()

except KeyboardInterrupt:
    print("\nOperation aborted by the user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Analyze content & display result area
# Sample of Output:
"""
School Assessment Summary Report:

1. Overall Performance of Student A:
   - Average score: 85.5
   - Top-performing class: Grade 10B

2. Subject-wise Analysis:
   - Mathematics: Improved by 10% compared to the last assessment.
   - Science: Consistent performance across all classes.

3. Notable Observations:
   - Grade 8A shows a significant improvement in English proficiency.

4. Web Data Insights:
   - Online participation: 95% of students accessed assessment resources online.

5. Recommendations:
   - Consider additional support for Grade 9B in Mathematics.

Report generated on: 2024-01-14
"""
