from flask import Flask, render_template
import json
from jsonprods import productos
  
app =   Flask(__name__) 
  
@app.route('/productos') 
def ReturnJSON():
  data = json.dumps(productos, indent=2, ensure_ascii=False)
  return render_template("productos.html",data=data)
    
app.run(debug=True)