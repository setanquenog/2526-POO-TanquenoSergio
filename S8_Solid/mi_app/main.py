from modelos.usuario import Usuario
from servicios.canales import CanalEmail, CanalSMS, CanalWhatsApp
from servicios.notificacion_service import NotificacionService

usuario = Usuario("Ana", "ana@example.com", "123456789")

# Email
servicio_email = NotificacionService(CanalEmail())
servicio_email.enviar_notificacion(usuario, "Hola vía Email!")

# SMS
servicio_sms = NotificacionService(CanalSMS())
servicio_sms.enviar_notificacion(usuario, "Hola vía SMS!")

# WhatsApp
servicio_whatsapp = NotificacionService(CanalWhatsApp())
servicio_whatsapp.enviar_notificacion(usuario, "Hola vía WhatsApp!")