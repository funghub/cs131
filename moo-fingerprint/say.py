import socket, platform, cowsay

text = f"Hostname:       {socket.gethostname()}\nPython version: {platform.python_version()}\nCowsay version:  {cowsay.__version__}"

cowsay.cow(text)
