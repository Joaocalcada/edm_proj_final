# Estudo da qualidade do ar das cidades.

Faculdade de Engenharia da universidade do Porto

Projeto realizado por: João Pedro de Azevedo Calçada 

Nº:201703511

## Introdução 
  Este projeto surgiu no âmbito da disciplina de Eletrónica Digital e Microprocessadores. 
  
  Em particular, o tema da qualidade do ar, surge em tempos onde cada vez se fala mais da poluição provocada pelo Homem e das suas consequências. Neste projeto, criei um programa que, em conjunto com o microprocessador ESP-32, permite recolher dados relativos à qualidade do ar e concentrações de certos gases em cidades de todo o mundo.

## Material
![alt text](https://github.com/Joaocalcada/edm_proj_final/blob/master/Proj%20final%20material.png "Imagem 1 - Material utilizado no projeto.")

## API aqicn
  Recolhe dados relativos à qualidade do ar da cidade pretendida, (aqi->Air quality index), para além do índice de qualidade do ar também nos dá informações relativas a gases específicos, densidade de partículas e outro conteúdo, como a humidade e a velocidade do vento. Infelizmente, nem todas as cidades conteem o mesmo detalhe nas informações o que, irá levar alguns problemas no funcionamento do programa.Por exemplo, Pequim contém informação de até 8 dias atrás enquanto que, o Porto de apenas um dia e nem sequer contém sobre todos os gases.

## Código em Micropython
  O código é constituído por três secções principais:
  
  **Atribuição das variáveis e dos pinos**
  
  **Funções**
  
    Existem duas funções: A função x(varb), irá receber o valor relativo ao gás em estudo recolhido a partir da API e a partir daí, ira avaliar o perigo que este valor constitui, de acordo com valores tabelados.
    A função ledproc(x,y) recebe o grau de perigo da concentração encontrada do gás (o x constitui o grau de perigo sendo que o seu valor está de acordo com a Tabela 1) 
    
--- |AQI|CO(ppm)|SO2 (μg/m3)|Ozono(μg/m3) 
--- | --- | --- | ---|---
Boa  |0-50| 0-5|0-80|0-80 
Moderada |50-100|5-10|80-366|80-160 
Não saudável para grupos sensíveis |100-150 |10-15|366-800|160-200   
Pouco saudável|150-200 |15-30| 800-1600|200- 800 
Muito insalubre|200-250|30-40|1600-2100|800-1000
Perigoso|>250|>40|>2100|>1000

Tabela 1

  **Mecanismo**
  
    Nesta secção começamos por recolher dados ao API e a partir daí usamos as funções para dessa forma, conseguirmos expor os dados da maneira pretendida. De notar, que apenas começam a aparecer dados quando carregamos num dos botões sendo que o tipo de gás em estudo é controlado pelos botões.
    
 ## Conclusão 
  Assim, Com este projeto consolidei conhecimentos do funcionamento do ESP32 em particular, do funcionamento de API´s e das suas vantagens. Também foi possível analisar o estado da poluião de alguns países facto particlarmente interessante dado que, nos encontramos numa crise da poluição. Também gostava de referir que com a chegada do verão esta funcionalidade pode ser usada para perceber o impacto nos incêndios algo que, infeizmente ataca fortemente Portugal.
 
 ## Referências
  https://aqicn.org
  https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet
  https://iema.es.gov.br/qualidadedoar/boletimdiario
  
