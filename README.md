# Raspberry-Semana-1

O Raspberry Pi Pico é uma placa de microcontrolador de baixo custo e alto desempenho com interfaces digitais flexíveis. Principais recursos incluem:

- Chip microcontrolador RP2040 projetado pela Raspberry Pi no Reino Unido
- Processador de núcleo duplo Arm Cortex M0+, com clock flexível de até 133 MHz
- 264 kB de SRAM e 2 MB de memória flash embutida
- USB 1.1 com suporte a dispositivos e hospedeiros
- Modos de baixo consumo de energia e inativos
- Programação de arrastar e soltar usando armazenamento em massa via USB
- 26 pinos GPIO multifuncionais
- 2 SPI, 2 I2C, 2 UART, 3 ADC de 12 bits, 16 canais PWM controláveis
- Relógio e temporizador precisos integrados
- Sensor de temperatura
- Bibliotecas de ponto flutuante aceleradas no chip
- 8 máquinas de estado de E/S programáveis (PIO) para suporte a periféricos personalizados

O Raspberry Pi Pico é disponibilizado como um módulo em formato castelado que permite a soldagem direta em placas de suporte, enquanto o Pico H vem com cabeçalhos pré-soldados. A imagem abaixo mostra uma representação do lógica das saídas no microcontrolador.

![Esquema lógico do Raspberry](/images/raspberry-image.png "Raspberry")

<br>

## Das Funcionalidades (Interfaces de Comunicação):

O Raspberry Pi Pico oferece uma série de funcionalidades que o tornam uma placa de microcontrolador versátil e útil em uma variedade de aplicações. Vamos explorar algumas dessas funcionalidades que desempenham um papel fundamental em seu desempenho e flexibilidade.

- Power (Alimentação): O Raspberry Pi Pico é alimentado por meio dos pinos de alimentação (Power). Esses pinos fornecem a energia necessária para o funcionamento do dispositivo.

- Ground (Terra): Os pinos Ground são essenciais para criar um circuito completo e fornecer uma referência de terra para os componentes conectados.

- UART (Comunicação Serial): O Raspberry Pi Pico oferece interfaces UART (Universal Asynchronous Receiver-Transmitter) para comunicação serial. É possível usar esses pinos para transmitir e receber dados de forma serial.

- ADC (Conversor Analógico-Digital): O Pico inclui pinos ADC que podem ser usados para converter sinais analógicos em dados digitais. Isso é útil para leitura de sensores analógicos.

- SPI (Interface Serial Periférica): O Pico possui pinos SPI (Serial Peripheral Interface) que podem ser usados para comunicação serial de alta velocidade com outros dispositivos, como sensores e displays.

- I2C (Comunicação de Barramento I2C): Os pinos I2C (Inter-Integrated Circuit) permitem a comunicação de dados entre dispositivos de forma bidirecional e com apenas dois fios.

- Debugging (Depuração): O Raspberry Pi Pico oferece recursos de depuração por meio de pinos específicos que permitem a análise e depuração de programas em desenvolvimento.

- System Control (Controle do Sistema): Além das interfaces de comunicação e E/S, o Pico também oferece pinos para controle do sistema, que podem ser usados para funções específicas de controle e configuração.

<br>

## Especificações Técnicas:

- Chip Microcontrolador: RP2040.
- Processador: Núcleo duplo Arm Cortex M0+.

- Clock: Até 133 MHz.

- Memória: 264 kB de SRAM e 2 MB de memória flash embutida.

- Interfaces de Comunicação: USB 1.1, 2 SPI, 2 I2C, 2 UART.

- Pinos GPIO: 26 pinos multifuncionais.

- Conversão Analógico-Digital (ADC): 3 ADC de 12 bits.
- PWM: 16 canais PWM controláveis.
- Relógio e Temporizador: Integrados.
- Sensor de Temperatura: Incluso.
- Máquinas de Estado de E/S Programáveis (PIO): 8 máquinas programáveis para suporte a periféricos personalizados.
- Alimentação: O Raspberry Pi Pico é alimentado por meio dos pinos de alimentação (Power).
  Terra:

Os pinos Ground (Terra) são essenciais para criar um circuito completo e fornecer uma referência de terra para os componentes conectados.
