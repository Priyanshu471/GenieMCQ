from flask import Flask, request, jsonify
import PyPDF2  # Library to extract text from PDF
import json
from src.main import generate_evaluate_chain
from langchain.callbacks import get_openai_callback
from src.utils import read_file, format_response
import traceback

app = Flask(__name__)

print("Server is started successfully")

@app.route('/generate', methods=['POST'])
def process_pdf():
  if 'file' not in request.files:
    return jsonify({'error': 'No PDF file uploaded'}), 400

  input_file = request.files['file']
  filename = input_file.filename
  number = request.form.get('number')
  subject = request.form.get('subject')
  tone = request.form.get('hardness')
  
  # Check if required data is present
  if not input_file or not number or not subject or not tone:
    return jsonify({'error': 'Missing required data (number of questions, subject, or tone)'}), 400

  with open("response.json","r") as f:
    RESPONSE_JSON=json.load(f)
  # Call LLM
  try:
    text=read_file(input_file,filename)

    with get_openai_callback() as cb:
      response=generate_evaluate_chain(
        {
          "text": text,
          "number": number,
          "subject":subject,
          "tone": tone,
          "RESPONSE_JSON": json.dumps(RESPONSE_JSON)
        }
      )
    ques=format_response(response)
    return ques

  except Exception as e:
    traceback.print_exception(type(e), e, e.__traceback__)

  return jsonify({'questions': "Error in processing the response. Please try again."})
  # Return JSON response

if __name__ == '__main__':
  app.run(debug=True)
