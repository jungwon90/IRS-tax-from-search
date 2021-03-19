import json
import click
from searchbot import IRSFormSearchBot
from downloadbot import DownloadBot

@click.group()
def cli():
    """ A group of commands """
    pass

@click.command()
@click.argument('forms', nargs=-1)
def search(forms):
    """ Take a list of tax form names,
    Search the forms and return the data as JSON. """
    
    # A list that will store data of forms
    forms_data_list = []
    for form in forms:
        # Create IRSFormSearchBot object and search the data
        irs_bot = IRSFormSearchBot(form)
        data = irs_bot.search()
        forms_data_list.append(data)

    print(json.dumps(forms_data_list))
    # Return the data of forms as JSON
    return json.dumps(forms_data_list)


@click.command()
@click.argument('download_input', nargs=2)
def download(download_input):
    """ Take a tax form name and range of years(ex: 2018-2020),
    Download all PDFs available within the range. """

    try:
        # Extract arguments from the user input
        form_name = download_input[0]
        min_year = int(download_input[1][:4])
        max_year = int(download_input[1][5:])
        # Creat DownloadBot object and download the PDFs
        download_bot = DownloadBot(form_name, min_year, max_year)
        download_bot.download()
    except:
        print('You may have worng commands!')

cli.add_command(search)
cli.add_command(download)



if __name__ == "__main__":
    cli()