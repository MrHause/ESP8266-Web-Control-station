from machine import Pin
led = Pin(15, Pin.OUT)
led1 = Pin(13, Pin.OUT)
def web_page(): 
    if led1.value()==1:
        gpio1_state="ON"
    else:
        gpio1_state="OFF"
    if led.value() == 1:
        gpio_state="ON"
    else:
        gpio_state="OFF"
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body{
                background-color:#333333;
                color:#f5f5f0;
            }
            #data{
                text-align:right;
                margin-right:5%;
            }
            
            
            #ledy{
                float:left;
                width:30%;
                margin-left:5%;
                font-size:16px;
            }
        
            .button {
                background-color: #ffdb4d;
                border: none;
                color: black;
                padding: 6px 12px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 14px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius:8px;
            }
            .button1{
                background-color: #4CAF50;
            }
            .button2{
                background-color:  #f44336;
            }
            .submit1{
                padding: 12px 20px;
                background-color:#f5f5f0;
                border-radius: 12px;
            }
            #serwomechanizm{
                float:left;
                width:35%;
                margin-left:5%;
                font-size:larger;
            }
            #odczyty{
                float:left;
                width:25%;
                font-size:larger;
            }
            #pojemnik{
                margin-top:20px;
            }
            #naglowek{
                width:100%;
                margin-bottom:20px;
            }
            input[type=text] {
                border: 2px solid black;
                padding: 12px 20px;
                border-radius: 12px;
                }
        </style>
    </head>
    <body onload="odliczanie();">
            
            <div id="data"><h2>Today is: <span id="CURRENTDAY"></span></h2></div>
            <div id="naglowek"><center><h1>METEO STATION WITH CONTROL PANEL</h1></center><br></div>
        <div id"pojemink">
            <div id="ledy">  
                <a href="/?led=on"> <button class="button button1">LED 1 ON</button></a>
                <a href="/?led=off"><button class="button button2">LED 1 OFF</button></a>
                LED 1 State is : """+gpio_state+"""<span id="LEDState">NA</span><br>
                <button class="button button1" onclick="LED2(1)">LED 2 ON</button>
                <button class="button button2" onclick="LED2(0)">LED 2 OFF</button>
                LED 2 State is :"""+gpio1_state+""" <span id="LED2State">NA</span><br>
            </div>
            <div id="serwomechanizm">
                Set servo angle (0-180): <br>
                <div>
                    <input type="text" id="pole" />
                    <button class="submit submit1" onclick="sendServo()">SET</button><br>
                </div>
            </div>
            <div id="odczyty">
                <table>
                    <tr><td>Temparute is :</td><td><span id="TEMPValue">0</span>C</td></tr>
                    <tr><td>Humidity is :</td><td><span id="HUMValue">0</span>%</td></tr>
                    <tr><td>ADC value is :</td><td> <span id="ADCValue">0</span>V</td></tr>
                </table>
                
                
            </div>
            <div style="clear:both;"></div>
        </div>
        <script>
            function odliczanie(){
            var today = new Date();
            var day = today.getDate();
            var month = today.getMonth()+1;
            var year = today.getFullYear();
            var hour = today.getHours();
            var minute = today.getMinutes();
            var second = today.getSeconds();
            

            document.getElementById("CURRENTDAY").innerHTML = day+"/"+month+"/"+year+" | "+hour+":"+minute+";"+second;
            setTimeout("odliczanie()",1000);
            }
            function LED(led) {
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/?led="+led, false);
            xhttp.send();
            }
            function LED2(led) {
            var xhttp = new XMLHttpRequest();
              xhttp.onreadystatechange = function() {
              if (this.readyState == 4 && this.status == 200) {
                document.getElementById("LED2State").innerHTML =
                this.responseText;
              }
            };
            xhttp.open("GET", "/?led1="+led, false);
            xhttp.send();
            }
        </script>
    </body>
    </html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  led1_on = request.find('/?led1=1')
  led1_off = request.find('/?led1=0')
  if led_on == 6:
    led.value(1)
  if led_off == 6:
    led.value(0)
  if led1_on == 6:
    led1.value(1)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/plane\n')
    conn.send('ON')
  if led1_off == 6:
    led1.value(0)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/plane\n')
    conn.send('OFF')
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
