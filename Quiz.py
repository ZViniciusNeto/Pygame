#-*-encoding:UTF-8-*-
import random
# __author__ = 'vinicius'
acerto = True
cultural1 = {"pergunta" : "Dançar quadrilha, pular fogueira, o uso de balões e fogos de artifício e comidas como\
 arroz doce, canjica, pipoca e pé de moleque fazem parte de qual festa: ",
             "a" : "Carnaval", "b" : "Dia dos Finados", "c" : "Festa do Boi-Bumbá", "d" : "Festa Junina",
             "correta" : "d",
             "tipo" : "Cultura"}
cultural2 = {"pergunta" : "O frevo é uma dança típica de qual estado do Brasil: ",
            "a" : "Tocantis",
            "b" : "Minas Gerais",
            "c" : "Pernambuco",
            "d" : "São Paulo",
            "correta" : "c",
            "tipo" : "Cultura"}
esporte1 = {"pergunta" : "Qual desses times é espanhol: ",
            "a" : "Tenerife",
            "b" : "Porto",
            "c" : "PSG",
            "d" : "Nimes",
            "correta" : "a",
            "tipo" : "Esporte"}
esporte2 = {"pergunta" : "Que time abaixo é conhecido como leão do Pici: ",
            "a" : "Ceará",
            "c" : "Sport",
            "b" : "Fortaleza",
            "d" : "Havai",
            "correta" : "b",
            "tipo" : "Esporte"}
historia1 = {"pergunta" : "A Era Vargas que durou cerca de 15 anos e foi a segunda fase do Brasil República se caracterizou por: ",
             "a" : "Uma política político-administrativa centralizada",
             "b" : "Um caráter ditatorial em toda sua duração",
             "c" : "Um abandono definitivo à economia cafeeira que até então vigorava na República Velha",
             "d" : "Uma ideologia de igualdade e pouco autoritária por parte de Getúlio Vargas",
             "correta" : "a",
             "tipo" : "História"}
historia2 = {"pergunta" : "A Era Vargas durou: ",
             "a" : "1929 - 1944",
             "b" : "1930 - 1945",
             "c" : "1924 - 1939",
             "d" : "1934 - 1949",
             "correta" : "b",
             "tipo" : "História"}
tecnologia1 = {"pergunta" : "Qual o nome do sistema operacional mobile mais utilizado hoje em dia: ",
               "a" : "iOS",
               "b" : "Android",
               "c" : "Windows",
               "d" : "Linux",
               "correta" : "b",
               "tipo" : "Tecnologia"}
tecnologia2 = {"pergunta" : "Selecione a opção abaixo que não caracteriza uma medida de segurança para seu computador: ",
               "a" : "Deixar o Firewall ativado",
               "b" : "Mascarar seu endereçamento IP utilizando o proxy",
               "c" : "Utilizar o desfragmentador de discos do windows",
               "d" : "Colocar senha para que somente você tenha acesso ao sistema",
               "correta" : "c",
               "tipo" : "Tecnologia"}
musica1 = {"pergunta" : "Quem é a cantora de \"Era uma vez\": ",
           "a" : "Ana Vitória",
           "b" : "Dua Lipa",
           "c" : "Kell Smith",
           "d" : "Nenhuma das alternativas",
           "correta" : "c",
           "tipo" : "Musica"}
musica2 = {"pergunta" : "Qual dessas musicas não é do cantor \" Shawn Mendes\": ",
           "a" : "Stitches",
           "b" : "Kid In Love",
           "c" : "Mercy",
           "d" : "Feeling Good",
           "correta" : "d",
           "tipo" : "Musica"}
questao = [cultural1, cultural2, esporte1, esporte2, historia1, historia2, tecnologia1, tecnologia2, musica1, musica2]
questaoInicial = len(questao)
pontos = 0
while acerto == True:
    questaoNumero = random.randint(0, (len(questao)-1))
    teste = questao[questaoNumero]
    print "Tema da Pergunta: ", teste["tipo"]
    print teste["pergunta"]
    print " A) ", teste["a"], "\n B) ", teste["b"], "\n C) ", teste["c"], "\n D) ", teste["d"]
    escolha = raw_input("\nResposta: ").lower()
    if escolha == teste["correta"]:
        pontos += 1
        del questao[questaoNumero]
    else:
        acerto = False
    if questaoInicial == pontos:
        print "Você zerou meu quiz ^^, mande perguntas para que o quiz fique mais divertido, " \
              "caso tenha gostado ou não me mande seu seu feedback para que eu possa melhorar"
        acerto = False
print "Você marcou", pontos, "pontos"
