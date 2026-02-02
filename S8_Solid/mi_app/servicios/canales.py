from abc import ABC, abstractmethod
from modelos.usuario import Usuario

class CanalNotificacion(ABC):
    @abstractmethod
    def enviar(self, usuario: Usuario, mensaje: str) -> None:
        pass

class CanalEmail(CanalNotificacion):
    def enviar(self, usuario: Usuario, mensaje: str) -> None:
        print(f"Enviando EMAIL a {usuario.email}: {mensaje}")

class CanalSMS(CanalNotificacion):
    def enviar(self, usuario: Usuario, mensaje: str) -> None:
        print(f"Enviando SMS a {usuario.telefono}: {mensaje}")

# ✅ NUEVO CANAL DE COMUNICACIÓN
class CanalWhatsApp(CanalNotificacion):
    def enviar(self, usuario: Usuario, mensaje: str) -> None:
        print(f"Enviando WHATSAPP a {usuario.telefono}: {mensaje}")