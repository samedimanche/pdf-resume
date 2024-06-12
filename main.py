import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QFileDialog
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

class ResumeGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resume Generator")
        self.setGeometry(100, 100, 400, 400)

        # Create input fields
        self.first_name_label = QLabel("First Name:")
        self.first_name_input = QLineEdit()
        self.last_name_label = QLabel("Last Name:")
        self.last_name_input = QLineEdit()
        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()
        self.education_label = QLabel("Education:")
        self.education_input = QLineEdit()
        self.work_label = QLabel("Work Experience:")
        self.work_input = QLineEdit()
        self.skills_label = QLabel("Skills:")
        self.skills_input = QLineEdit()

        # Create generate button
        self.generate_button = QPushButton("Generate Resume")
        self.generate_button.clicked.connect(self.generate_resume)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.education_label)
        layout.addWidget(self.education_input)
        layout.addWidget(self.work_label)
        layout.addWidget(self.work_input)
        layout.addWidget(self.skills_label)
        layout.addWidget(self.skills_input)
        layout.addWidget(self.generate_button)

        # Set the layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def generate_resume(self):
        # Get user input
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        age = self.age_input.text()
        education = self.education_input.text()
        work = self.work_input.text()
        skills = self.skills_input.text()

        # Create PDF resume
        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate(f"{first_name}_{last_name}_resume.pdf", pagesize=letter)
        elements = []

        # Add header
        header = Paragraph(f"{first_name} {last_name}", styles["Heading1"])
        elements.append(header)
        elements.append(Spacer(1, 12))

        # Add personal information
        personal_info = Paragraph(f"Age: {age}", styles["BodyText"])
        elements.append(personal_info)
        elements.append(Spacer(1, 12))

        # Add education
        education_section = Paragraph("Education", styles["Heading2"])
        elements.append(education_section)
        education_details = Paragraph(education, styles["BodyText"])
        elements.append(education_details)
        elements.append(Spacer(1, 12))

        # Add work experience
        work_section = Paragraph("Work Experience", styles["Heading2"])
        elements.append(work_section)
        work_details = Paragraph(work, styles["BodyText"])
        elements.append(work_details)
        elements.append(Spacer(1, 12))

        # Add skills
        skills_section = Paragraph("Skills", styles["Heading2"])
        elements.append(skills_section)
        skills_details = Paragraph(skills, styles["BodyText"])
        elements.append(skills_details)

        # Build the PDF
        doc.build(elements)

        # Show a success message
        file_path = f"{first_name}_{last_name}_resume.pdf"
        self.statusBar().showMessage(f"Resume saved successfully: {file_path}")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    resume_generator = ResumeGenerator()
    resume_generator.show()
    sys.exit(app.exec())
