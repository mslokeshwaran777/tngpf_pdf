from flask import Flask, request, send_file
import requests
import io

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Website'


@app.route('/get_pdf', methods=['GET'])
def get_pdf():

    suf = request.args.get('suf')
    gpfno = request.args.get('gpfno')
    year = request.args.get('year')

    if not suf or not gpfno or not year:
       return 'Missing one or more parameters', 400

    print(suf)

    url = 'https://agae.tn.nic.in/TNGPF_Reports/loginnew.aspx?Flag=A&EmpDeptcode={}&EmpgpfNo={}&ASlipYear={}'.format(suf, gpfno, year)
    res = requests.get(url)
    pdf_content = res.content
    return send_file(io.BytesIO(pdf_content), as_attachment=True, download_name='output.pdf', mimetype='application/pdf')
