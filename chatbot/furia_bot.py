class ChatbotFURIA:
    def __init__(self):
        self.data = {
            "jogadores": {
                "kscerato": {
                    "nome": "Kaike 'KSCERATO' Cerato",
                    "funcao": "AWPer",
                    "descricao": "Principal fragger e um dos mais consistentes da equipe. KSCERATO tem 1.15 de rating em 2023.",
                    "nacionalidade": "Brasileiro",
                    "idade": "25 anos"
                },
                "art": {
                    "nome": "Andrei 'arT' Piovezan",
                    "funcao": "IGL e Entry Fragger",
                    "descricao": "Conhecido por seu estilo agressivo e liderança inovadora. Mestre em estratégias não convencionais.",
                    "nacionalidade": "Brasileiro",
                    "idade": "27 anos"
                },
                "yuurih": {
                    "nome": "Yuri 'yuurih' Santos",
                    "funcao": "Suporte",
                    "descricao": "Especialista em clutches e um dos pilares da equipe. Tem 53% de duelos ganhos em 2023.",
                    "nacionalidade": "Brasileiro",
                    "idade": "24 anos"
                },
                "fallen": {
                    "nome": "Gabriel 'FalleN' Toledo",
                    "funcao": "AWP/Leader",
                    "descricao": "Lenda do CS brasileiro, traz experiência e liderança. 2x Major Champion (MLG Columbus 2016 e Cologne 2016).",
                    "nacionalidade": "Brasileiro",
                    "idade": "32 anos"
                }
            },
            "titulos": [
                "ESL Pro League Season 12 NA (2020)",
                "DreamHack Open Rio (2020)",
                "cs_summit 6 (2019)"
            ],
            "proximo_jogo": {
                "adversario": "Team Vitality",
                "data": "15/05/2024",
                "horario": "16:00 (Brasília)",
                "evento": "BLAST Premier: Spring Final",
                "local": "Londres, Reino Unido"
            },
            "ultimos_resultados": [
                "FURIA 2-1 NAVI (Mirage 16-14, Nuke 10-16, Inferno 16-12)",
                "FURIA 0-2 FaZe (Overpass 12-16, Vertigo 8-16)"
            ]
        }
        
        self.palavras_chave = {
            "jogadores": ["jogador", "player", "roster", "elenco", "equipe", "time", "jogadores", "team"],
            "titulos": ["título", "titulo", "troféu", "trofeu", "conquista", "campeão"],
            "proximo": ["próximo", "proximo", "jogo", "partida", "match", "quando"],
            "resultados": ["resultado", "ultimo", "último", "placar", "score","historico"],
            "ajuda": ["ajuda", "help", "?"]
        }

    def encontrar_jogador(self, pergunta):
        pergunta = pergunta.lower()
        for nome_jogador, dados in self.data["jogadores"].items():
            if (nome_jogador in pergunta or 
                dados["nome"].split()[0].lower() in pergunta):
                return nome_jogador
        return None

    def responder_sobre_jogador(self, nome_jogador):
        jogador = self.data["jogadores"].get(nome_jogador)
        if jogador:
            resposta = f"🔹 {jogador['nome'].upper()} 🔹\n"
            resposta += f"Função: {jogador['funcao']}\n"
            resposta += f"Idade: {jogador['idade']}\n"
            resposta += f"Nacionalidade: {jogador['nacionalidade']}\n"
            resposta += f"\nSobre: {jogador['descricao']}"
            return resposta
        return None

    def responder(self, mensagem):
        mensagem = mensagem.lower().strip()
        
        
        if mensagem in ["sair", "exit", "bye"]:
            return "Até mais! #VAMOFURIA"
            
        if mensagem in ["ajuda", "help", "?"]:
            return ("ℹ️ Tópicos disponíveis:\n"
                    "- Jogadores/elenco (ex: 'quem é o arT?', 'fale sobre o FalleN')\n"
                    "- Títulos/conquistas\n"
                    "- Próximo jogo\n"
                    "- Últimos resultados")
        
        
        if any(palavra in mensagem for palavra in ["time", "jogadores", "team", "equipe"]):
            jogadores = self.data["jogadores"]
            resposta = "👥 **Jogadores da FURIA** 🔥\n"
            for nome, info in jogadores.items():
                resposta += f"\n🔹 {info['nome']} | Função: {info['funcao']}"
            return resposta
        
       
        jogador = self.encontrar_jogador(mensagem)
        if jogador:
            resposta = self.responder_sobre_jogador(jogador)
            if resposta:
                return resposta
            else:
                return "Jogador não encontrado. Os jogadores atuais são: " + ", ".join(self.data["jogadores"].keys())
        
        
        for categoria, palavras in self.palavras_chave.items():
            if any(palavra in mensagem for palavra in palavras):
                if categoria == "titulos":
                    return "🏆 Títulos recentes da FURIA:\n" + "\n".join(f"- {titulo}" for titulo in self.data["titulos"])
                elif categoria == "proximo":
                    jogo = self.data["proximo_jogo"]
                    return (f"🎮 Próximo jogo:\n"
                            f"Adversário: {jogo['adversario']}\n"
                            f"Data: {jogo['data']} às {jogo['horario']}\n"
                            f"Evento: {jogo['evento']}\n"
                            f"Local: {jogo['local']}")
                elif categoria == "resultados":
                    return "📊 Últimos resultados:\n" + "\n".join(f"- {resultado}" for resultado in self.data["ultimos_resultados"])
        
       
        return ("Não entendi sua pergunta. Digite 'ajuda' para ver os tópicos disponíveis.\n"
                "Exemplos válidos:\n"
                "- Fale sobre o KSCERATO\n"
                "- Quando é o próximo jogo?\n"
                "- Quais são os títulos da FURIA?")