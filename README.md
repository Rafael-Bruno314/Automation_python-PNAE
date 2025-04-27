# Automation_python-PNAE

Automações desenvolvidas em Python para otimizar processos relacionados ao Programa Nacional de Alimentação Escolar (PNAE), atendendo às demandas do contrato da Emater com a Secretaria Estadual de Educação de Minas Gerais (SEE-MG). O projeto foi desenvolvido durante estágio supervisionado na Empresa de Assistência Técnica e Extensão Rural do Estado de Minas Gerais (EMATER-MG).

**Link relacionado:**  
[Parceria entre EMATER e SEE beneficia escolas e agricultores familiares](https://www.educacao.mg.gov.br/parceria-entre-emater-e-see-beneficia-escolas-e-agricultores-familiares/)

## Impacto do Projeto

O projeto possibilitou a automação da coleta de dados via web scraping de fazendeiros locais e cooperativas agrícolas de todas as 853 cidades de Minas Gerais vinculadas ao PNAE – anteriormente realizadas manualmente, ocupando um setor inteiro de técnicos agrícolas.

**Resultados:**
- Redução do tempo de coleta de cerca de 2 meses para poucas horas;
- Economia de tempo e recursos públicos;
- Melhoria nos serviços prestados pela EMATER-MG aos agricultores familiares.

## 📁 Estrutura do Projeto

O repositório contém notebooks Jupyter que automatizam as seguintes tarefas:

1. **Automatizando a meta 1.1.ipynb:**  
   Automação da meta 1.1 - Mapa da Oferta de Alimentos da Agricultura Familiar.

2. **Automatizando a meta 2.3.ipynb:**  
   Automação da meta 2.3 - Assistência Técnica e Extensão Rural: Produção, Organização e Mercado.

3. **Automatizando a meta 3.1.ipynb:**  
   Automação da meta 3.1 - Assistência Técnica e Extensão Rural em Agroindústria.

4. **Comprimir pdf.ipynb:**  
   Redução do tamanho dos arquivos PDF baixados durante a automação (~30.000 arquivos).

5. **Zipando com limites.ipynb:**  
   Compressão de arquivos em ZIP para adequação aos limites de upload do sistema da empresa.

## 🛠️ Principais Tecnologias Utilizadas

- **Python**
- **Selenium:** Automação de navegadores web.
- **PDFNetPython3:** Ferramenta para manipulação de PDFs.
- **Pyperclip:** Módulo Python para funções de copiar e colar da área de transferência.

## Pnae pelo SIGPC

O repositório também contém um pequeno projeto realizado anteriormente ao contrato: uma automação utilizando o [Selenium IDE](https://www.selenium.dev/selenium-ide/), uma extensão para navegadores que realiza web scraping, com o objetivo de coletar os gastos de todas as 853 cidades de Minas Gerais com o PNAE.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.
