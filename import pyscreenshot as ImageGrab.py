import pyscreenshot as ImageGrab
import webbrowser,pyautogui
import time


if __name__ == "__main__":
    
    url = 'http://192.168.0.28:3000/'
    webbrowser.open_new_tab(url)
    time.sleep(5)
    imagem = ImageGrab.grab()
    imagem.save('192_168_0_28_3000.jpg', 'jpeg')
    pyautogui.hotkey('ctrl', 'w')