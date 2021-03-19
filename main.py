import json
import click
from searchbot import IRSFormSearchBot
from downloadbot import DownloadBot

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
@click.argument('downloads', nargs=2)
def download(downloads):
    click.echo('downloaded forms')
    try:
        form_name = downloads[0]
        min_year = int(downloads[1][:4])
        max_year = int(downloads[1][5:])
     
        download_bot = DownloadBot(form_name, min_year, max_year)
        download_bot.download()
    except:
        print('Check out commands!')

cli.add_command(search)
cli.add_command(download)



if __name__ == "__main__":
    cli()