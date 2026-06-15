from flask import Flask, render_template_string, request
from datetime import datetime

app = Flask(__name__)

PASSWORD = "2806"
BIRTHDAY = datetime(2026, 8, 28, 0, 0)

lock_page = """
<!DOCTYPE html>
<html>
<head>
<title>Waiting for Sarina</title>
</head>

<body style="background:#0f0f1a;color:white;text-align:center;padding-top:100px;">

<h1>Waiting for Sarina</h1>

<h2 id="countdown"></h2>

<form method="POST">
  <input type="password" name="code" placeholder="Enter code">
  <br><br>
  <button type="submit">Unlock</button>
</form>

<p>{{ msg }}</p>

<script>
const birthday = new Date("2026-08-28T00:00:00");

function updateCountdown() {
  const now = new Date();
  const diff = birthday - now;

  if (diff <= 0) {
    document.getElementById("countdown").innerText = "It's time";
    autoUnlock();
    return;
  }

  const d = Math.floor(diff / (1000 * 60 * 60 * 24));
  const h = Math.floor((diff / (1000 * 60 * 60)) % 24);
  const m = Math.floor((diff / (1000 * 60)) % 60);
  const s = Math.floor((diff / 1000) % 60);

  document.getElementById("countdown").innerText =
    d + "d " + h + "h " + m + "m " + s + "s left";
}

async function autoUnlock() {
  const res = await fetch("/", {
    method: "POST",
    headers: {"Content-Type": "application/x-www-form-urlencoded"},
    body: "code=2806"
  });

  const html = await res.text();
  document.open();
  document.write(html);
  document.close();
}

setInterval(updateCountdown, 1000);
updateCountdown();
</script>

</body>
</html>
"""

birthday_page = """
<!DOCTYPE html>
<html>
<head>
<title>Birthday</title>

<link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">

<style>
body {
  margin: 0;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #ffffff;
  overflow: hidden;
  font-family: sans-serif;
}

body::before {
  content: "";
  position: absolute;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(255,192,203,0.25), transparent 70%);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  filter: blur(40px);
}

.container {
  text-align: center;
  max-width: 700px;
  opacity: 0;
  animation: fadeIn 2s ease forwards;
}

@keyframes fadeIn {
  to { opacity: 1; }
}

#text {
  color: #111;
  font-size: 20px;
  line-height: 1.8;
  white-space: pre-wrap;
}

.signature {
  margin-top: 20px;
  font-family: 'Dancing Script', cursive;
  font-size: 26px;
  color: #111;
  opacity: 0;
  animation: fadeIn 3s ease forwards;
  animation-delay: 6s;
}

.cursor {
  display: inline-block;
  width: 10px;
  background: #111;
  animation: blink 0.8s infinite;
}

@keyframes blink {
  50% { opacity: 0; }
}

.confetti {
  position: fixed;
  top: -10px;
  z-index: 9999;
  will-change: transform;
}
</style>
</head>

<body>

<audio autoplay loop>
  <source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8c8a9b6c3.mp3">
</audio>

<div class="container">
  <div id="text"></div><span class="cursor"></span>
  <div class="signature">- euri</div>
</div>

<script>
const message = `Dear " Jigar "
امیدوارم روزی که اینو میخونی بهترین روزت باشه و خوشحالترین باشی و بتونم یه بار دیگه اون لبخند خوشگلو روی لبات بیارم.
تو این مدت تو همه‌ی لحظه ها چه خوب و چه بد کنارم بودی حتی اگه حضور فیزیکی نداشتی یا کیلومتر ها از هم فاصله داشتیم و اگه ازم بپرسن وقتی برگردی به 23 September سال 2024 همین راهو میری یا نه بدون لحظه ای فکر کردن میگم اره. وجودت تو زندگیم بخشی از شکرگذاری صبح و شب منه و سلامتیت و شادی و موفقیتت چیزایین که هر روز برات میخوامشون و هر طور بتونم سعی میکنم ازت مراقبت کنم و خوشحال نگهت دارم و توی بهترین کارها تشویقت کنم . میخوام اینو بدونی که تو این مدت بهم ثابت شد که لیاقت بهترینارو داری و چقد قوی‌ای و تو همچی استعداد داری. امروز روز تولدته، روزی که هر سال باید ورود یکی از فرشته های خدا روی زمین و تو زندگی خیلیا از جمله من رو جشن گرفت. تو خوشگلترین و بامزه ترین و باحال ترین و مهربون ترین و ناز ترین و خوردنی ترین و دوست داشتنی ترین و باهوش ترین دختری هستی که تو زندگیم دیدم پس نباید برات عجیب باشه که انقدر دوستت دارم فرشته کوچولوی من.
وقت گذروندن باهات ، حرف زدن باهات ، دیدنت تو هر حالتی ، بغل کردنت ، گرفتن دستای ناز و خوشگلت ، بوس بوسی کردنت و حتی هیچکاری نکردن باهات از بهترین لحظات زندگیم بودن و هر بار به من حس زندگی میدن. خیلی میتونم حرف بزنم باهات راجب خوبیات یا راجب اینکه چقد دوستت دارم و اینارو همشو خودت حتی بهتر میدونی و تو این دو سال بهت ثابت شده و این متن هم هدفش این نبود ولی چیکار کنم انقد خوبی نمیشه ازت حرف نزد و وقتی بحث، بحثِ حرف زدن راجب خوبیای تو باشه من پرحرف ترینم. میخوام بدونی که چقد این روز برای من با ارزشه و همیشه به یادش هستم و برات بهترینارو ارزو میکنم، تولدت مبارک باشه جوجهه🐥💕
-euri;

let i = 0;

function typeWriter() {
  if (i < message.length) {
    document.getElementById("text").innerHTML += message.charAt(i);
    i++;
    setTimeout(typeWriter, 18);
  }
}

function spawnConfetti() {
  const colors = ["#ff4d6d", "#ffb703", "#8ecae6", "#cdb4db", "#80ed99", "#ffd6a5", "#ff8fab"];

  for (let i = 0; i < 140; i++) {
    let c = document.createElement("div");
    c.className = "confetti";

    const size = Math.random() * 8 + 4;

    c.style.left = Math.random() * window.innerWidth + "px";
    c.style.width = size + "px";
    c.style.height = size + "px";
    c.style.background = colors[Math.floor(Math.random() * colors.length)];

    const duration = Math.random() * 3 + 2;
    const drift = (Math.random() - 0.5) * 300;

    let start = performance.now();

    function animate(time) {
      let t = (time - start) / 1000;

      c.style.transform =
        translate(${drift * t}px, ${t * 250}px) rotate(${t * 360}deg)`;

      if (t < duration) {
        requestAnimationFrame(animate);
      } else {
        c.remove();
      }
    }

    document.body.appendChild(c);
    requestAnimationFrame(animate);
  }
}

window.onload = function () {
  const audio = document.querySelector("audio");
  audio.volume = 0.15;

  spawnConfetti();

  setTimeout(() => {
    typeWriter();
  }, 2500);
};
</script>

</body>
</html>
"""

def countdown():
    now = datetime.now()
    diff = BIRTHDAY - now
    if diff.total_seconds() <= 0:
        return "It's time"
    return f"{diff.days}d {diff.seconds//3600}h {(diff.seconds%3600)//60}m left"

@app.route("/", methods=["GET", "POST"])
def home():
    now = datetime.now()

    if request.method == "POST":
        if now >= BIRTHDAY and request.form.get("code") == PASSWORD:
            return render_template_string(birthday_page)

    return render_template_string(lock_page, countdown=countdown(), msg="")

if __name__ == "__main__":
    app.run(debug=True)