# pdf-resume

 Python program that uses PyQt6 and the ```reportlab``` library to create a PDF resume with a modern design style. The program will prompt the user to enter their personal information, and then generate a PDF resume based on the provided data.<br/>

 Here's how the code works:<br/>

The ResumeGenerator class inherits from QMainWindow and sets up the user interface with input fields for the user's personal information (first name, last name, age, education, work experience, and skills).<br/>
The generate_resume method is called when the user clicks the "Generate Resume" button.<br/>
The user's input is retrieved from the respective input fields.<br/>
The reportlab library is used to create a PDF document with the user's information.<br/>
The getSampleStyleSheet function from reportlab is used to define the styles for different elements in the PDF.<br/>
A SimpleDocTemplate object is created with the file name in the format {first_name}_{last_name}_resume.pdf.<br/>
The user's information is added to the PDF document as Paragraph objects with appropriate styles.<br/>
The build method of the SimpleDocTemplate object is called to generate the PDF file.<br/>
A success message is displayed in the status bar with the file path of the generated PDF resume.<br/>
To run the program, you need to have PyQt6 and the reportlab library installed. You can install them using pip:<br/>
```
pip install PyQt6 reportlab
```
<br/>
When you run the program, a window will appear with input fields for your personal information. After entering the required details, click the "Generate Resume" button to create a PDF resume with a modern design style based on the provided information.
