
from python_forestacion.constantes import ABSORCION_SEASONAL_INVIERNO, ABSORCION_SEASONAL_VERANO, MES_FIN_VERANO, MES_INICIO_VERANO
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo):
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO 
        else:
            return ABSORCION_SEASONAL_INVIERNO