import pygame  # Importa la librería pygame
import random  # Importa la librería random para generar posiciones aleatorias de la comida

# Inicializa Pygame
pygame.init()

# Definir colores (RGB)
WHITE = (255, 255, 255)  # Color de la serpiente
BLACK = (0, 0, 0)  # Fondo del juego
GREEN = (0, 255, 0)  # Color de la comida
RED = (213, 50, 80)  # Color de la pantalla de Game Over

# Dimensiones de la pantalla
WIDTH, HEIGHT = 600, 400  # Ancho y alto de la ventana del juego
BLOCK_SIZE = 10  # Tamaño de cada bloque de la serpiente y la comida
SPEED = 15  # Velocidad del juego (cuántos cuadros por segundo)

# Crear la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Crea la ventana del juego con las dimensiones especificadas
pygame.display.set_caption('Snake Game')  # Título de la ventana del juego

# Reloj del juego para controlar la velocidad
clock = pygame.time.Clock()

# Función para mostrar mensajes en pantalla
def message(msg, color):
    """ Muestra un mensaje en pantalla.
    msg: texto del mensaje.
    color: color del mensaje. """
    font = pygame.font.SysFont(None, 35)  # Usa una fuente predeterminada del sistema
    text = font.render(msg, True, color)  # Renderiza el mensaje con el texto y color
    screen.blit(text, [WIDTH // 6, HEIGHT // 3])  # Muestra el texto en el centro aproximado de la pantalla

# Función principal del juego
def game():
    # Posición inicial de la serpiente (en el centro de la pantalla)
    x, y = WIDTH // 2, HEIGHT // 2
    # Cambios en la dirección de la serpiente (inicia sin moverse)
    x_change, y_change = 0, 0
    snake_body = []  # Lista que almacenará los segmentos de la serpiente
    snake_length = 1  # Longitud inicial de la serpiente (solo la cabeza)

    # Posición inicial de la comida en una coordenada aleatoria
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    game_over = False  # Indicador para controlar el estado del juego
    while not game_over:  # Bucle principal del juego
        for event in pygame.event.get():  # Revisa los eventos (teclado, cierre de ventana, etc.)
            if event.type == pygame.QUIT:  # Si el jugador cierra la ventana
                game_over = True  # Termina el juego
            if event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if event.key == pygame.K_LEFT:
                    x_change, y_change = -BLOCK_SIZE, 0  # Cambia la dirección hacia la izquierda
                elif event.key == pygame.K_RIGHT:
                    x_change, y_change = BLOCK_SIZE, 0  # Cambia la dirección hacia la derecha
                elif event.key == pygame.K_UP:
                    x_change, y_change = 0, -BLOCK_SIZE  # Cambia la dirección hacia arriba
                elif event.key == pygame.K_DOWN:
                    x_change, y_change = 0, BLOCK_SIZE  # Cambia la dirección hacia abajo

        x += x_change  # Actualiza la posición de la serpiente en el eje X
        y += y_change  # Actualiza la posición de la serpiente en el eje Y

        # Si la serpiente se sale de los límites de la pantalla, el juego termina
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        screen.fill(BLACK)  # Limpia la pantalla y la pinta de negro

        # Dibujar comida en la pantalla
        pygame.draw.rect(screen, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Actualiza el cuerpo de la serpiente
        snake_body.append([x, y])  # Añade la nueva posición de la cabeza de la serpiente
        if len(snake_body) > snake_length:  # Si el cuerpo de la serpiente es más largo que su longitud permitida
            del snake_body[0]  # Elimina el segmento más antiguo (cola)

        # Verifica si la serpiente colisiona consigo misma
        for segment in snake_body[:-1]:  # Verifica cada segmento excepto la cabeza
            if segment == [x, y]:  # Si la cabeza de la serpiente toca cualquier parte de su cuerpo
                game_over = True  # Termina el juego

        # Dibujar cada segmento de la serpiente en la pantalla
        for segment in snake_body:
            pygame.draw.rect(screen, WHITE, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()  # Actualiza la pantalla con todos los cambios realizados

        # Verifica si la serpiente come la comida
        if x == food_x and y == food_y:
            # Si la cabeza de la serpiente está en la misma posición que la comida
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0  # Nueva posición aleatoria para la comida
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1  # Aumenta la longitud de la serpiente

        clock.tick(SPEED)  # Controla la velocidad del juego (FPS)

    # Si el juego termina, pinta la pantalla de rojo y muestra el mensaje "Game Over"
    screen.fill(RED)
    message("Game Over!", WHITE)
    pygame.display.update()  # Actualiza la pantalla
    pygame.time.delay(2000)  # Pausa por 2 segundos antes de cerrar el juego
    pygame.quit()  # Cierra la ventana del juego
    quit()  # Sale del programa

# Ejecutar el juego
game()
