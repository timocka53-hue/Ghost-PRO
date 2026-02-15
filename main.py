import flet as ft

def main(page: ft.Page):
    page.title = "GHOST PRO V6 ULTIMATE"
    page.padding = 0
    page.bgcolor = "#000000"

    # ВЕСЬ ТВОЙ ИМБОВЫЙ ФУНКЦИОНАЛ И ДИЗАЙН ТУТ
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body, html { margin: 0; padding: 0; background: #000; color: #00FF00; font-family: 'Courier New', monospace; height: 100%; overflow: hidden; }
            canvas { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.4; }
            .ghost-card { border: 1px solid #00FF00; background: rgba(0, 10, 0, 0.95); box-shadow: 0 0 20px #00FF00; padding: 20px; }
            .screen { display: none; height: 100vh; flex-direction: column; padding: 15px; z-index: 10; position: relative; }
            .active { display: flex; }
            input, textarea { background: #000; border: 1px solid #00FF00; color: #00FF00; padding: 10px; outline: none; width: 100%; box-sizing: border-box; }
            .btn { border: 1px solid #00FF00; padding: 12px; text-align: center; cursor: pointer; font-weight: bold; text-transform: uppercase; transition: 0.2s; }
            .btn:active { background: #00FF00; color: #000; box-shadow: 0 0 30px #00FF00; }
            .admin-only { border-color: #ff0000 !important; color: #ff0000 !important; }
            .msg-bubble { margin-bottom: 10px; border-left: 2px solid #00FF00; padding-left: 8px; font-size: 13px; background: rgba(0,255,0,0.05); }
            .avatar-img { width: 80px; height: 80px; border-radius: 50%; border: 2px solid #00FF00; object-fit: cover; }
            .glitch { animation: g 2s infinite; }
            @keyframes g { 0% { opacity: 1; } 50% { opacity: 0.7; transform: skewX(2deg); } 100% { opacity: 1; } }
        </style>
    </head>
    <body>
        <canvas id="m"></canvas>

        <div id="auth-screen" class="screen active justify-center items-center">
            <div class="ghost-card w-full max-w-sm space-y-4">
                <h1 class="text-3xl text-center font-bold glitch tracking-tighter">GHOST_PRO_OS</h1>
                <input type="email" id="email" placeholder="EMAIL / IDENTIFIER">
                <input type="password" id="pass" placeholder="ACCESS_PASSWORD">
                <div class="btn" onclick="authProcess()">INITIALIZE SESSION</div>
                <div class="text-[9px] text-center opacity-40">SECURE NODE: ACTIVE | AES-256-GCM</div>
            </div>
        </div>

        <div id="2fa-screen" class="screen justify-center items-center">
            <div class="ghost-card w-full max-w-xs text-center space-y-4">
                <h2 class="text-xl">2FA_REQUIRED</h2>
                <p class="text-[10px]">CHECK EMAIL FOR VERIFICATION CODE</p>
                <input type="text" id="code2fa" placeholder="000000" class="text-center text-2xl tracking-[5px]">
                <div class="btn" onclick="verify2fa()">VERIFY_IDENTITY</div>
            </div>
        </div>

        <div id="chat-screen" class="screen">
            <div class="flex justify-between items-center border-b border-green-500 pb-2 mb-2">
                <span id="role-label" class="text-[10px] border border-green-500 px-1">GUEST_LINK</span>
                <span onclick="nav('profile-screen')" class="text-xs underline cursor-pointer">/MY_SYSTEM/</span>
            </div>
            <input type="text" id="user-search" placeholder="SEARCH_BY_UID (@user...)" class="h-8 text-xs mb-2">
            <div id="chat-flow" class="flex-1 overflow-y-auto p-2 bg-black/60 border border-green-900 mb-2">
                <div class="text-[10px] text-center opacity-30 italic">--- SECURE CHANNEL READY ---</div>
            </div>
            
            <div id="admin-panel" class="hidden grid grid-cols-2 gap-2 mb-2">
                <div class="btn admin-only text-[10px] py-1" onclick="nav('tickets-screen')">VIEW_TICKETS</div>
                <div class="btn admin-only text-[10px] py-1" onclick="broadcast()">BROADCAST</div>
            </div>

            <div class="flex space-x-2">
                <button onclick="alert('REC_AUDIO')" class="btn px-3 py-1">🎤</button>
                <button onclick="alert('REC_VIDEO')" class="btn px-3 py-1">🎥</button>
                <input type="text" id="msg-input" placeholder="Data..." class="flex-1 h-10">
                <button onclick="sendMsg()" class="btn px-4 py-1">></button>
            </div>
        </div>

        <div id="tickets-screen" class="screen">
            <div class="border-b border-red-500 pb-2 mb-4 flex justify-between">
                <span class="text-red-500 font-bold">ACTIVE_TICKETS</span>
                <span onclick="nav('chat-screen')" class="text-[10px] underline">CLOSE</span>
            </div>
            <div id="tickets-list" class="space-y-2 overflow-y-auto flex-1">
                <div class="ghost-card p-2 border-red-900 flex justify-between items-center" onclick="openSupportChat('@user1')">
                    <div class="text-[10px]">FROM: @user1<br><span class="italic text-gray-400">"Help with 2FA..."</span></div>
                    <div class="text-[8px] bg-red-600 px-1 text-white">REPLY</div>
                </div>
            </div>
            <div class="grid grid-cols-2 gap-2 mt-2">
                <div class="btn admin-only text-[10px]" onclick="alert('All Users Frozen')">FREEZE_ALL</div>
                <div class="btn admin-only text-[10px]" onclick="alert('Security Lockdown')">LOCK_CORE</div>
            </div>
        </div>

        <div id="profile-screen" class="screen items-center space-y-6">
            <h2 class="text-xl glitch">IDENTITY_STORAGE</h2>
            <div class="relative">
                <img id="my-avatar" src="https://api.dicebear.com/7.x/pixel-art/svg?seed=Ghost" class="avatar-img">
                <input type="file" id="av-file" class="hidden" onchange="loadAv(event)">
                <button onclick="document.getElementById('av-file').click()" class="absolute bottom-0 right-0 bg-green-500 text-black text-[10px] px-1 font-bold">UPLOAD</button>
            </div>
            <input type="text" id="my-uid" placeholder="SET_UNIQUE_UID" class="text-center">
            <div class="w-full space-y-2">
                <button onclick="nav('support-chat-screen')" class="w-full btn text-sm">CONTACT_SUPPORT</button>
                <button onclick="nav('chat-screen')" class="w-full btn text-sm opacity-50">BACK</button>
            </div>
        </div>

        <div id="support-chat-screen" class="screen">
            <div class="border-b border-green-500 pb-2 mb-2">DIRECT_SUPPORT_LINE</div>
            <div id="support-flow" class="flex-1 overflow-y-auto p-2">
                <div class="msg-bubble text-[11px]"><span class="text-red-500 font-bold">SYSTEM:</span> State your bug or issue.</div>
            </div>
            <div class="flex space-x-2">
                <input type="text" id="sup-input" placeholder="Message Admin..." class="flex-1">
                <button onclick="sendToSup()" class="btn px-4">SEND</button>
            </div>
        </div>

        <script>
            let isAdmin = false;
            let currentUID = "@guest";

            // MATRIX EFFECT
            const c = document.getElementById('m');
            const x = c.getContext('2d');
            c.width = window.innerWidth; c.height = window.innerHeight;
            const s = "77701GHOSTPRO";
            const f = 16;
            const drops = Array(Math.floor(c.width/f)).fill(1);
            function draw() {
                x.fillStyle = "rgba(0,0,0,0.05)"; x.fillRect(0,0,c.width,c.height);
                x.fillStyle = "#0F0"; x.font = f+"px monospace";
                drops.forEach((y, i) => {
                    x.fillText(s[Math.floor(Math.random()*s.length)], i*f, y*f);
                    if(y*f > c.height && Math.random() > 0.975) drops[i] = 0;
                    drops[i]++;
                });
            }
            setInterval(draw, 35);

            // LOGIC
            function nav(id) {
                document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
                document.getElementById(id).classList.add('active');
            }

            function authProcess() {
                const e = document.getElementById('email').value;
                const p = document.getElementById('pass').value;
                if(e === "adminpan" && p === "TimaIssam2026") {
                    isAdmin = true;
                    currentUID = "@ADMIN_CORE";
                    document.getElementById('role-label').innerText = "MASTER_NODE";
                    document.getElementById('role-label').style.color = "red";
                    document.getElementById('admin-panel').classList.remove('hidden');
                    nav('chat-screen'); // Админ входит мгновенно
                } else {
                    currentUID = "@" + (e.split('@')[0] || "user");
                    nav('2fa-screen');
                }
            }

            function verify2fa() {
                document.getElementById('my-uid').value = currentUID;
                nav('chat-screen');
            }

            function sendMsg() {
                const i = document.getElementById('msg-input');
                if(!i.value) return;
                document.getElementById('chat-flow').innerHTML += `<div class="msg-bubble"><span class="text-blue-500">${currentUID}:</span><br>${i.value}</div>`;
                i.value = "";
                document.getElementById('chat-flow').scrollTop = 9999;
            }

            function sendToSup() {
                const i = document.getElementById('sup-input');
                document.getElementById('support-flow').innerHTML += `<div class="msg-bubble text-[11px]"><span class="text-blue-400">YOU:</span><br>${i.value}</div>`;
                i.value = "";
                alert("ADMIN_NOTIFIED: Notification sent to phone.");
            }

            function loadAv(e) {
                const r = new FileReader();
                r.onload = () => document.getElementById('my-avatar').src = r.result;
                r.readAsDataURL(e.target.files[0]);
            }

            function broadcast() {
                const m = prompt("ENTER BROADCAST MESSAGE:");
                if(m) alert("BROADCASTING TO ALL NODES...");
            }

            function openSupportChat(uid) {
                alert("OPENING DIRECT CHAT WITH " + uid);
                nav('chat-screen');
            }
        </script>
    </body>
    </html>
    """

    # WebView — загружаем код напрямую
    wv = ft.WebView(
        html_content,
        expand=True,
    )

    page.add(wv)

ft.app(target=main)
