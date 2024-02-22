from datetime import datetime
fecha_hora_now = datetime.now().strftime("%Y-%m-%d %H:%M:%D")

with open('/workspaces/exercise-terminal-challenge/tutorial_terminal/res/test.txt', "a") as archivo:
	archivo.write(f'Tarea finalizada a las {fecha_hora_now}')
