import time

# Classe 
class CasaAutomatizada:
    def __init__(self):
        self.comodos = {
            "Sala": {"presenca": False, "luz": False, "temperatura": 26, "ventilador": False},
            "Quarto": {"presenca": False, "luz": False, "temperatura": 30, "ventilador": False},
            "Cozinha": {"presenca": False, "luz": False, "temperatura": 27, "ventilador": False},
        }

    def aplicar_regras(self):
        for comodo, estado in self.comodos.items():
            # Regra: Se houver presença, acender a luz
            estado["luz"] = estado["presenca"]
            
            # Regra: Se a temperatura estiver acima de 30°C e houver presença, ligar o ventilador
            estado["ventilador"] = estado["temperatura"] > 30 and estado["presenca"]

    def atualizar_estado(self, comodo, presenca=None, temperatura=None):
        if comodo in self.comodos:
            if presenca is not None:
                self.comodos[comodo]["presenca"] = presenca
            if temperatura is not None:
                self.comodos[comodo]["temperatura"] = temperatura
            
            self.aplicar_regras()

    def gerar_log(self):
        print("\nEstado atual da casa:\n")
        for comodo, estado in self.comodos.items():
            print(f"{comodo}: A luz está {'ligada' if estado['luz'] else 'desligada'}, "
                  f"pois {'alguém está no cômodo,' if estado['presenca'] else 'ninguém está no cômodo,'} "
                  f"o ventilador está {'ligado' if estado['ventilador'] else 'desligado'} "
                  f"e a temperatura está em {estado['temperatura']}°C.")
        print("\n" + "-" * 120)

# Informando o estado inicial da casa
casa = CasaAutomatizada()
casa.gerar_log()

time.sleep(1)  # Simulando o tempo de espera para a atualização dos sensores
print("\nCenário 1: Ninguém está nos cômodos, então as luzes e os ventiladores devem estar desligados.")
casa.atualizar_estado("Sala", presenca=False)
casa.atualizar_estado("Quarto", presenca=False)
casa.atualizar_estado("Cozinha", presenca=False)
casa.gerar_log()

time.sleep(1)
print("\nCenário 2: A temperatura no quarto aumentou para 32°C, mas ninguém está lá.")
casa.atualizar_estado("Quarto", temperatura=32)
casa.gerar_log()

time.sleep(1)
print("\nCenário 3: Alguém entrou na sala, a luz deve estar ligada.")
casa.atualizar_estado("Sala", presenca=True)
casa.gerar_log()


time.sleep(1)
print("\nCenário 4: A temperatura na sala aumentou para 31°C e há alguém lá, logo o ventilador deve estar ligado.")
casa.atualizar_estado("Sala", temperatura=31)
casa.gerar_log()

time.sleep(1)
print("\nCenário 5: A pessoa saiu da sala, logo o ventilador deve estar estar desligado.") 
casa.atualizar_estado("Sala", presenca=False)
casa.gerar_log()