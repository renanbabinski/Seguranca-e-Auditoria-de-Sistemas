
# TUTORIAL

## HACKEANDO REDES WI-FI WPA2

**OBS**:Para este tutorial estarei usando uma distribuição do Kali Linux. Esta distro já contém todos os softwares necessários que serão utilizados nesse passo-a-passo. Você pode utilizar qualquer outra distribuição Linux, porém precisará instalar cada ferramenta separadamente. TODOS OS COMANDOS DEVEM SER EXECUTADOS COMO ADMINISTRADOR. SE NÃO TIVER CERTEZA SE TEM OS PRIVILÉGIOS ADICIONE:

        sudo

NO INICIO DE CADA COMANDO.

**********************************

Vamos lá...

1. Você irá precisar um adaptador Wi-fi. Os notebooks já possuem conexão Wireless integrada, se você tiver um desktop precisará de um adaptador USB ou PCI.  

2. Abra um terminal, então digite:

        ifconfig
    serão listados todos os seus adaptadores de rede:  

    ![Lista de adaptadores](Adaptadores1.png)

    Se tudo estiver correto, seu adaptador Wireless deve aparecer como **wlan0** ou **wlan1**.  

3. O próximo passo é colocar esse adaptador Wi-fi no modo de monitoramento, para isso você deve desabilitar o adaptador primeiramente com:

        ifconfig wlan0 down

    Alterando para o modo monitoramento:

        iwconfig wlan0 mode monitor

    Você pode verificar se o modo do adaptador foi alterado digitando:

        iwconfig

    ![Modo monitor](Modo_monitor.png)

    Agora você precisa habilitar o adaptador novamente:

        ifconfig wlan0 up  

4. Agora vamos utilizar o **airodump-ng** para listar as redes Wi-fi e escolher qual será atacada. Para isso digite o comando seguido da interface de monitoramento que acabamos de configurar:

        airodump-ng wlan0

    Você terá uma tela semelhante a esta:

    ![Redes Disponiveis](Wireless_networks.png)  

    **OBS:** escondi os endereços da minha rede privada e seus respectivos nomes. A rede que nos interessa é a **Victim_Network**, ela foi gerada por mim somente para esse fim de teste. ESSE TUTORIAL É SOMENTE PARA FINS DIDÁTICOS, NÃO FAÇA ISSO NA REDE DE TERCEIROS.  

    Para o próximo passo vamos precisar do BSSID do nosso alvo que é C0:25:E9:77:AB:00 e o canal que é o 3.  

5. Agora o passo chave deste tutorial, capturar um “handshake”. É muito importante ressaltar que para conseguir um handshake da rede que estamos atacando é necessário que haja pelo menos 1 cliente conectado nela. O handshake do inglês significa “aperto de mão”. Ele acontece quando um cliente tenta se conectar ao router, para isso existe uma negociação de senha que é chamada de “handshake”. Se capturarmos o pacote onde esse dado está armazenado poderemos quebrar a senha Wi-fi.

    Para iniciar o monitoramento do tráfego em busca do handshake utilizamos o seguinte comando:

        airodump-ng -w handshake -c 3 -bssid C0:25:E9:77:AB:00 wlan0

    