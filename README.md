# random-code-generator
timer on by verifying random code generator

<!doctype html>
<html>
<head>
  <title>Timer</title>
</head>
<body>

<h1>Hello User</h1>

<button onclick="code_generator()">Random Code</button>

<p>Generated code: <span id="showCode">---</span></p>

<input type="text" id="userCode" placeholder="Enter code"><br><br>

<button onclick="verify()">Verify</button>

<p id="result"></p>

<p id="timer">00:00</p>

<button onclick="start()">Start</button>

<script>
let code = null;
let isVerified = false;
let timer = null;
let count = 0;

function code_generator() {
  code = Math.floor(Math.random() * (4000 - 1000 + 1)) + 1000;
  document.getElementById("showCode").innerText = code;
}

function verify() {
  let user_input = document.getElementById("userCode").value;

  if (parseInt(user_input) === code) {
    document.getElementById("result").innerText = "Verified ✅";
    isVerified = true;
  } else {
    document.getElementById("result").innerText = "Invalid ❌";
    isVerified = false;
  }
}

function start() {
if (!isVerified) {
  alert("first verify the code!!");
  return;
    
}
if (timer) return;
  timer=setInterval(function() {
  count++;
  document.getElementById("timer").innerText=count;
    
},1000);
 
 
}
  


</script>

<hr><br><br>

</body>
</html>
