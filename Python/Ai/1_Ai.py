import sys
import json
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox

class CurlApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("cURL Request GUI")
        self.setGeometry(100, 100, 400, 300)

        # Create layout
        layout = QVBoxLayout()

        # URL input
        self.url_label = QLabel("URL:")
        self.url_input = QLineEdit(self)
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)

        # Prompt input
        self.prompt_label = QLabel("Prompt:")
        self.prompt_input = QTextEdit(self)
        layout.addWidget(self.prompt_label)
        layout.addWidget(self.prompt_input)

        # Send button
        self.send_button = QPushButton("Send Request", self)
        self.send_button.clicked.connect(self.send_request)
        layout.addWidget(self.send_button)

        # Response output
        self.response_label = QLabel("Response:")
        self.response_output = QTextEdit(self)
        self.response_output.setReadOnly(True)
        layout.addWidget(self.response_label)
        layout.addWidget(self.response_output)

        self.setLayout(layout)

    def send_request(self):
        url = self.url_input.text()
        prompt = self.prompt_input.toPlainText()

        # Prepare the JSON data
        data = json.dumps({"prompt": prompt})
        headers = {'Content-Type': 'application/json'}

        try:
            # Send the POST request
            response = requests.post(url, headers=headers, data=data)

            # Display the response
            self.response_output.setPlainText(response.text)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurlApp()
    window.show()
    sys.exit(app.exec_())



    # Another one 
    previous_code = """ 
    import json
    import requests
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox

    class CurlApp(QWidget):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("cURL Request GUI")
            self.setGeometry(100, 100, 400, 300)

            # Create layout
            layout = QVBoxLayout()

            # Prompt input
            self.prompt_label = QLabel("Prompt:")
            self.prompt_input = QTextEdit(self)
            layout.addWidget(self.prompt_label)
            layout.addWidget(self.prompt_input)

            # Send button
            self.send_button = QPushButton("Send Request", self)
            self.send_button.clicked.connect(self.send_request)
            layout.addWidget(self.send_button)

            # Response output
            self.response_output = QTextEdit(self)
            self.response_output.setReadOnly(True)
            layout.addWidget(self.response_output)

            self.setLayout(layout)

        def send_request(self):
            url = "https://llm.x22.workers.dev/"
            prompt = self.prompt_input.toPlainText().strip()  # Strip whitespace

            # Prepare the JSON data
            data = json.dumps({
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            })
            headers = {'Content-Type': 'application/json'}

            try:
                # Send the POST request
                response = requests.post(url, headers=headers, data=data)

                # Check if the response is successful
                response.raise_for_status()  # Raise an error for bad responses

                # Extract the AI response from the JSON data
                ai_response = response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response")

                # Display the AI response
                self.response_output.setPlainText(ai_response)
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            except json.JSONDecodeError:
                QMessageBox.critical(self, "Error", "Failed to decode JSON response.")

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = CurlApp()
        window.show()
        sys.exit(app.exec_())
        """
second_code = """
from huggingface_hub import InferenceClient

client = InferenceClient(
    "meta-llama/Meta-Llama-3-8B-Instruct",
    token="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",
)

for message in client.chat_completion(
	messages=[{"role": "user", "content": "What is the capital of France?"}],
	max_tokens=500,
	stream=True,
):
    print(message.choices[0].delta.content, end="")

"""

# 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
This_Kod_PerT = """
ENDPOINT = https://api-inference.huggingface.co/models/<MODEL_ID>
import requests
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query("Can you please let us know more details about your ") """
Pro_plus_code = """

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox, QFileDialog
from huggingface_hub import InferenceClient
import OCR  # Import your OCR module

class LlamaAssistantGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Llama Assistant with PDF Support")
        self.setGeometry(100, 100, 600, 600)  # Increased size for better usability

        # Create layout
        layout = QVBoxLayout()

        # PDF file input
        self.pdf_label = QLabel("Select PDF File (optional):")
        self.pdf_input = QTextEdit(self)
        self.pdf_input.setReadOnly(True)
        layout.addWidget(self.pdf_label)
        layout.addWidget(self.pdf_input)

        # Browse button
        self.browse_button = QPushButton("Browse PDF", self)
        self.browse_button.clicked.connect(self.browse_pdf)
        layout.addWidget(self.browse_button)

        # User prompt input
        self.prompt_label = QLabel("Enter your prompt:")
        self.prompt_input = QTextEdit(self)
        layout.addWidget(self.prompt_label)
        layout.addWidget(self.prompt_input)

        # Send button
        self.send_button = QPushButton("Ask Jafar", self)
        self.send_button.clicked.connect(self.send_prompt)
        layout.addWidget(self.send_button)

        # Response output
        self.response_output = QTextEdit(self)
        self.response_output.setReadOnly(True)
        layout.addWidget(self.response_output)

        self.setLayout(layout)

        self.pdf_path = None  # Store the path of the selected PDF

    def browse_pdf(self):
        self.pdf_path, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")
        if self.pdf_path:
            self.pdf_input.setPlainText(self.pdf_path)

    def send_prompt(self):
        # Get the user input from the prompt text box
        user_prompt = self.prompt_input.toPlainText().strip()

        # Extract text from the selected PDF if a PDF is provided
        pdf_text = ""
        if self.pdf_path:
            pdf_text = OCR.extract_text_from_pdf(self.pdf_path)

            if not pdf_text:
                QMessageBox.warning(self, "Warning", "No text found in the PDF.")
                return

        # Combine the user prompt with the extracted PDF text if both are provided
        combined_prompt = user_prompt
        if pdf_text:
            combined_prompt += f"\n\n[Extracted from PDF]:\n{pdf_text}"

        # Ensure that there is input to process
        if not combined_prompt.strip():
            QMessageBox.warning(self, "Warning", "Please enter a prompt or select a PDF file.")
            return

        self.response_output.clear()
        self.send_button.setDisabled(True)

        try:
            client = InferenceClient(
                "meta-llama/Meta-Llama-3-8B-Instruct",
                token="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  # Replace with your actual token
            )

            # Send the combined prompt as input
            response_text = ""
            for message in client.chat_completion(
                messages=[
                    {"role": "system", "content": "You are a good and helpful assistant named Jafar."},
                    {"role": "user", "content": combined_prompt},
                ],
                max_tokens=500,
                stream=True,
            ):
                response_text += message.choices[0].delta.content
                QApplication.processEvents()  # Allow the GUI to update

            self.response_output.setPlainText(response_text)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
        finally:
            self.send_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LlamaAssistantGUI()
    window.show()
    sys.exit(app.exec_())
    """
