from stevebannon.client import SteveBannonClient
import click


@click.group()
def steve_cli():
    pass


@steve_cli.command()
@click.option('-F', '--force', is_flag=True, help='Força o envio de mensagem para todos os seus dialogos e membro de grupos')
@click.option('-G', '--all-groups', is_flag=True, help='Envia para todos os grupos que você participa')
@click.option('-U', '--all-users', is_flag=True, help='Envia para todos os seus dialogos')
# @click.argument('text', help='Mensagem para ser enviada')
@click.argument('text')
def send_message(text):
    """
    Envia mensagem para grupos e usuarios.
    """
    if force and all_users:
        click.echo('Enviando mensagem para todos os contatos encontrados...')
        SteveBannonClient.send_message_brute_force(text)
        click.echo('Mensagens enviadas com sucesso!')
    if all_groups:
        click.echo('Enviando mensagem para todos os grupos...')
        SteveBannonClient.send_message_to_all_groups(text)
        click.echo('Mensagens enviadas com sucesso!')
    if all_users:
        click.echo('Enviando mensagem para todos os usuarios...')
        SteveBannonClient.send_message_to_all_people(text)
        click.echo('Mensagens enviadas com sucesso!')


@steve_cli.command()
@click.option('-F', '--force', is_flag=True, help='Força o envio de mensagem para todos os seus dialogos e membro de grupos')
@click.option('-G', '--all-groups', is_flag=True, help='Envia para todos os grupos que você participa')
@click.option('-U', '--all-users', is_flag=True, help='Envia para todos os seus dialogos')
@click.option('--caption', default=None, help='Legenda para a imagem')
# @click.argument('path', type=click.Path(exists=True), help='Caminho para a imagem')
@click.argument('path', type=click.Path(exists=True))
def send_image(path, caption):
    """
    Envia imagem para grupos e usuarios.
    """
    if force and all_users:
        click.echo('Enviando imagem para todos os contatos encontrados...')
        SteveBannonClient.send_image_brute_force(path, caption)
        click.echo('Imagens enviadas com sucesso!')
    if all_groups:
        click.echo('Enviando imagem para todos os grupos...')
        SteveBannonClient.send_image_to_all_groups(path, caption)
        click.echo('Imagens enviadas com sucesso!')   
    if all_users:
        click.echo('Enviando imagem para todos os usuarios...')
        SteveBannonClient.send_image_to_all_people(path, caption)
        click.echo('Imagens enviadas com sucesso!')


@steve_cli.command()
@click.option('--group', default=None, help='Grupo especifico para pegar as mensagens')
@click.option('--total', default=1000, help='Quantidade de mensagens para fazer o calculo')
@click.option('--top', default=10, help='Quantidade de usuarios mais engajados')
def get_engagement(group, total, top):
    """
    Traz a lista de pessoas mais engajadas em grupos.
    """
    SteveBannonClient.get_group_more_engaged(group, total, top)


if __name__ == '__main__':
    steve_cli()