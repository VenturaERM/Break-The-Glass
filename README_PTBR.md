# VENTURA ERM
VENTURA ERM é uma ferramenta para automatizar a coleta, armazenamento e análise de eventos do AWS CloudTrail. Ela permite aos usuários baixar arquivos de eventos CloudTrail de várias regiões da AWS, compactá-los e gerar hashes de segurança para verificação de integridade.

## Pré-requisitos
Python 3.x

Bibliotecas AWS SDK para Python (Boto3)

Acesso configurado à AWS CLI com as devidas permissões

## Instalação
Clone o repositório: git clone  https://github.com/VenturaERM/Break-The-Glass

Instale as dependências necessárias: pip install boto3 requests

## Uso
Para usar o VENTURA ERM, siga estes passos:

Configure seu ambiente AWS CLI com as credenciais e a região desejada.

Execute o script: python [Break-The-Glass.py](https://github.com/VenturaERM/Break-The-Glass/blob/main/break_the_glass.py)

Os arquivos do CloudTrail serão baixados, compactados e terão sua integridade verificada automaticamente.

## Contribuições
Contribuições são bem-vindas! Para contribuir:

Faça um fork do repositório.

Crie uma branch para sua feature: git checkout -b minha-nova-feature

Faça suas alterações e commit: git commit -am 'Adiciona alguma feature'

Push para a branch: git push origin minha-nova-feature

Envie um pull request.

## Licença
Este projeto está sob a licença [MIT](https://github.com/VenturaERM/Break-The-Glass/blob/main/LICENSE). 
Veja o arquivo LICENSE para mais detalhes.

## Contato
Para entrar em contato, envie um e-mail para [contato@venturaerm.com](https://venturaerm.com/contact_us).
