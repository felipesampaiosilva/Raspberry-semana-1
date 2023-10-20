## Construção do Circuito

O código é projetado para funcionar em um Raspberry Pi Pico e realiza duas tarefas:

Leitura da Luminosidade: O programa utiliza um sensor de luminosidade chamado LDR (Light-Dependent Resistor). Este sensor muda sua resistência elétrica com base na quantidade de luz que incide sobre ele. Quanto mais luz, menor é a resistência.

Exibição no Display LCD: O Raspberry Pi Pico está conectado a um display LCD que é capaz de mostrar informações. O código lê a resistência do LDR e exibe esse valor no display LCD.

O programa executa essas duas tarefas repetidamente. Ele atualiza a leitura do LDR e mostra o valor no display a cada segundo. Dessa forma, você pode monitorar o nível de luz no ambiente em que o Raspberry Pi Pico está localizado, pois a resistência do LDR muda com as mudanças na luminosidade.

A imagem abaixo demonstra como o circuito final está organizado e funcionando. O código completo está na pasta **Raspberry_versao_final**.

![RaspBerry](/images/imagem_ldr.png "MarineGEO logo")