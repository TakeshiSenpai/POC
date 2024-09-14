from typing import List

# Simulación de una API genérica para dispositivos externos
class DeviceAPI:
    def __init__(self, device_name: str):
        self.device_name = device_name
        self.alarms = []
        self.events = []

    def sync_alarms(self, alarms: List[str]):
        self.alarms = alarms
        print(f"Alarmas sincronizadas con {self.device_name}:", self.alarms)

    def receive_command(self, command: str):
        print(f"{self.device_name} recibe comando:", command)
        if command.startswith("cancelar"):
            alarm = command.split(" ")[1]
            if alarm in self.alarms:
                self.alarms.remove(alarm)
                print(f"Alarma {alarm} cancelada en {self.device_name}.")

# Gestión de Alarmas
class AlarmManager:
    def __init__(self):
        self.alarms = []
    
    def create_alarm(self, alarm: str):
        self.alarms.append(alarm)
        print(f"Alarma creada: {alarm}")

    def delete_alarm(self, alarm: str):
        if alarm in self.alarms:
            self.alarms.remove(alarm)
            print(f"Alarma eliminada: {alarm}")

    def sync_with_device(self, device_api: DeviceAPI):
        device_api.sync_alarms(self.alarms)

# Gestión de Eventos
class EventManager:
    def __init__(self):
        self.events = []

    def create_event(self, event: str):
        self.events.append(event)
        print(f"Evento creado: {event}")

    def delete_event(self, event: str):
        if event in self.events:
            self.events.remove(event)
            print(f"Evento eliminado: {event}")

# Notificaciones
class NotificationService:
    def send_notification(self, message: str):
        print("Notificación enviada:", message)

# Función principal para la PoC
def main():
    # Inicialización de componentes
    alarm_manager = AlarmManager()
    event_manager = EventManager()
    notification_service = NotificationService()
    
    # Simulación de dos dispositivos externos
    device_1 = DeviceAPI("Google Home")
    device_2 = DeviceAPI("Smartwatch")

    # Crear alarmas y eventos
    alarm_manager.create_alarm("Despertador 07:00")
    event_manager.create_event("Reunión con el equipo 10:00")

    # Sincronizar con los dispositivos externos
    alarm_manager.sync_with_device(device_1)
    alarm_manager.sync_with_device(device_2)

    # Simular notificaciones
    notification_service.send_notification("Recordatorio: Reunión con el equipo en 30 minutos.")

    # Simular comandos recibidos en dispositivos externos
    device_1.receive_command("cancelar Despertador 07:00")
    device_2.receive_command("cancelar Despertador 07:00")

    # Mostrar estado final
    print("Estado final de alarmas:", alarm_manager.alarms)
    print("Estado final de eventos:", event_manager.events)

if __name__ == "__main__":
    main()
