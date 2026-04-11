import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="HBD JOEY", layout="centered")

with open("cake.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

cake_data_url = f"data:image/png;base64,{encoded_string}"

components.html(
f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
  background: #fff0f4;
  font-family: Arial;
  text-align: center;
}}

#cake {{
  width: 420px;
  height: 300px;
  background-image: url("{cake_data_url}");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  margin: auto;
  position: relative;
  cursor: pointer;
}}

.candle {{
  width: 8px;
  height: 40px;
  background: #ffd966;
  position: absolute;
}}

.flame {{
  width: 12px;
  height: 18px;
  background: orange;
  border-radius: 50%;
  position: absolute;
  top: -16px;
  left: -2px;
  animation: flicker 0.15s infinite alternate;
}}

@keyframes flicker {{
  from {{ transform: scale(1); }}
  to {{ transform: scale(0.85); }}
}}

#counter {{
  margin-top: 10px;
}}

/* ✉️ الظرف */
#envelope {{
  position: fixed;
  bottom: -200px;
  left: 50%;
  transform: translateX(-50%);
  width: 260px;
  height: 160px;
  perspective: 1000px;
  transition: bottom 1s ease;
}}

#envelope.show {{
  bottom: 120px;
}}

.envelope-body {{
  width: 100%;
  height: 100%;
  background: #fff;
  border: 2px solid #e91e63;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
}}

.envelope-flap {{
  position: absolute;
  width: 100%;
  height: 50%;
  background: #e91e63;
  clip-path: polygon(0 0, 50% 100%, 100% 0);
  transform-origin: top;
  transition: transform 0.8s;
  z-index: 2;
}}

#envelope.open .envelope-flap {{
  transform: rotateX(180deg);
}}

.letter {{
  position: absolute;
  width: 90%;
  height: 120%;
  background: #fff0f4;
  left: 5%;
  top: 100%;
  padding: 15px;
  font-size: 14px;
  color: #e91e63;
  border-radius: 6px;
  transition: top 0.8s ease;
}}

#envelope.open .letter {{
  top: 10%;
}}

#footer {{
  position: fixed;
  bottom: 5px;
  left: 10px;
  font-size: 12px;
  color: gray;
}}
</style>
</head>

<body>

<h2> Happy Birthday Joey 😘 </h2>
<p>Click on the cake then blow </p>

<div id="cake"></div>
<p id="counter">Candles: 0</p>

<div id="envelope">
  <div class="envelope-body">
    <div class="envelope-flap"></div>
    <div class="letter">
      Have a great year schatje ;) <br><br>
      sending kisses from far away<br><br>
       💋💋💋
    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

<script>
const cake = document.getElementById("cake");
const counter = document.getElementById("counter");

let current = 0;

function addCandle(x,y) {{
  const candle = document.createElement("div");
  candle.className = "candle";
  candle.style.left = x + "px";
  candle.style.top = y + "px";

  const flame = document.createElement("div");
  flame.className = "flame";

  candle.appendChild(flame);
  cake.appendChild(candle);

  current++;
  counter.innerText = "Candles: " + current;
}}

cake.onclick = function(e) {{
  const rect = cake.getBoundingClientRect();
  addCandle(e.clientX - rect.left, e.clientY - rect.top);
}};

function blowCandles() {{
  document.querySelectorAll(".flame").forEach(function(f) {{
    f.remove();
  }});

  current = 0;
  counter.innerText = "Candles: 0";

  confetti({{
    particleCount: 150,
    spread: 100
  }});

  const env = document.getElementById("envelope");

  env.classList.add("show");

  setTimeout(function() {{
    env.classList.add("open");
  }}, 1000);
}}

navigator.mediaDevices.getUserMedia({{audio:true}})
.then(function(stream) {{
  const ctx = new AudioContext();
  const mic = ctx.createMediaStreamSource(stream);
  const analyser = ctx.createAnalyser();

  mic.connect(analyser);

  const data = new Uint8Array(analyser.frequencyBinCount);

  function detect() {{
    analyser.getByteFrequencyData(data);
    let avg = data.reduce((a,b)=>a+b)/data.length;

    if(avg > 30) {{
      blowCandles();
    }}

    requestAnimationFrame(detect);
  }}

  detect();
}});
</script>

<p id="footer">Made with ❤️ renad</p>

</body>
</html>
""",
height=700
)
