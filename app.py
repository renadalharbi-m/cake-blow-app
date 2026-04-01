import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Cake Blow 🎂", layout="centered")

# تحويل الصورة إلى Base64
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
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
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

        /* Footer ثابت أسفل الصفحة على اليسار */
        #footer {{
            position: fixed;
            left: 10px;
            bottom: 5px;
            font-size: 12px;
            color: #888888;
            font-weight: normal;
        }}
    </style>
    </head>
    <body>

        <h2> Happy Birthday Joey  </h2>
        <div id="cake"></div>
        <p>Click on the cake to place candles</p>
        <p>Then blow into your mic 😘</p>
        <p id="counter">Candles: 0</p>

        <!-- Confetti library -->
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

                        // عند نفخ كل الشموع اطلق confetti
                        if(current === 0) {{
                            confetti({{
                                particleCount: 150,
                                spread: 100,
                                origin: {{ y: 0.6 }}
                            }});
                        }}
                    }}, 500);
                }}, index * 100);
            }});
        }}

        // Microphone detection
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

        <!-- Footer -->
        <p id="footer">Made with ❤️ Renad</p>

    </body>
    </html>
    """,
    height=650,
)
