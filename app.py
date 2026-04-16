from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form2', methods=['GET', 'POST'])
def form2():
    if request.method == 'POST':
        email = request.form.get('email')
        parol = request.form.get('parol')
        return f"<h2>Kirish muvaffaqiyatli!</h2><p>Email: {email}</p><br><a href='/'>Orqaga</a>"
    return render_template('form2.html')

if __name__ == '__main__':
    app.run(debug=True)
