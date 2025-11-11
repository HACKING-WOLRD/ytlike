#!/usr/bin/env python3
# youtube_like_prank_nonroot.py
# HACKING WORLD™ — YouTube Video Like Simulator (NON-ROOT • DEMO)
# WARNING: 100% LOCAL DEMO — no network calls, no real likes added.
# This script intentionally displays a visible "DEMO / FAKE" label. Do NOT mislead others.

import os, sys, time, random

# Colors
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
C = '\033[1;36m'; M = '\033[1;35m'; W = '\033[1;37m'; RESET = '\033[0m'

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def slow_type(text, delay=0.005):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def spinner(msg, secs=1.6):
    frames = ['|','/','-','\\']
    sys.stdout.write(Y + msg + " ")
    t0 = time.time(); i = 0
    while time.time() - t0 < secs:
        sys.stdout.write(frames[i % 4]); sys.stdout.flush()
        time.sleep(0.10); sys.stdout.write('\b'); i += 1
    print(G + " ✓" + RESET)

def progress_bar(cur, target, width=40):
    frac = min(1.0, cur/target) if target>0 else 1.0
    filled = int(width * frac)
    bar = "█"*filled + "░"*(width-filled)
    percent = int(frac*100)
    sys.stdout.write(C + f"\r[{bar}] {cur}/{target} likes ({percent}%)" + RESET)
    sys.stdout.flush()

def banner():
    clear()
    print(M + "██╗   ██╗███████╗██╗   ██╗███████╗" + RESET)
    print(C + "██║   ██║██╔════╝██║   ██║██╔════╝" + RESET)
    print(G + "██║   ██║█████╗  ██║   ██║███████╗" + RESET)
    print(Y + "██║   ██║██╔══╝  ██║   ██║╚════██║" + RESET)
    print(R + "╚██████╔╝███████╗╚██████╔╝███████║" + RESET)
    print(W + "\n    H A C K I N G   W O R L D™ — YT LIKE SIMULATOR (DEMO)\n" + RESET)
    print(R + "!!! DEMO / PRANK — This script does NOT add real likes or contact YouTube !!!\n" + RESET)

def simulate_likes(start, target, duration=5.0):
    steps = max(8, int(duration / 0.12))
    cur = start
    for i in range(steps):
        remaining = target - cur
        if remaining <= 0:
            break
        # make increments look natural / bursty
        burst = max(1, int(remaining / (steps - i)))
        jitter = random.randint(0, max(1, burst//3))
        inc = burst + jitter
        # occasional big jump
        if random.random() < 0.08:
            inc += random.randint(10, min(200, remaining))
        cur += inc
        if cur > target: cur = target
        progress_bar(cur, target)
        time.sleep(0.12 + random.uniform(-0.02, 0.06))
    print()

def show_confetti():
    syms = ['✦','✧','✪','•','*','+']
    cols = [R,G,Y,C,M,W]
    for _ in range(6):
        line = "".join(random.choice(cols) + random.choice(syms) + RESET for _ in range(60))
        print(line)
        time.sleep(0.06)

def save_log(channel, video, start, target):
    try:
        os.makedirs("prank_logs", exist_ok=True)
        path = f"prank_logs/yt_like_sim_{int(time.time())}.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write("YT LIKE SIMULATION — HACKING WORLD™\n")
            f.write(f"time: {time.ctime()}\n")
            f.write(f"channel: {channel}\n")
            f.write(f"video: {video}\n")
            f.write(f"start_likes: {start}\n")
            f.write(f"displayed_likes: {target}\n")
            f.write("NOTE: DEMO/FAKE\n")
        return path
    except Exception:
        return None

def main():
    banner()
    channel = input(Y + "Enter channel name (optional): " + W).strip() or "MyChannel"
    video = input(Y + "Enter video title or URL (optional): " + W).strip() or "MyVideo"
    try:
        start = int(input(Y + "Current likes (e.g. 120): " + W).strip())
    except:
        start = random.randint(0,500)
    try:
        target = int(input(Y + "Target likes to simulate (e.g. 5000): " + W).strip())
    except:
        target = start + random.randint(50,5000)
    print()
    slow_type(C + f"Preparing like stream for '{video}' on channel '{channel}'..." + RESET, 0.008)
    spinner("[*] Establishing visual like mesh (simulation)", 1.8)
    spinner("[*] Securing ghost CDN routes (visual)", 1.6)

    # package suggestion (visual only)
    packages = [("Lite", start + 200), ("Boost", start + 1200), ("Turbo", start + 5000)]
    print()
    print(W + "Available visual packages (simulation):" + RESET)
    for i,(n,v) in enumerate(packages,1):
        print(C + f" [{i}] {n:<6} -> ~{v} likes" + RESET)
    print()
    choice = input(Y + "[?] Choose package number or press Enter to run custom target: " + W).strip()
    if choice.isdigit():
        idx = max(1, min(len(packages), int(choice)))
        _, pkg_target = packages[idx-1]
        target = pkg_target

    print()
    spinner("[*] Initiating like stream (visual)", 1.4)
    simulate_likes(start, target, duration=6.0)

    print(G + f"\n[✓] Simulation complete. Displayed likes for '{video}': {target}" + RESET)
    show_confetti()
    print(R + "\nNOTE: THIS IS A SIMULATION / DEMO — NO REAL LIKES WERE ADDED." + RESET)

    if input(Y + "\nSave simulation log locally? (y/N): " + W).strip().lower() == 'y':
        p = save_log(channel, video, start, target)
        if p:
            print(G + "[✓] Saved log → " + p + RESET)
        else:
            print(R + "[!] Save failed." + RESET)

    input(W + "\nPress Enter to exit..." + RESET)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + R + "Interrupted. Exiting." + RESET)