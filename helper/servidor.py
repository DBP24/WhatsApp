import os
class Linux :
 
    # Comando para saber el estado del Disco duro
    def obtener_estado_disco(self):
        return f'estado de disco: \n \n {os.popen('df -h').read()}'
    
    def obtener_estado_memoria(self):
        return f'estado de memoria: \n \n {os.popen('free -m').read()}'
    
    def obtener_estado_proceso(self):
        return f'estado de proceso: \n \n {os.popen('free -m').read()}'