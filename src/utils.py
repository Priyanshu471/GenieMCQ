import os
import PyPDF2
import json
import traceback
from flask import jsonify

def read_file(file, filename):
    print("The file name is: ", file)
    if "pdf" in filename:
        try:
            pdf_reader=PyPDF2.PdfReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
            
        except Exception as e:
            raise Exception("error reading the PDF file")
        
    elif "txt" in filename:
        return file.read().decode("utf-8")
    
    else:
        raise Exception("unsupported file format only pdf and text file suppoted")

def format_response(response):
    quiz = response.get("mcq").strip()
    quiz = quiz.replace('### RESPONSE_JSON\n', '')
    quiz_json = json.loads(quiz)
    questions = quiz_json["questions"]
    answers = quiz_json["answers"]
    
    return jsonify({"answers": answers,"questions": questions});