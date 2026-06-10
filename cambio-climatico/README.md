# Bot de Discord sobre Cambio Climático 🌍

Bot educativo de Discord con 5 comandos diferentes sobre cambio climático y cómo combatirlo.

## Características

El bot incluye 5 comandos completamente diferentes:

### 1. `!huella_carbono` 🚗
Calcula tu huella de carbono semanal según el tipo de transporte.
- **Parámetros**: `tipo_transporte` (auto, bicicleta, transporte_publico), `km_diarios` (número)
- **Ejemplo**: `!huella_carbono auto 50`

### 2. `!energia_renovable` ☀️
Proporciona consejos aleatorios sobre diferentes tipos de energía renovable.
- **Sin parámetros**
- **Ejemplo**: `!energia_renovable`

### 3. `!emisiones_pais` 🌍
Muestra estadísticas de emisiones de CO2 de un país.
- **Parámetros**: `pais` (nombre del país)
- **Países disponibles**: China, Estados Unidos, India, Rusia, Japón, Alemania, España, México, Brasil
- **Ejemplo**: `!emisiones_pais España`

### 4. `!dieta_sostenible` 🥗
Proporciona consejos sobre dietas sostenibles y amigables con el clima.
- **Sin parámetros**
- **Ejemplo**: `!dieta_sostenible`

### 5. `!check_energia_linux` ⚡ (SOLO LINUX)
**ESPECIAL**: Monitorea la energía del sistema (solo funciona en Linux).
- Si se ejecuta en Windows o macOS, el bot se **crashea silenciosamente** sin enviar mensajes.
- **Sin parámetros**
- **Ejemplo**: `!check_energia_linux`

## Instalación

### 1. Clonar o descargar el proyecto
```bash
cd /home/pc/Proyectos/cambio-climatico
```

### 2. Crear un entorno virtual (opcional pero recomendado)
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Obtener token de Discord
1. Ir a [Discord Developer Portal](https://discord.com/developers/applications)
2. Crear una nueva aplicación
3. Ir a "Bot" y crear un bot
4. Copiar el token
5. En `hola.py`, reemplazar `"TU_TOKEN_DE_DISCORD_AQUI"` con tu token real

### 5. Dar permisos al bot
En Discord Developer Portal:
1. Ir a "OAuth2" → "URL Generator"
2. Seleccionar scopes: `bot`
3. Seleccionar permisos: `Send Messages`, `Embed Links`, `Read Messages/View Channels`
4. Usar la URL generada para invitar el bot a tu servidor

## Ejecución

```bash
python hola.py
```

El bot debería mostrar:
```
NombreDelBot#0000 se ha conectado a Discord
```

## Características de Código

✅ Cumple con **PEP-8**:
- Máximo 79 caracteres por línea
- Nombres en `snake_case`
- Clases en `PascalCase`
- Docstrings descriptivos
- Importes organizados

✅ **Un comando especial solo para Linux**: `!check_energia_linux` se crashea silenciosamente en otros SO

✅ **Embeds bonitos** con colores y emojis

✅ **Información útil** sobre cambio climático

## Notas

- El comando `!check_energia_linux` busca archivos de batería en `/sys/class/power_supply/`
- Los datos de emisiones son aproximados basados en organismos internacionales
- Todos los comandos tienen funcionalidades educativas reales

---

**¡Ayuda a combatir el cambio climático desde Discord!** 🌱
