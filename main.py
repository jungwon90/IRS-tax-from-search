import json
import click
from searchbot import IRSFormSearchBot

@click.group()
def cli():
    pass

@click.command()
@click.argument('forms', nargs=-1)
def search(forms):
    click.echo('searched forms')
    forms_data_list = []
    for form in forms:
        irs_bot = IRSFormSearchBot(form)
        data = irs_bot.search()
        forms_data_list.append(data)

    print(json.dumps(forms_data_list))
    return json.dumps(forms_data_list)


@click.command()
def download():
    click.echo('downloaded forms')

cli.add_command(search)
cli.add_command(download)



if __name__ == "__main__":
    cli()