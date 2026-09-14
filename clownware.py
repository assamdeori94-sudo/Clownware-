# clownware.py — run in Pydroid 3
# Harmless prank suite. No files touched. No data sent.
# Requires: kivy (preinstalled in Pydroid 3), plyer (pip install plyer)

import os, sys, time, random, threading, subprocess, webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# ============================================================
# CONFIG — edit these
# ============================================================
PRANK_NAME = "System Security Alert"
FAKE_VIRUS_COUNT = 47
JUMPSCARE_IMAGE = "jumpscare.png"   # drop a scary png next to this file
PRANK_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# ============================================================
# 1. FAKE VIRUS SCANNER
# ============================================================
def fake_virus_scan():
    lines = [
        "Scanning /storage/emulated/0/...",
        "Scanning /system/...",
        "Scanning WhatsApp media...",
        "Threat detected: Trojan.AndroidOS.FakeBank.a",
        "Threat detected: Spyware.Agent.KM",
        "Threat detected: Ransom.Banker.Gen",
        "Threat detected: Rootkit.Hidden.Pro",
        "Threat detected: Keylogger.Android.Spy",
    ]
    popup = Popup(
        title="⚠ SYSTEM SCAN ⚠",
        content=Label(text="Initializing...", font_size=18),
        size_hint=(0.9, 0.7),
        auto_dismiss=False
    )
    lbl = popup.content
    popup.open()

    state = {"i": 0, "found": 0}

    def tick(dt):
        if state["i"] < len(lines):
            msg = lines[state["i"]]
            if "Threat" in msg:
                state["found"] += 1
                lbl.text = f"{msg}\n\nThreats found: {state['found']}"
            else:
                lbl.text = msg
            state["i"] += 1
        else:
            lbl.text = (
                f"🚨 {FAKE_VIRUS_COUNT} THREATS FOUND 🚨\n\n"
                "Your device is COMPROMISED.\n"
                "All data is being uploaded.\n\n"
                "Tap anywhere to see report."
            )
            popup.dismiss()

    Clock.schedule_interval(tick, 0.9)
    return popup

# ============================================================
# 2. JUMPSCARE OVERLAY
# ============================================================
def jumpscare():
    if not os.path.exists(JUMPSCARE_IMAGE):
        _text_jumpscare()
        return
    popup = Popup(
        title="",
        separator_height=0,
        size_hint=(1, 1),
        auto_dismiss=True,
        background_color=(0, 0, 0, 1)
    )
    popup.content = Image(source=JUMPSCARE_IMAGE, allow_stretch=True)
    popup.open()

    # shiver effect
    win = Window
    base = win.size
    step = [0]
    def shake(dt):
        step[0] += 1
        if step[0] > 30:
            popup.dismiss()
            return False
        dx = random.randint(-20, 20)
        dy = random.randint(-20, 20)
        win.size = (base[0] + dx, base[1] + dy)
    Clock.schedule_interval(shake, 0.03)

def _text_jumpscare():
    popup = Popup(
        title="",
        size_hint=(1, 1),
        auto_dismiss=True,
        background_color=(0.6, 0, 0, 1)
    )
    popup.content = Label(
        text="BOO 👻\n\nAGENT MAN GOT YOU",
        font_size=60,
        color=(1, 1, 1, 1)
    )
    popup.open()

# ============================================================
# 3. FAKE NOTIFICATION SPAM
# ============================================================
def fake_notif_spam():
    try:
        from plyer import notification
    except ImportError:
        return
    msgs = [
        ("Battery Critical", "0% remaining. Shutting down."),
        ("SIM Removed", "Your SIM card was removed."),
        ("Bank Alert", "₹99,999 debited. Balance: ₹0."),
        ("Google", "New login from Russia. Was this you?"),
        ("Camera", "Someone is watching your camera feed."),
        ("WhatsApp", "Your account will be deleted in 1 hour."),
    ]
    for title, msg in msgs:
        try:
            notification.notify(title=title, message=msg, timeout=2)
        except Exception:
            pass
        time.sleep(2)

# ============================================================
# 4. FAKE BSOD FULLSCREEN
# ============================================================
def fake_bsod():
    popup = Popup(
        title="",
        separator_height=0,
        size_hint=(1, 1),
        auto_dismiss=False,
        background_color=(0, 0, 0.4, 1)
    )
    box = BoxLayout(orientation="vertical", padding=40, spacing=20)
    box.add_widget(Label(
        text=":( ",
        font_size=80, color=(1, 1, 1, 1)
    ))
    box.add_widget(Label(
        text="Your device ran into a problem and needs to restart.\n"
             "We're just collecting some error info, and then\n"
             "we'll restart for you.\n\n"
             "0% complete",
        font_size=18, color=(1, 1, 1, 1)
    ))
    btn = Button(text="Tap 47 times to cancel", size_hint=(1, 0.15))
    counter = {"n": 0}
    def on_tap(_):
        counter["n"] += 1
        btn.text = f"Taps: {counter['n']}/47"
        if counter["n"] >= 47:
            popup.dismiss()
    btn.bind(on_release=on_tap)
    box.add_widget(btn)
    popup.content = box
    popup.open()

# ============================================================
# 5. SCREENSHOT-FAKE "HACKED" OVERLAY
# ============================================================
def fake_hacked():
    popup = Popup(
        title="",
        separator_height=0,
        size_hint=(1, 1),
        auto_dismiss=False,
        background_color=(0, 0, 0, 1)
    )
    box = BoxLayout(orientation="vertical")
    box.add_widget(Label(
        text=(
            "> ACCESS GRANTED\n"
            "> TARGET: 127.0.0.1\n"
            "> OS: Android 13\n"
            "> UPLOADING:\n"
            "  /DCIM/Camera.......DONE\n"
            "  /WhatsApp/Media....DONE\n"
            "  /Downloads.........DONE\n"
            "> SENDING TO MERCY SERVER...\n"
            "> 47% [████░░░░░░]\n"
        ),
        font_size=16,
        halign="left",
        valign="top",
        color=(0, 1, 0, 1)
    ))
    btn = Button(text="EXIT", size_hint=(1, 0.15))
    btn.bind(on_release=lambda _: popup.dismiss())
    box.add_widget(btn)
    popup.content = box
    popup.open()

# ============================================================
# 6. RICKROLL
# ============================================================
def rickroll():
    webbrowser.open(PRANK_URL)

# ============================================================
# MAIN UI
# ============================================================
class PrankApp(App):
    def build(self):
        Window.clearcolor = (0.05, 0.05, 0.08, 1)
        root = BoxLayout(orientation="vertical", padding=20, spacing=14)

        root.add_widget(Label(
            text=" You are done bro",
            font_size=36,
            color=(1, 0.4, 0.4, 1),
            size_hint=(1, 0.15)
        ))

        buttons = [
            ("Fake Virus Scan", fake_virus_scan),
            ("JUMPSCARE", jumpscare),
            ("Notification Spam", lambda *_: threading.Thread(target=fake_notif_spam, daemon=True).start()),
            ("Fake BSOD", fake_bsod),
            ("'You Got Hacked'", fake_hacked),
            ("Rickroll", rickroll),
            ("Run EVERYTHING", self.run_all),
            ("Exit", self.stop),
        ]

        for label, cb in buttons:
            b = Button(text=label, font_size=20, size_hint=(1, 0.1))
            if cb == self.run_all:
                b.bind(on_release=lambda _, f=cb: f())
            elif cb == self.stop:
                b.bind(on_release=lambda _, f=cb: f())
            else:
                b.bind(on_release=lambda _, f=cb: f())
            root.add_widget(b)

        return root

    def run_all(self, *_):
        threading.Thread(target=fake_notif_spam, daemon=True).start()
        Clock.schedule_once(lambda dt: fake_virus_scan(), 0)
        Clock.schedule_once(lambda dt: fake_bsod(), 3)
        Clock.schedule_once(lambda dt: jumpscare(), 8)
        Clock.schedule_once(lambda dt: fake_hacked(), 10)
        Clock.schedule_once(lambda dt: rickroll(), 16)

if __name__ == "__main__":
    PrankApp().run()