from pydantic import BaseModel, Field
from typing import Literal

class ResultadoTriagem(BaseModel):
    categoria: Literal["Rede/VPN", "Acesso/Senha", "Hardware", "Software", "Infraestrutura Crítica"] = Field(
        description="Categoria técnica do incidente."
    )
    urgencia: Literal["P1 - Crítico", "P2 - Alto", "P3 - Médio", "P4 - Baixo"] = Field(
        description="Nível de severidade baseado no impacto no trabalho do usuário."
    )
    resolvido_no_n1: bool = Field(
        description="True se o usuário puder resolver sozinho com os passos; False se exigir intervenção humana N2/Infra."
    )
    mensagem_usuario: str = Field(
        description="Resposta empática e clara, adaptada ao nível técnico do usuário, com passos numerados se aplicável."
    )
    resumo_escalonamento: str = Field(
        description="Resumo técnico objetivo para o analista humano caso precise de escalonamento."
    )