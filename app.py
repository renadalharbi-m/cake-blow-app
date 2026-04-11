import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="HBD JOEY ", layout="centered")

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

/* ✉️ ظرف حقيقي */
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

/* الغطاء */
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

/* الرسالة */
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

<h2> Happy Birthday Joey 🎉 </h2>
<p>Click on the cake then blow 🎤</p>

<div id="cake"></div>
<p id="counter">Candles: 0</p>

<!-- ✉️ الظرف -->
<div id="envelope">
  <div class="envelope-body">
    <div class="envelope-flap"></div>
    <div class="letter">
      Have a great year schatje 💋<br><br>
      sending kisses from far away 💋💋💋
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

cake.onclick = (e) => {{
  const rect = cake.getBoundingClientRect();
  addCandle(e.clientX - rect.left, e.clientY - rect.top);
}}

function blowCandles() {{
  document.querySelectorAll(".flame").forEach(f => f.remove());
  current = 0;
  counter.innerText = "Candles: 0";

  confetti({{particleCount:150,spread:100}});

  const env = document.getElementById("envelope");

  // يطلع الظرف
  env.classList.add("show");

  // بعدين ينفتح
  setTimeout(()=> {{
    env.classList.add("open");
  }}, 1000);
}}

navigator.mediaDevices.getUserMedia({{audio:true}})
.then(stream => {{
  const ctx = new AudioContext();
  const mic = ctx.createMediaStreamSource(stream);
  const analyser = ctx.createAnalyser();

  mic.connect(analyser);

  const data = new Uint8Array(analyser.frequencyBinCount);

  function detect() {{
    analyser.getByteFrequencyData(data);
    let avg = data.reduce((a,b)=>a+b)/data.length;

    if(avg > 30) blowCandles();

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
)}}

.candle {{
  width: 8px;
  height: 40px;
  background: #ffd966;
  position: absolute;
  border-radius: 2px;
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
  font-size: 16px;
  margin-top: 10px;
}}

#footer {{
  position: fixed;
  left: 10px;
  bottom: 5px;
  font-size: 12px;
  color: #888888;
}}

/* ✉️ الظرف */
#envelope {{
  position: fixed;
  bottom: 120px;
  left: 50%;
  transform: translateX(-50%);
  width: 220px;
  height: 140px;
  background: #fff;
  border: 2px solid #e91e63;
  border-radius: 10px;
  display: none;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}}

#envelope::before {{
  content: "";
  position: absolute;
  top: 0;
  width: 100%;
  height: 50%;
  background: #e91e63;
  clip-path: polygon(0 0, 50% 100%, 100% 0);
  transform-origin: top;
  transition: transform 0.6s;
}}

#envelope.open::before {{
  transform: rotateX(180deg);
}}

#letter {{
  padding: 15px;
  font-size: 13px;
  color: #e91e63;
  opacity: 0;
  transition: opacity 0.5s 0.5s;
}}

#envelope.open #letter {{
  opacity: 1;
}}

</style>
</head>

<body>

<h2> Happy Birthday Joey 🎉 </h2>
<p>Click on the cake to place candles, then blow into your mic 😘</p>

<div id="cake"></div>
<p id="counter">Candles: 0</p>

<!-- الظرف -->
<div id="envelope">
  <div id="letter">
    Have a great year schatje 💋<br>
    sending kisses from far away 💋💋💋
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

<script>
const cake = document.getElementById("cake");
const counter = document.getElementById("counter");

let current = 0;
const maxCandles = 31;

function addCandle(x, y) {{
  if (current >= maxCandles) return;

  const candle = document.createElement("div");
  candle.className = "candle";
  candle.style.left = x - 4 + "px";
  candle.style.top = y - 40 + "px";

  const flame = document.createElement("div");
  flame.className = "flame";

  candle.appendChild(flame);
  cake.appendChild(candle);

  current++;
  counter.innerText = "Candles: " + current;
}}

cake.addEventListener("click", function(event) {{
  const rect = cake.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;
  addCandle(x, y);
}});

function blowCandles() {{
  const flames = document.querySelectorAll(".flame");

  flames.forEach((f, index) => {{
    setTimeout(() => {{
      f.style.transition = "transform 0.5s, opacity 0.5s";
      f.style.transform = "scale(0)";
      f.style.opacity = "0";

      setTimeout(() => {{
        f.style.display = "none";
        current--;
        counter.innerText = "Candles: " + current;

        if(current === 0) {{
          confetti({{
            particleCount: 150,
            spread: 100,
            origin: {{ y: 0.6 }}
          }});

          // ✉️ إظهار الظرف
          const envelope = document.getElementById("envelope");
          envelope.style.display = "block";

          setTimeout(() => {{
            envelope.classList.add("open");
          }}, 200);
        }}

      }}, 500);
    }}, index * 100);
  }});
}}

navigator.mediaDevices.getUserMedia({{ audio: true, video: false }})
.then(stream => {{
  const audioContext = new (window.AudioContext || window.webkitAudioContext)();
  const source = audioContext.createMediaStreamSource(stream);
  const analyser = audioContext.createAnalyser();

  source.connect(analyser);
  analyser.fftSize = 512;

  const dataArray = new Uint8Array(analyser.frequencyBinCount);

  function detectBlow() {{
    analyser.getByteFrequencyData(dataArray);
    let sum = dataArray.reduce((a,b)=>a+b,0);
    let avg = sum / dataArray.length;

    if(avg > 30) {{
      blowCandles();
    }}

    requestAnimationFrame(detectBlow);
  }}

  detectBlow();
}})
.catch(err => {{
  console.log("Microphone access denied", err);
}});
</script>

<p id="footer">Made with ❤️ renad</p>

</body>
</html>
""",
height=700,
)
