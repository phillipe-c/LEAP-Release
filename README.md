![alt text](https://github.com/phillipe-c/LEAP-Release/blob/main/Others/LEAP%20Logo.png?raw=true)
# LEAP 1.5.9-LU3
The LISA Experimental Accessibility Project Repository<br /><br />
LISA is an Intelligent Assistant, that let's you do things like *advanced* internet searches and much more.
The assistant was from the very beginning designed to help teachers and students in classrooms to do things like searching the web, getting news or just simply knowing how the weather is. It uses AIML and LIM-L to recognize patterns in speech to then give an answer to each specific question.

## How to use it
After downloading and installing the software, simply run the main script, `lisa_LAS.py`, adding flags to run the program in text or in speech recognition (*voice*) based mode and that's it. Here are the following options to run the program: <br />
- **-v** activates speech recognition<br />
- **-g** activates google's speech synthesis 

## Usage Examples

- ### Searching the web
  Lisa retrieves the information contained in a google snippet related to the asked question. If it doesn't find anything in the snippet, it searches wikipedia for an answer, and if those sources didn't offer any result, it seaches for related news, which can apparently give pretty good answers to most of the questions asked. Here are some examples of answers:<br />
  
  **Você:** Lisa quantos fios de cabelo a gente tem? <br />
  **Lisa:** Entre 20 e 30 anos, a cabeça humana tem, em média, 615 fios por centímetro quadrado – o que quer dizer 150 000 fios, aproximadamente. Dos 30 aos 50, o número cai para 485 fios e vai diminuindo lentamente. Um octogenário saudável tem 435 raízes por centímetro quadrado.<br />
  ________________________________________________________
  
  **Você:** Lisa qual sistema digestório o filo nematoda tem <br />
  **Lisa:** Processando!  Os nematódeos são os primeiros animais a apresentarem sistema digestório completo, ou seja, possuem boca e ânus. A boca possui lábios ao redor. Esses lábios possuem papilas sensoriais, dentes ou placas cortantes seguidas de uma faringe musculosa que efetua sucção do alimento, bombeando para o intestino.<br />
  _______________________________________________________

  **Você:** Lisa qual é a resolução 4k<br />
  **Lisa:** É pra já!  Um televisor 4K possui uma resolução quatro vezes maior que um televisor Full HD, isto é, ele possui uma resolução de 3840 x 2160, ou seja, 2160 linhas contendo 3840 pixels em cada linha totalizando 8.294.400 pixels.<br />
  ________________________________________________________
  Lisa, when making a Google Search, uses real-time location, so that it knows nearby points of interest:<br />
  
  **Você:** Lisa qual é o hospital mais perto de mim<br />
  **Lisa:** Processando!  Hospital São Paulo<br />

- ### Weather
  Lisa uses a modified version of the ***in search*** search engine to get weather information from google. It retrieves the temperature, pressure, humidity, wind speed, location and the description of the weather<br />
  
  **Você:** Lisa como está o tempo agora?<br />
  **Lisa:** A temperatura em Paulista, São Paulo - SP está por volta dos 28 graus com Chuvisco leve. A precipitação é de 32%, a humidade é de 77%, e está ventando a uma velocidade aproximada de 11 km/h.

- ### News
  Lisa can say the latest news from newspapers, such as *Estadão*, *Folha de São Paulo* and *BBC News Brazil*.<br />
  
  **Você:** Lisa me diga as notícias principais<br />
  **Lisa:** Pesquisa sugere que 46% dos brasileiros não tomariam vacina chinesa contra covid-19. Mas cerca de um terço dos princípios ativos de medicamentos usados no Brasil são importados do país asiático.<br />
  _____________________________________________________________________________________________________________________________________
  Lisa can also search for news about specific topics, using the *Bing News* search engine.<br />
  
  **Você:** Lisa me diga notícias sobre o novo iPhone 12<br />
  **Lisa:** Os novos recursos poderosos do iPhone 12, como a gravação de vídeo em Dolby Vision 4K e as fotos HDR ultranítidas, exigem uma tela igualmente avançada. Por isso, usamos a melhor que já fizemos: a Super Retina XDR. 1200 nits de brilho em HDR.<br />
  
- ### Scenes
  LISA also has a handy feature called *scenes*. Scenes are just pre-built scripts that LISA uses to say information such as weather, date and time, news, suggestions and more. They are activated every time the user says ´bom dia´ or ´boa noite´:<br /><br />
  **Você:** Lisa bom dia<br />
  **Lisa:** Bom dia! Fico feliz em escutar a sua voz. Hoje é terça-feira, dia 21 de dezembro de 2021, o dia em que comemoramos o Início do Verão. É bom lembrar que já se passaram cerca de 97 por cento do ano. Agora aqui vai a previsão do tempo: A temperatura agora é de 27 graus celcius. E a precipitação hoje é de 50%. É recomendado levar um guarda chuva. Os ventos estão a uma velocidade de 5km/h, e a umidade é de 71%. Aqui vai a notícia mais recente: Mais da metade da população brasileira está vacinada com pelo menos a primeira dose da vacina. Espero que tenha um ótimo dia!<br />

## LIM Language
You can also contribute to the intelligence of LISA by programming conversations with the easiest language ever. [See LIM-L documentation for more.](https://github.com/phillipe-c/LIM-L)

## Contact
Do you want to contribute to the project or have an awesome idea? Or you just want to report an error? Anyway, feel free to send an email to me through this adress:  `icephillipe@hotmail.com`

## License
LEAP License
Copyright (c) 2022, Phillipe Caetano. All rights reserved.
Redistribution and use in source and binary forms, with or without modification, 
are permitted provided that the following conditions are met:

1. Phillipe Caetano must allow the redistribution and use in source and binary 
   forms, with or without modification of the software in a written permission 
   letter before the redistribution.

2. Phillipe Caetano can modify, remove, and add conditions in and out of this 
   license at any time, previously or after the written permission, and the 
   license of the redistributed software must immediately be modified to match 
   the new license.

3. In case of granted permission from Phillipe Caetano in the written permission 
   letter, the following conditions must be met:

   3.1. Redistributions in source and in binary form must reproduce the above 
        copyright notice, this list of conditions from topic 1 and below including 
        topic 1, and the following disclaimer in the documentation and/or other 
        materials provided with the distribution

   3.2. All advertising materials mentioning features or use of this software must 
        display the following acknowledgement: This product includes software 
        developed by Phillipe Caetano

   3.3. Neither the name of Phillipe Caetano nor the names of its contributors may 
        be used to endorse or promote products derived from this software without 
        specific prior written permission.

THIS SOFTWARE IS PROVIDED BY PHILLIPE CAETANO AS IS AND ANY EXPRESS OR IMPLIED WARRANTIES, 
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A 
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PHILLIPE CAETANO BE LIABLE FOR ANY 
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT 
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE 
USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
