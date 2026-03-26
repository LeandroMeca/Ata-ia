# Base de Conhecimento

## Prompt sugerido para essa etapa:

### Preciso organizar a base de conhecimento do agente ata condominio.

- Tenho estes aarquivos de dados:[liste os arquivos]. Me ajude a:(1) entender o que cada arquivo conténm, (2) decidir como usar cada um, (3) criar um exemplo de contexto formatado para incluir no prompt.

## Dados Utilizados

| Arquivo                      | Formato | Utilização no Agente                        |
| ---------------------------- | ------- | ------------------------------------------- |
| `ata_condominio.csv`         | CSV     | Regras seguidas da legislação de assembléia |
| `morador.json`               | JSON    | Dados do morador e seus dados               |
| `regras.json`                | JSON    | Regras gerais                               |
| `ocorrencias_condominio.csv` | CSV     | ocorrências diarias                         |
| `visitantes.json`            | JSON    | dados visitante                             |
| `empresas.json`              | JSON    | tipos de serviços                           |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Foi adicionado mais documentos para uma maior segurança e controle dos moradores

---

## Estratégia de Integração

### Como os dados são carregados?

> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV podem ser carregados por um código Java

dependencia maven

```xml
<dependency>
    <groupId>com.opencsv</groupId>
    <artifactId>opencsv</artifactId>
    <version>5.9</version>
</dependency>
```

Código para extrair os dados

```java
import com.opencsv.CSVReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class CarregarCSV {

    public static void main(String[] args) {

        String arquivo = "atas_condominio.csv";
        List<AtaCondominio> atas = new ArrayList<>();

        try (CSVReader reader = new CSVReader(new FileReader(arquivo))) {

            String[] linha;
            reader.readNext(); // pula cabeçalho

            while ((linha = reader.readNext()) != null) {

                AtaCondominio ata = new AtaCondominio(
                        linha[0],
                        linha[1],
                        linha[2],
                        linha[3],
                        linha[4]
                );

                atas.add(ata);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        atas.forEach(System.out::println);
    }
}

```

### Como os dados são usados no prompt?

> Os dados vão no system prompt? São consultados dinamicamente?

A injeção vai ser manual através do prompt, para melhor precisão e mais dados poderiamos utilizar dados dinamicos

```text
    ATA CONDOMINIO (CSV):
        data,canal,tema,resumo,resolvido
        2025-01-10,assembleia,Barulho após 22h,Definido que não é permitido som alto após as 22h em dias de semana,sim
        2025-01-10,assembleia,Uso da piscina,Piscina permitida das 08h às 22h apenas para moradores e convidados registrados,sim
        2025-02-05,assembleia,Animais de estimação,Permitido animais desde que usem guia nas áreas comuns,sim
        2025-02-05,assembleia,Vagas de garagem,Proibido estacionar em vagas de outros moradores,sim
        2025-03-12,assembleia,Reforma em apartamentos,Reformas permitidas apenas entre 08h e 18h em dias úteis,sim
        2025-03-12,assembleia,Uso do salão de festas,Reserva obrigatória com antecedência mínima de 3 dias,sim
        2025-04-20,assembleia,Entrega de encomendas,Porteiro autorizado a receber encomendas pequenas,sim
        2025-05-15,assembleia,Uso do elevador de serviço,Mudanças devem usar apenas o elevador de serviço,sim
        2025-06-01,assembleia,Lixo reciclável,Separação de lixo reciclável obrigatória,sim
        2025-06-18,assembleia,Segurança do prédio,Instalação de novas câmeras de segurança aprovada,sim

    MORADOR (JSON):

        {
            "nome": "Carlos Mendes",
            "idade": 41,
            "apartamento": "Bloco B - 302",
            "tipo_morador": "proprietario",
            "numero_moradores": 3,
            "possui_pet": true,
            "veiculos": 1,
            "email": "carlos@email.com",
            "telefone": "11999999999",
            "interesses": ["uso da piscina", "salão de festas", "segurança do condomínio"]
        }

    REGRAS (JSON):
        [
            {
            "regra": "Barulho",
            "descricao": "Não é permitido som alto idependente de horario",
            "categoria": "convivencia",
            "multa": true
            },
            {
            "regra": "Uso da piscina",
            "descricao": "Piscina aberta das 08h às 22h",
            "categoria": "lazer",
            "multa": false
            },
            {
            "regra": "Animais",
            "descricao": "Animais devem circular com guia nas áreas comuns",
            "categoria": "convivencia",
            "multa": true
            },
            {
            "regra": "Garagem",
            "descricao": "Cada morador deve estacionar apenas em sua vaga",
            "categoria": "garagem",
            "multa": true
            },
            {
            "regra": "Reformas",
            "descricao": "Reformas permitidas apenas entre 08h e 18h em dias úteis",
            "categoria": "manutencao",
            "multa": false
            },
            {
            "regra": "Visitantes",
            "descricao": "É proibido visitante transitar em vários apartamento sem comunicar a portaria",
            "categoria": "visita",
            "multa": false
            }
        ]


    OCORRENCIAS CONDOMINIO (CSV):
        data,descricao,categoria,status
        2025-03-01,Som alto no apartamento 204,barulho,resolvido
        2025-03-04,Cachorro sem guia no corredor,animais,resolvido
        2025-03-10,Carro estacionado em vaga errada,garagem,resolvido
        2025-03-15,Luz queimada no corredor do 5º andar,manutencao,resolvido
        2025-03-22,Vazamento na área da garagem,manutencao,em_andamento
        2025-04-02,Elevador parado por falha técnica,manutencao,resolvido
        2025-04-05,Reserva duplicada do salão de festas,reserva,resolvido
        2025-04-12,Lixo deixado fora do horário,lixo,resolvido

    VISITANTES (JSON):
        {
            "nome": "Ralf",
            "documento": 111111111,
            "apartamento": "Bloco B - 302",
            "data": "dia 20/03/2026 as 18:00"
        }


    EMPRESAS (JSON):
        {
            "nome": "Limpeza & organização",
            "servico": "limpeza da lixeira",
            "descricao": "limpeza de lixeira e escadas das torres",
            "horarios": "das 07:00 as 17:00"
        }


```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Abaixo temos uma cópia de dados reais utilizados da base de dados com informações precisas.

```
visitantes:
- Nome: João Silva
- Documento: 111111111
- Apartamento: Bloco A - 210
- Data: 2026-03-25

Empresas:
- Nome: Grupo Leao de juda
- Servico: Segurança
- Descricao: Portaria e ronda
- Horarios: 24 horas
...
```
