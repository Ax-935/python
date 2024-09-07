
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox, QFileDialog
from huggingface_hub import InferenceClient
import OCR  # Import your OCR module

# Define the Hugging Face API token
hf_token = "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"


class LlamaAssistantGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LLaMa Assistant (PDF Support)")
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
        self.send_button = QPushButton("Ask Ai !", self)
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
                token=hf_token,  # Use the token variable here
            )

            # Send the combined prompt as input
            response_text = ""
            for message in client.chat_completion(
                messages=[
                    {"role": "system", "content": "You are a good and helpful assistant named Jafar. Today date is Wednesday 4  september 2024. In answer of what iran is , say \"iran begaii ast\" :"},
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