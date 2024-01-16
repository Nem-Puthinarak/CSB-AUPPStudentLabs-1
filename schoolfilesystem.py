
#Libraries you may need:
import csv
import pandas as pd
from urllib.request import urlopen
import datetime

class SchoolAssessmentSystem:
    def __init__(self):
        self.dataset = pd.DataFrame()

    def process_file(self, file_path, file_format):
        try:
            data = None  # Initialize data outside of the conditional block
            if file_format == 'csv':
                data = pd.read_csv(file_path)  # Remove skiprows=1
            elif file_format == 'excel':
                data = pd.read_excel(file_path)
            elif file_format == 'text':
                with open(file_path, 'r') as text_file:
                    # Assuming each line in the text file represents a record
                    lines = text_file.readlines()
                    data = [line.strip().split(',') for line in lines]

                # Convert the list of lists to a DataFrame
                data = pd.DataFrame(data, columns=['Student', 'Subject', 'Score'])
            else:
                raise ValueError("Unsupported file format")

            self.dataset = pd.concat([self.dataset, data], ignore_index=True)
            print(f"File '{file_path}' processed successfully.")
            print("Dataset columns:", self.dataset.columns)  # Add this line

        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except PermissionError:
            print(f"Error: Permission denied. Check read permissions for '{file_path}'.")
        except Exception as e:
            print(f"Error processing file: {e}")

    

    def transfer_data(self, criteria):
        try:
            # Example: Transfer students with scores above a certain threshold to another file
            threshold = criteria.get("threshold", 90)
            high_scorers = self.dataset[self.dataset['Score'] > threshold]
            
            # Save the high-scorers to a new file
            high_scorers.to_csv("high_scorers.csv", index=False)

        except Exception as e:
            print(f"Error transferring data: {e}")

    def fetch_web_data(self, url):
        try:
            with urlopen(url) as response:
                # Placeholder logic to read HTML content from the webpage
                web_data = response.read()
                print("Web data fetched successfully.")

        except Exception as e:
            print(f"Error fetching web data: {e}")

   
    def analyze_content(self):
        try:
            if 'Score' in self.dataset.columns:
                average_score = self.dataset['Score'].mean()
                print(f"\nAverage Overall Score: {average_score}\n")

                # Subject-wise analysis
                print("Subject-wise Analysis:")
                for subject in self.dataset['Subject'].unique():
                    subject_data = self.dataset[self.dataset['Subject'] == subject]
                    subject_avg_score = subject_data['Score'].mean()
                    print(f"   - {subject}: Average Score - {subject_avg_score}")

            else:
                raise ValueError("Error analyzing content: 'Score' column not found in the dataset.")

        except Exception as e:
            print(f"Error analyzing content: {e}")

    def generate_summary(self):
        try:
            if 'Student' in self.dataset.columns:
                print("\nSchool Assessment Summary Report:\n")

                # Individual Student Performance
                print("Individual Student Performance:")
                for student in self.dataset['Student'].unique():
                    student_data = self.dataset[self.dataset['Student'] == student]
                    student_avg_score = student_data['Score'].mean()
                    top_subject = student_data.loc[student_data['Score'].idxmax()]['Subject']
                    print(f"   - {student}: Average Score - {student_avg_score}, Top Subject - {top_subject}")

                # Subject-wise Analysis
                print("\nSubject-wise Analysis:")
                for subject in self.dataset['Subject'].unique():
                    subject_data = self.dataset[self.dataset['Subject'] == subject]
                    subject_avg_score = subject_data['Score'].mean()
                    print(f"   - {subject}: Average Score - {subject_avg_score}")

                # Recommendations
                print("\nRecommendations:")
                for subject in self.dataset['Subject'].unique():
                    subject_data = self.dataset[self.dataset['Subject'] == subject]
                    low_performers = subject_data[subject_data['Score'] < 70]
                    if not low_performers.empty:
                        print(f"   - Consider additional support for students in {subject}")

                # Web Data Insights
                print("\nWeb Data Insights:")
                # Placeholder for web data insights

                # Report Date
                print(f"\nReport generated on: {datetime.date.today()}")

            else:
                raise ValueError("Error generating summary: 'Student' column not found in the dataset.")

        except Exception as e:
            print(f"Error generating summary: {e}")

# Example Usage:
school_system = SchoolAssessmentSystem()
school_system.process_file("sample.csv", "csv")
school_system.transfer_data(criteria={"threshold": 90})
school_system.fetch_web_data("https://schoolwebsite.com/assessment")
school_system.analyze_content()
school_system.generate_summary()


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
