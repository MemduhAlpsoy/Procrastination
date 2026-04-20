#  Procrastination Hunter

Procrastination Hunter is a ruthless yet educational desktop automation tool that silently hunts down your distracting apps and websites in the background. The moment you open a forbidden game or tab (e.g., Steam, YouTube), the system detects it, freezes the application, locks your screen, and traps you with a math problem. 

Solve it to earn "Immunity," or the system will mercilessly terminate your app!

##  Features

*  **Continuous Listener:** Runs in the background with minimal resource consumption. It catches dynamic window titles (like constantly changing YouTube tabs) using a smart "Fuzzy Match" algorithm.
*  **Ruthless Enforcer:** Intervenes directly at the OS level. It completely freezes (`suspend`) active processes/games and instantly minimizes browser windows.
*  **Procedural Question Generator:** Zero hardcoded questions! Generates a completely new Polynomial Derivative problem with random coefficients and degrees upon every catch (featuring aesthetic Unicode exponent formatting: e.g., `4x³ + 2x`).
*  **Interrogation Room (GUI):** A built-in, inescapable Tkinter interface that runs Fullscreen and "Always on Top," completely hiding your taskbar and other monitors.
*  **Immunity System (Cooldown):** If you answer correctly, you are rewarded with a "Shield" that allows you to use that specific application freely for a designated period.
* **Giving up** If you want to give up and end the interrogation, you can click the "Give Up" button, but be warned: it will immediately kill the offending application without any immunity or cooldown.
*  **Lethal Penalty:** If you attempt to cheat by bypassing the interface, your active program is instantly killed.

## Project Architecture

The project consists of 4 isolated core modules and an Orchestrator (`main.py`):

1.  **`listener/` (The Eyes):** Scans active background processes and windows.
2.  **`enforcer/` (The Muscles):** Commands the operating system to freeze, resume, or minimize targets.
3.  **`generator/` (The Brain):** Uses mathematical algorithms to produce infinite variations of question/answer pairs.
4.  **`gui/` (The Prison):** The asynchronous graphical user interface module that confronts the user.

##  Installation & Usage

### Prerequisites
You need Python 3.x and the following libraries installed on your system:

```bash
pip install psutil pygetwindow tkinter pyautogui
```

### How to Run
1.  Clone the repository:
```bash
git clone https://github.com/MemduhAlpsoy/procrastination-hunter.git
```
2.  Navigate to the project directory and run the main script:
```python main.py
```
3.  The system will start monitoring for distractions immediately. Open a forbidden app or website to see it in action!
##  Contributing
Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request.
##  License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
