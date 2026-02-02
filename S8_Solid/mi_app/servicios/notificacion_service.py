from modelos.usuario import Usuario
from servicios.canales import CanalNotificacion

class NotificacionService:
    def __init__(self, canal: CanalNotificacion):
        self.canal = canal

    def enviar_notificacion(self, usuario: Usuario, mensaje: str) -> None:
        self.canal.enviar(usuario, mensaje)