"""
Bot de Discord sobre cambio climático con 5 comandos educativos.

Este bot proporciona información y consejos sobre cómo combatir
el cambio climático a través de diferentes estrategias.
"""

import os
import sys
import discord
import platform
import random
from discord.ext import commands
from dotenv import load_dotenv

# Cargar variables de entorno desde .env y usar .env.example como respaldo
load_dotenv()
load_dotenv(".env.example", override=False)

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True

# Crear bot
bot = commands.Bot(command_prefix="%", intents=intents)


@bot.event
async def on_ready():
    """Se ejecuta cuando el bot se conecta a Discord."""
    print(f"{bot.user} se ha conectado a Discord")


@bot.command(name="ayuda")
async def ayuda(ctx):
    """Muestra los comandos disponibles y su uso."""
    embed = discord.Embed(
        title="📘 Comandos del Bot Climático",
        description="Usa `%` antes de cada comando",
        color=discord.Color.teal(),
    )
    embed.add_field(
        name="%huella_carbono",
        value=(
            "Calcula la huella de carbono semanal.\n"
            "Uso: `%huella_carbono <auto|bicicleta|transporte_publico> <km_diarios>`"
        ),
        inline=False,
    )
    embed.add_field(
        name="%energia_renovable",
        value="Muestra un consejo aleatorio sobre energía renovable.",
        inline=False,
    )
    embed.add_field(
        name="%emisiones_pais",
        value="Muestra datos de emisiones de CO2 de un país.",
        inline=False,
    )
    embed.add_field(
        name="%dieta_sostenible",
        value="Da consejos sobre una dieta sostenible y amigable con el clima.",
        inline=False,
    )
    embed.add_field(
        name="%check_energia_linux",
        value=(
            "Comando solo para Linux que muestra datos de energía del sistema.\n"
            "No funciona en otros sistemas operativos."
        ),
        inline=False,
    )
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    """Maneja errores de comandos y muestra mensajes amigables."""
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "❌ Faltan argumentos. Usa: "
            "`!huella_carbono <auto|bicicleta|transporte_publico> <km_diarios>`"
        )
        return
    if isinstance(error, commands.BadArgument):
        await ctx.send(
            "❌ Tipo de argumento incorrecto. "
            "Asegúrate de que `km_diarios` sea un número."
        )
        return
    raise error


@bot.command(name="huella_carbono")
async def huella_carbono(ctx, tipo_transporte: str, km_diarios: float):
    """
    Calcula la huella de carbono semanal según el tipo de transporte.

    Args:
        tipo_transporte: 'auto', 'bicicleta', 'transporte_publico'
        km_diarios: Kilómetros recorridos diariamente

    Returns:
        Embed con el cálculo de la huella de carbono
    """
    # Emisiones en kg CO2 por km
    emisiones_por_km = {
        "auto": 0.192,
        "bicicleta": 0.0,
        "transporte_publico": 0.089,
    }

    tipo_transporte_lower = tipo_transporte.lower()

    if tipo_transporte_lower not in emisiones_por_km:
        await ctx.send(
            "❌ Tipo de transporte no válido. "
            "Usa: 'auto', 'bicicleta' o 'transporte_publico'"
        )
        return

    emision_diaria = emisiones_por_km[tipo_transporte_lower] * km_diarios
    emision_semanal = emision_diaria * 7

    transport_name = tipo_transporte_lower.replace('_', ' ').title()
    embed = discord.Embed(
        title="🚗 Calculadora de Huella de Carbono",
        description=f"Transporte: **{transport_name}**",
        color=discord.Color.green(),
    )
    embed.add_field(name="Km diarios", value=f"{km_diarios} km", inline=True)
    embed.add_field(
        name="Emisión diaria",
        value=f"{emision_diaria:.2f} kg CO2",
        inline=True,
    )
    embed.add_field(
        name="Emisión semanal",
        value=f"{emision_semanal:.2f} kg CO2",
        inline=False,
    )

    if tipo_transporte_lower == "bicicleta":
        embed.set_footer(
            text="¡Excelente! La bicicleta es la opción más ecológica 🌍"
        )
    elif tipo_transporte_lower == "transporte_publico":
        embed.set_footer(
            text="¡Buen trabajo! El transporte público reduce emisiones 👍"
        )
    else:
        embed.set_footer(
            text="Considera usar transporte público o bicicleta ♻️"
        )

    await ctx.send(embed=embed)


@bot.command(name="energia_renovable")
async def energia_renovable(ctx):
    """
    Proporciona consejos aleatorios sobre energía renovable.

    Returns:
        Embed con consejos sobre energías limpias
    """
    consejos = [
        {
            "titulo": "☀️ Energía Solar",
            "descripcion": "Instala paneles solares en tu hogar. "
            "Una casa con paneles puede reducir sus emisiones "
            "hasta un 80%",
        },
        {
            "titulo": "💨 Energía Eólica",
            "descripcion": "Apoya proyectos de energía eólica en tu región. "
            "Un único aerogenerador puede evitar miles de toneladas "
            "de CO2 anuales",
        },
        {
            "titulo": "💧 Energía Hidroeléctrica",
            "descripcion": "Presiona a tu gobierno para invertir en represas "
            "hidroeléctricas. Es una fuente limpia y renovable",
        },
        {
            "titulo": "🔥 Energía Geotérmica",
            "descripcion": "Conoce proyectos geotérmicos en tu país. "
            "Aprovecha el calor del planeta para generar electricidad",
        },
        {
            "titulo": "🌊 Energía Maremotriz",
            "descripcion": "Apoya investigación en energía de mareas. "
            "Los océanos son una fuente inagotable de energía limpia",
        },
    ]

    consejo = random.choice(consejos)

    embed = discord.Embed(
        title=consejo["titulo"],
        description=consejo["descripcion"],
        color=discord.Color.blue(),
    )
    embed.set_footer(text="🌱 Cada acción cuenta en la lucha climática")

    await ctx.send(embed=embed)


@bot.command(name="emisiones_pais")
async def emisiones_pais(ctx, pais: str):
    """
    Muestra datos de emisiones de CO2 de un país.

    Args:
        pais: Nombre del país

    Returns:
        Embed con estadísticas de emisiones
    """
    # Datos de emisiones (Gt CO2 anuales aproximados)
    emisiones_data = {
        "china": {"emisiones": 10.5, "ranking": 1},
        "estados unidos": {"emisiones": 5.8, "ranking": 2},
        "india": {"emisiones": 2.4, "ranking": 3},
        "rusia": {"emisiones": 1.7, "ranking": 4},
        "japón": {"emisiones": 1.0, "ranking": 5},
        "alemania": {"emisiones": 0.8, "ranking": 6},
        "españa": {"emisiones": 0.3, "ranking": 20},
        "méxico": {"emisiones": 0.65, "ranking": 12},
        "brasil": {"emisiones": 0.5, "ranking": 14},
    }

    pais_lower = pais.lower()

    if pais_lower not in emisiones_data:
        await ctx.send(
            "❌ País no disponible en la base de datos. "
            "Intenta con: China, Estados Unidos, India, Rusia, Japón, "
            "Alemania, España, México o Brasil"
        )
        return

    datos = emisiones_data[pais_lower]

    embed = discord.Embed(
        title=f"🌍 Emisiones de CO2 - {pais.title()}",
        color=discord.Color.red(),
    )
    embed.add_field(
        name="Emisiones anuales",
        value=f"{datos['emisiones']} Gt CO2",
        inline=True,
    )
    embed.add_field(
        name="Ranking mundial",
        value=f"Puesto #{datos['ranking']}",
        inline=True,
    )
    embed.add_field(
        name="Acciones recomendadas",
        value="• Reducir dependencia de combustibles fósiles\n"
        "• Invertir en energías renovables\n"
        "• Mejorar eficiencia energética industrial",
        inline=False,
    )
    embed.set_footer(
        text="Fuente: Datos aproximados de organismos internacionales"
    )

    await ctx.send(embed=embed)


@bot.command(name="dieta_sostenible")
async def dieta_sostenible(ctx):
    """
    Proporciona consejos sobre dietas sostenibles y amigables con el clima.

    Returns:
        Embed con consejos alimenticios ecológicos
    """
    embed = discord.Embed(
        title="🥗 Dieta Sostenible para el Clima",
        color=discord.Color.green(),
    )
    embed.add_field(
        name="🥘 Reduce carne roja",
        value="La ganadería bovina genera 14.5% de las emisiones globales. "
        "Come carne roja máximo 2 veces a la semana",
        inline=False,
    )
    embed.add_field(
        name="🐟 Elige proteínas alternativas",
        value="Legumbres, frutos secos, pescado azul y algas son excelentes "
        "opciones con menor huella de carbono",
        inline=False,
    )
    embed.add_field(
        name="🌾 Compra productos locales",
        value="Reducen el transporte. El transporte de alimentos representa "
        "el 11% de las emisiones alimentarias",
        inline=False,
    )
    embed.add_field(
        name="🍌 Come alimentos de temporada",
        value="Los productos fuera de temporada requieren transporte "
        "internacional y energía de invernaderos",
        inline=False,
    )
    embed.add_field(
        name="♻️ Reduce desperdicio",
        value="1/3 de la comida se desperdicia. Planifica tus compras "
        "y compostas los residuos orgánicos",
        inline=False,
    )
    embed.set_footer(
        text="🌱 Una dieta sostenible puede reducir tu huella en 50%"
    )

    await ctx.send(embed=embed)


@bot.command(name="check_energia_linux")
async def check_energia_linux(ctx):
    """
    SOLO FUNCIONA EN LINUX.

    Usa uptime y carga promedio para dar una visión del sistema.
    Si no está en Linux, causa un crash silencioso.
    """
    try:
        if platform.system() != "Linux":
            raise Exception("Sistema no compatible")

        try:
            with open("/proc/uptime", "r") as f:
                uptime_seconds = float(f.read().split()[0])
        except (OSError, ValueError, IndexError):
            await ctx.send(
                "⚠️ No se pudo leer /proc/uptime en este Linux. "
                "El comando requiere un Linux con /proc activo."
            )
            return

        try:
            with open("/proc/loadavg", "r") as f:
                load_values = f.read().split()
                load_1, load_5, load_15 = load_values[:3]
        except (OSError, ValueError, IndexError):
            await ctx.send(
                "⚠️ No se pudo leer /proc/loadavg en este Linux. "
                "El comando requiere un Linux con /proc activo."
            )
            return

        uptime_minutes = int(uptime_seconds // 60)
        uptime_hours = uptime_minutes // 60
        uptime_days = uptime_hours // 24
        uptime_hours %= 24
        uptime_minutes %= 60

        embed = discord.Embed(
            title="⚡ Estado del Sistema Linux",
            description=(
                "Tiempo activo y carga promedio para optimizar el consumo de energía "
                "en servidores y equipos Linux."
            ),
            color=discord.Color.blue(),
        )
        embed.add_field(
            name="Tiempo activo",
            value=f"{uptime_days}d {uptime_hours}h {uptime_minutes}m",
            inline=True,
        )
        embed.add_field(
            name="Carga promedio",
            value=f"1m: {load_1}, 5m: {load_5}, 15m: {load_15}",
            inline=True,
        )
        embed.add_field(
            name="💡 Consejo",
            value=(
                "Reduce servicios y procesos innecesarios para consumir menos "
                "energía y ayudar al clima."
            ),
            inline=False,
        )
        embed.set_footer(text="Disponible solo en Linux")

        await ctx.send(embed=embed)

    except Exception:
        # Crash silencioso - no envía ningún mensaje
        raise


def get_token():
    """Obtiene el token de Discord de variables de entorno."""
    token = os.getenv("DISCORD_TOKEN")
    if not token or token == "tu_token_real_aqui_sin_comillas":
        print("❌ ERROR: Token de Discord no configurado")
        print("\nPasos para configurar:")
        print("1. Ve a: https://discord.com/developers/applications")
        print("2. Crea una nueva aplicación")
        print("3. Ve a 'Bot' y copia el token")
        print("4. Copia el archivo .env.example a .env")
        print("5. Reemplaza 'tu_token_real_aqui_sin_comillas' con tu token")
        print("6. Guarda y ejecuta nuevamente")
        sys.exit(1)
    return token


if __name__ == "__main__":
    token = get_token()
    bot.run(token)
