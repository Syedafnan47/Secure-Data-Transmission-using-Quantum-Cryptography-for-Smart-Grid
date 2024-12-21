from flask import Flask, redirect, render_template, request, session, url_for
import mysql.connector, random, string, os
import csv



app = Flask(__name__)
app.secret_key = "Qazwsx@123"  



link = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    password = '', 
    database = 'flaskquantumdb_2024'
)




@app.after_request
def add_header(response):
  
  response.cache_control.no_store = True
  return response




@app.route('/')
def index():
  
  return render_template('index.html')    




@app.route('/centrallogin', methods=['GET', 'POST'])
def centrallogin(): 
    
  if 'centraluser' in session:
    return redirect(url_for('upload'))

  if request.method == "GET":
    return render_template('centrallogin.html') 
    
  else:
    cursor = link.cursor()
    try: 
      email = request.form["email"]
      password = request.form["password"]
      cursor.execute("SELECT * FROM flaskquantumdb_2024_central WHERE email = %s AND password = %s", (email, password))
      user = cursor.fetchone()
      if user:
        session['centraluser'] = user[3]
        session['centralusername'] = user[2] 
        return redirect(url_for('upload'))
      else:
        return render_template('centrallogin.html', error='Invalid email or password') 
    
    except Exception as e:
      error = e
      return render_template('centrallogin.html', error=error)
      
    finally:
        cursor.close() 




@app.route('/centralregister', methods=['GET', 'POST'])
def centralregister():
      
  if 'centraluser' in session:
    return redirect(url_for('upload'))

  if request.method == "GET": 
    return render_template('centralregister.html') 
  
  else: 
    cursor = link.cursor()  
    try: 
      name = request.form["name"]
      email = request.form["email"]
      password = request.form["password"] 
      phone = request.form["phone"] 
      uid = 'uid_'+''.join(random.choices(string.ascii_letters + string.digits, k=10))
      cursor.execute("SELECT * FROM flaskquantumdb_2024_central WHERE email = %s", (email,))
      user = cursor.fetchone()
 
      if user:
        return render_template('centralregister.html', exists='Email already exists') 
      else:
        cursor.execute("INSERT INTO flaskquantumdb_2024_central (uid, name, email, password, phone) VALUES (%s, %s, %s, %s, %s)", (uid, name, email, password, phone))
        link.commit()
        return render_template('centralregister.html', success='Registration successful') 
       
    except Exception as e:
      error = e
      return render_template('centralregister.html', error=error)
      
    finally:
        cursor.close() 







@app.route('/arealogin', methods=['GET', 'POST'])
def arealogin(): 
    
  if 'areauser' in session:
    return redirect(url_for('viewarea'))

  if request.method == "GET":
    return render_template('arealogin.html') 
    
  else:
    cursor = link.cursor()
    try: 
      email = request.form["email"]
      password = request.form["password"]
      print("SELECT * FROM flaskquantumdb_2024_area WHERE email = %s AND password = %s", (email, password))
      cursor.execute("SELECT * FROM flaskquantumdb_2024_area WHERE email = %s AND password = %s", (email, password))
      user = cursor.fetchone()
      if user:
        session['areauser'] = user[3]
        session['areausername'] = user[2]  
        session['areauserone'] = user[6] 
        session['areausertwo'] = user[7] 
        return redirect(url_for('viewarea'))
      else:
        return render_template('arealogin.html', error='Invalid email or password') 
    
    except Exception as e:
      error = e
      return render_template('arealogin.html', error=error)
      
    finally:
        cursor.close() 




@app.route('/arearegister', methods=['GET', 'POST'])
def arearegister():
      
  if 'areauser' in session:
    return redirect(url_for('viewarea'))

  if request.method == "GET": 
    return render_template('arearegister.html') 
  
  else: 
    cursor = link.cursor()  
    try: 
      name = request.form["name"]
      email = request.form["email"]
      password = request.form["password"] 
      phone = request.form["phone"] 
      areaone = request.form["areaone"] 
      areatwo = request.form["areatwo"] 
      uid = 'uid_'+''.join(random.choices(string.ascii_letters + string.digits, k=10))
      cursor.execute("SELECT * FROM flaskquantumdb_2024_area WHERE email = %s", (email,))
      user = cursor.fetchone()
 
      if user:
        return render_template('arearegister.html', exists='Email already exists') 
      else:
        cursor.execute("INSERT INTO flaskquantumdb_2024_area (uid, name, email, password, phone, areaone, areatwo) VALUES (%s, %s, %s, %s, %s, %s, %s)", (uid, name, email, password, phone, areaone, areatwo))
        link.commit()
        return render_template('arearegister.html', success='Registration successful') 
       
    except Exception as e:
      error = e
      return render_template('arearegister.html', error=error)
      
    finally:
        cursor.close() 
    




@app.route('/viewarea')
def viewarea():
    
  if 'areauser' not in session:
    return redirect(url_for('arealogin'))
  
  cursor = link.cursor()
  try: 
    areaone = session.get('areauserone')
    areatwo = session.get('areausertwo')
    print(areaone)
    print(areatwo)
    sq_query="select * from flaskquantumdb_2024_detail where area = %s or area = %s limit 100"
    print(sq_query)
    cursor.execute(sq_query, (areaone, areatwo))
    data = cursor.fetchall() 
    return render_template('viewarea.html', data = data)
    
  except Exception as e:
    error = e
    return render_template('error.html', error=error)
      
  finally:
    cursor.close()      




@app.route('/consumption')
def consumption():
    
  if 'areauser' not in session:
    return redirect(url_for('arealogin'))
  
  cursor = link.cursor()
  try: 
    areaone = session.get('areauserone') 
    areatwo = session.get('areausertwo')
    sq_query="select dated, house, hospital, industry from flaskquantumdb_2024_detail where area = %s or area = %s group by dated limit 100"
    cursor.execute(sq_query, (areaone, areatwo))
    data = cursor.fetchall()
    return render_template('consumption.html', data = data)
    
  except Exception as e:
    error = e
    return render_template('error.html', error=error)
      
  finally:
    cursor.close()   
  





@app.route('/upload', methods=['GET', 'POST'])
def upload():

  if 'centraluser' not in session:
    return redirect(url_for('centrallogin'))
  
  if request.method == "GET": 
    return render_template('upload.html') 

  else:
    cursor = link.cursor()
    try: 
      file = request.files["file"] 
      filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '\\static\\docs', file.filename)
      file.save(filepath)
      
      insert_query = """INSERT INTO flaskquantumdb_2024_detail (id, area, house, hospital, company, industry, dated, central, centralname) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

      with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader: 
          values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], session.get('centraluser'),  session.get('centralusername'))
          cursor.execute(insert_query, values) 
          
      link.commit()   
      return render_template('upload.html', success='Upload successful', file=file) 
    
    except Exception as e:
      error = e
      return render_template('error.html', error=error)
      
    finally:
        cursor.close() 



@app.route('/viewdata')
def viewdata():
    
  if 'centraluser' not in session:
    return redirect(url_for('centrallogin'))
  
  cursor = link.cursor()
  try: 
    sq_query="select * from flaskquantumdb_2024_detail limit 100"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    return render_template('viewdata.html', data = data) 
    
  except Exception as e:
    error = e
    return render_template('error.html', error=error)
      
  finally:
    cursor.close()   
  


@app.route('/logout')
def logout():
    
    session.pop('centraluser', None)
    session.pop('centralusername', None)
    session.pop('areauser', None)
    session.pop('areausername', None)
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(debug=True)
