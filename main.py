from flask import Flask,render_template,request
from Operasi import *
import random

app = Flask(__name__)

@ app.route('/')
def home():
    return render_template('index.html')

@ app.route('/suit', methods = ['GET','POST'])
def suit():
    button_id = request.form.get('button_id')
    if request.method == "POST":
        robot = str(random.randint(1,3))
        output_suit = Suit_Game(button_id,robot)
        return render_template('suit.html',output = output_suit, output_player = convert_Suit(button_id), output_robot = convert_Suit(robot))
    return render_template('suit.html',output = None)

@ app.route('/suhu', methods = ['GET','POST'])
def suhu():
    input_id = request.form.get('select_id1')
    output_id = request.form.get('select_id2')
    
    if request.method == "POST":
        num_id = validate(request.form['Num_Input'])
        return render_template("suhu.html", output = convensi_suhu(output_id,input_id,num_id), last = output_id, input = num_id, first = input_id)
    return render_template("suhu.html", output = None)

@ app.route('/life', methods = ['GET','POST'])
def life():
    gander = request.form.get('select_id')
    if request.method == "POST":
        age = validate_age(request.form['age'])
        hight = validate_tall(request.form['hight'])
        weight = validate_weight(request.form['weight'])
        
        if age == False or hight == False or weight == False:
            return  render_template("life.html",output_Category = None, eror = 'True')
        else:
            calori = Calori(age,gander,weight)
            ideal = ideal_body(gander,hight)
            imt = IMT(weight,hight)
            categori = Category(imt)
            return render_template("life.html",output_Category = categori, output_imt = imt, output_calori = calori, output_hight = hight, output_weight = weight, output_age = age, output_ideal = ideal, eror = None)

    return render_template("life.html",output_Category = None, eror = None)

@app.route('/binary',methods = ['GET','POST'])
def binary():
    first_id = request.form.get('select_id1')
    last_id = request.form.get('select_id2')
    if request.method == "POST":
        num_id = request.form['Num_Input']
        if verivication(num_id,first_id):
            return render_template("Binary.html", output = Binary_Calc(num_id,first_id,last_id), first = first_id, last = last_id, input = num_id, eror = None,)
        else:
            return render_template("binary.html", output = None, eror = 'eror')
    return render_template("binary.html", output = None, eror = None)

@app.route('/matrix',methods = ['GET','POST'])
def matrix():
    
    Button_type = request.form.get('type_button')
    
    if request.method == "POST":   
            
        a1 =validate_matrix( request.form.get('a1'))
        a2 =validate_matrix( request.form.get('a2'))
        a3 =validate_matrix( request.form.get('a3'))
        a4 =validate_matrix( request.form.get('a4'))
        
        b1 =validate_matrix( request.form.get('b1'))
        b2 =validate_matrix( request.form.get('b2'))
        b3 =validate_matrix( request.form.get('b3'))
        b4 =validate_matrix( request.form.get('b4'))
        
        c1 =validate_matrix( request.form.get('c1'))
        c2 =validate_matrix( request.form.get('c2'))
        c3 =validate_matrix( request.form.get('c3'))
        c4 =validate_matrix( request.form.get('c4'))
        
        d1 =validate_matrix( request.form.get('d1'))
        d2 =validate_matrix( request.form.get('d2'))
        d3 =validate_matrix( request.form.get('d3'))
        d4 =validate_matrix( request.form.get('d4'))
        
        if Button_type == 'dimension_2':
            return render_template('matrix.html', output_rank = None, output_determinant = None, dimensi = '2')
        elif Button_type == 'dimension_3':
            return render_template('matrix.html', output_rank = None, output_determinant = None, dimensi = '3')
        elif Button_type == 'dimension_4':
            return render_template('matrix.html', output_rank = None, output_determinant = None, dimensi = '4')
        
        elif Button_type == 'rank_2':
            return render_template('matrix.html',output_rank = rank2(a1,a2,b1,b2), output_determinant = None, dimensi = '2', a1=a1, a2=a2, b1=b1, b2=b2)
        elif Button_type == 'rank_3':
            return render_template('matrix.html',output_rank = rank3(a1,a2,a3,b1,b2,b3,c1,c2,c3), output_determinant = None, dimensi = '3', a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3)
        elif Button_type == 'rank_4':
            return render_template('matrix.html',output_rank = rank4(a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4,d1,d2,d3,d4), output_determinant = None, dimensi = '4', a1=a1, a2=a2, a3=a3, a4=a4, b1=b1, b2=b2, b3=b3, b4=b4, c1=c1, c2=c2, c3=c3, c4=c4, d1=d1, d2=d2, d3=d3, d4=d4)
        
        elif Button_type == 'determinant_2':
            return render_template('matrix.html',output_rank = None, output_determinant = determinant2(a1,a2,b1,b2), dimensi = '2', a1=a1, a2=a2, b1=b1, b2=b2)
        elif Button_type == 'determinant_3':
            return render_template('matrix.html',output_rank = None, output_determinant = determinant3(a1,a2,a3,b1,b2,b3,c1,c2,c3), dimensi = '3', a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3)
        elif Button_type == 'determinant_4':
            return render_template('matrix.html',output_rank = None, output_determinant = determinant4(a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4,d1,d2,d3,d4), dimensi = '4', a1=a1, a2=a2, a3=a3, a4=a4, b1=b1, b2=b2, b3=b3, b4=b4, c1=c1, c2=c2, c3=c3, c4=c4, d1=d1, d2=d2, d3=d3, d4=d4)
            
    return render_template('matrix.html', output_rank = None, output_determinant = None, dimensi = '2')

if __name__ == "__main__":
    app.run()