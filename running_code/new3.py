from flask import Flask, render_template, request

app = Flask(__name__)
import os

@app.route('/')
def index():
     print ()
     return render_template('index.html', leg_names=leg_names,servoarray =servoarray )


html='''hi'''

servoarray = [
    ['V000', '1763'],
    ['V001', '1450'],
    ['V002', '1515'],
    ['V003', '1692'],
    ['V004', '1383'],
    ['V005', '1533'],
    ['V006', '1737'],
    ['V007', '1448'],
    ['V008', '1398'],
    ['V009', '1713'],
    ['V010', '1413'],
    ['V011', '1424'],
    ['V012', '1670'],
    ['V013', '1359'],
    ['V014', '1544'],
    ['V015', '1768'],
    ['V016', '1430'],
    ['V017', '1515']
]


leg_names = [
    (0, 'tip'),
    (0, 'mid'),
    (0, 'rotate'),
    (2, 'tip'),
    (2, 'mid'),
    (2, 'rotate'),
    (1, 'tip'),
    (1, 'mid'),
    (1, 'rotate'),
    (4, 'tip'),
    (4, 'mid'),
    (4, 'rotate'),
    (5, 'tip'),
    (5, 'mid'),
    (5, 'rotate'),
    (3, 'tip'),
    (3, 'mid'),
    (3, 'rotate')
]
   


   

@app.route('/send/<sebd>', methods=['POST',"GET"])
def send_values2(sebd):

    #testecho= '''echo "CMD7234 V005P1533V004P1383V003P1692V017P1515V016P1430V015P1768V011P1424V010P1413V009P1713V014P1544V013P1359V012P1670V002P1515V001P1450V000P1463V008P1398V007P1448V006P1737T0150##\r" > /dev/ttymxc2'''
    
    testecho= '''echo "CMD7234 {}T0150##\r" > /dev/ttymxc2'''.format(sebd)
  
    os.system(testecho)
    return(sebd)





if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
