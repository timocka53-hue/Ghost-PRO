import flet as ft
import time

def main(page: ft.Page):
    page.title = "GHOST PRO V6 ULTIMATE"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#000000"
    
    # Полный код системы со всеми функциями
    full_ghost_os = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
        <style>
            body, html { margin: 0; padding: 0; background: #000; color: #00FF00; font-family: 'Courier New', monospace; height: 100%; overflow: hidden; }
            canvas { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.5; }
            .ghost-card { border: 1px solid #00FF00; background: rgba(0, 15, 0, 0.95); box-shadow: 0 0 25px #00FF00; padding: 25px; }
            .screen { display: none; height: 100vh; flex-direction: column; padding: 20px; z-index: 10; position: relative; box-sizing: border-box; }
            .active { display: flex; }
            input, textarea { background: rgba(0,0,0,0.8); border: 1px solid #00FF00; color: #00FF00; padding: 12px; outline: none; width: 100%; }
            .btn { border: 1px solid #00FF00; padding: 12px; text-align: center; cursor: pointer; font-weight: bold; text-transform: uppercase; transition: 0.3s; background: rgba(0,30,0,0.6); }
            .btn:active { background: #00FF00; color: #000; box-shadow: 0 0 40px #00FF00; }
            .admin-border { border-color: #ff0000 !important; color: #ff0000 !important; }
            .msg { margin-bottom: 12px; border-left: 3px solid #00FF00; padding-left: 10px; background: rgba(0, 255, 0, 0.05); }
            .avatar-main { width: 100px; height: 100px; border-radius: 50%; border: 2px solid #00FF00; object-fit: cover; box-shadow: 0 0 15px #00FF00; }
            .glitch { animation: glitch 1.5s infinite; }
            @keyframes glitch { 0% { transform: skew(0); } 20% { transform: skew(3deg); opacity: 0.8; } 40% { transform: skew(-3deg); } 100% { transform: skew(0); } }
        </style>
    </head>
    <body>
        <canvas id="matrix"></canvas>

        <div id="auth-screen" class="screen active justify-center items-center">
            <div class="ghost-card w-full max-w-sm space-y-5">
                <h1 class="text-3xl text-center font-bold glitch tracking-[8px]">GHOST_PRO</h1>
                <input type="email" id="email" placeholder="IDENTITY_EMAIL">
                <input type="password" id="pass" placeholder="ACCESS_KEY">
                <div class="btn" onclick="runAuth()">INITIALIZE_CONNECTION</div>
                <p class="text-[9px] text-center opacity-40">PROTOCOL: AES-256-GCM | NODE: ENCRYPTED</p>
            </div>
        </div>

        <div id="main-screen" class="screen">
            <div class="flex justify-between items-center border-b border-green-500 pb-2 mb-3">
                <span id="node-id" class="text-xs font-bold">NODE: GUEST</span>
                <div class="flex space-x-3">
                    <span id="admin-indicator" class="hidden text-red-500 font-bold animate-pulse text-xs">[ADMIN_MODE]</span>
                    <span onclick="nav('profile-screen')" class="text-xs underline cursor-pointer">/IDENTITY/</span>
                </div>
            </div>

            <div class="relative mb-3">
                <input type="text" id="search" placeholder="SEARCH_BY_UID (@ghost_...)" class="h-10 text-xs pl-10">
                <span class="absolute left-3 top-2.5 opacity-50">🔎</span>
            </div>

            <div id="chat-flow" class="flex-1 overflow-y-auto p-3 border border-green-900 bg-black/70 mb-3 space-y-3">
                <div class="text-[10px] text-center opacity-30 italic">--- SECURE CHANNEL INITIALIZED ---</div>
            </div>

            <div id="admin-console" class="hidden mb-3 grid grid-cols-2 gap-2">
                <div class="btn admin-border text-[10px] py-1" onclick="nav('admin-panel')">OPEN_CORE_CONTROL</div>
                <div class="btn admin-border text-[10px] py-1" onclick="alert('GLOBAL_BROADCAST_READY')">BROADCAST</div>
            </div>

            <div class="flex items-center space-x-2">
                <button onclick="action('mic')" class="btn px-4 py-2">🎤</button>
                <button onclick="action('cam')" class="btn px-4 py-2">🎥</button>
                <button onclick="document.getElementById('img-up').click()" class="btn px-4 py-2">🖼️</button>
                <input type="file" id="img-up" class="hidden" onchange="action('img')">
                <input type="text" id="msg-input" placeholder="Enter encrypted payload..." class="flex-1 h-11">
                <button onclick="sendMessage()" class="btn px-6 py-2">></button>
            </div>
        </div>

        <div id="admin-panel" class="screen">
            <div class="border-b border-red-600 pb-2 mb-4 flex justify-between">
                <h2 class="text-red-600 font-bold">CORE_ADMIN_PANEL</h2>
                <button onclick="nav('main-screen')" class="text-xs">CLOSE</button>
            </div>
            <div class="grid grid-cols-2 gap-3 mb-6">
                <div class="btn admin-border text-xs" onclick="alert('SEARCHING ALL NODES...')">BAN_USER</div>
                <div class="btn admin-border text-xs" onclick="alert('FREEZING NETWORK...')">FREEZE_ID</div>
                <div class="btn admin-border text-xs" onclick="alert('DELETING LOGS...')">WIPE_DATA</div>
                <div class="btn admin-border text-xs" onclick="alert('PROTOCOL CHANGED')">REGEN_KEYS</div>
            </div>
            <p class="text-xs text-red-500 mb-2">INCOMING_TICKETS:</p>
            <div id="admin-tickets" class="flex-1 overflow-y-auto space-y-2">
                <div class="ghost-card p-3 border-red-900 flex justify-between items-center" onclick="openChat('@user_777')">
                    <div class="text-[11px]">FROM: @user_777<br><span class="opacity-50 italic">"Security breach detected..."</span></div>
                    <div class="btn admin-border py-1 px-3 text-[10px]">OPEN</div>
                </div>
            </div>
        </div>

        <div id="profile-screen" class="screen items-center space-y-6">
            <h2 class="text-2xl font-bold tracking-widest">SYSTEM_ID</h2>
            <div class="relative">
                <img id="my-avatar" src="https://api.dicebear.com/7.x/bottts/svg?seed=Ghost" class="avatar-main">
                <input type="file" id="av-change" class="hidden" onchange="updateAvatar(event)">
                <button onclick="document.getElementById('av-change').click()" class="absolute bottom-0 right-0 bg-green-500 text-black px-2 py-1 text-[10px] font-bold">EDIT</button>
            </div>
            <input type="text" id="uid-input" placeholder="SET_UNIQUE_UID" class="text-center text-xl font-bold">
            <div class="w-full space-y-3">
                <button onclick="nav('support-screen')" class="w-full btn">CONTACT_ADMIN</button>
                <button onclick="nav('main-screen')" class="w-full btn opacity-50">RETURN_TO_NET</button>
            </div>
        </div>

        <div id="support-screen" class="screen">
            <h2 class="text-xl mb-4 border-b border-green-500 pb-2">SECURE_SUPPORT_LINE</h2>
            <div id="sup-chat" class="flex-1 overflow-y-auto p-3 mb-4 space-y-2">
                <div class="msg text-xs"><span class="text-red-500 font-bold">[SYS]:</span> Describe your issue. Ticket will be created.</div>
            </div>
            <div class="flex space-x-2">
                <input type="text" id="sup-msg" placeholder="Message to admin..." class="flex-1">
                <button onclick="sendTicket()" class="btn px-6">SEND</button>
            </div>
        </div>

        <script>
            let isAdmin = false;
            let currentUID = "@guest";
            const AES_KEY = "ghost_secret_2026";

            // Matrix Rain
            const canvas = document.getElementById('matrix');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth; canvas.height = window.innerHeight;
            const chars = "77701GHOSTPRO";
            const fontSize = 16;
            const columns = canvas.width/fontSize;
            const drops = Array(Math.floor(columns)).fill(1);
            function draw() {
                ctx.fillStyle = "rgba(0,0,0,0.05)"; ctx.fillRect(0,0,canvas.width,canvas.height);
                ctx.fillStyle = "#0F0"; ctx.font = fontSize+"px monospace";
                drops.forEach((y, i) => {
                    ctx.fillText(chars[Math.floor(Math.random()*chars.length)], i*fontSize, y*fontSize);
                    if(y*fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
                    drops[i]++;
                });
            }
            setInterval(draw, 35);

            function nav(id) {
                document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
                document.getElementById(id).classList.add('active');
            }

            function runAuth() {
                const e = document.getElementById('email').value;
                const p = document.getElementById('pass').value;
                if(e === "adminpan" && p === "TimaIssam2026") {
                    isAdmin = true;
                    currentUID = "@ADMIN_PRO";
                    document.getElementById('node-id').innerText = "NODE: MASTER_ADMIN";
                    document.getElementById('node-id').style.color = "#ff0000";
                    document.getElementById('admin-indicator').classList.remove('hidden');
                    document.getElementById('admin-console').classList.remove('hidden');
                    nav('main-screen');
                } else {
                    currentUID = "@" + (e.split('@')[0] || "ghost");
                    nav('main-screen');
                }
                document.getElementById('uid-input').value = currentUID;
            }

            function sendMessage() {
                const inp = document.getElementById('msg-input');
                if(!inp.value) return;
                const encrypted = CryptoJS.AES.encrypt(inp.value, AES_KEY).toString();
                console.log("SENDING_ENCRYPTED:", encrypted);
                
                const box = document.getElementById('chat-flow');
                box.innerHTML += `<div class="msg"><span class="text-blue-400 font-bold">${currentUID}:</span><br>${inp.value}</div>`;
                inp.value = "";
                box.scrollTop = 99999;
            }

            function action(type) {
                alert("INITIALIZING " + type.toUpperCase() + " MODULE...");
            }

            function sendTicket() {
                const val = document.getElementById('sup-msg').value;
                if(!val) return;
                document.getElementById('sup-chat').innerHTML += `<div class="msg text-xs"><span class="text-blue-500 font-bold">YOU:</span><br>${val}</div>`;
                document.getElementById('sup-msg').value = "";
                alert("TICKET_CREATED: Admin notified.");
            }

            function updateAvatar(event) {
                const r = new FileReader();
                r.onload = () => document.getElementById('my-avatar').src = r.result;
                r.readAsDataURL(event.target.files[0]);
            }

            function openChat(uid) {
                alert("OPENING TERMINAL WITH " + uid);
                nav('main-screen');
            }
        </script>
    </body>
    </html>
    """

    # Ультра-безопасная загрузка
    time.sleep(1) # Даем Android время подготовить WebView
    
    wv = ft.WebView(
        html_content=full_ghost_os,
        expand=True,
    )

    page.add(wv)

ft.app(target=main)
