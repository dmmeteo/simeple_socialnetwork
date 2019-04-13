#!/usr/bin/env python
import pipeline
import click


@click.command()
@click.option('-t', '--type', type=click.Choice(['csv', 'json', 'txt']))
@click.argument('input', type=click.File())
def runner(type, input):
    f = str(input.read())
    separator = ',' if type == 'csv' else ' '

    if type in ('csv', 'txt'):
        for data in f.split('\n'):
            data = data.split(separator)
            if len(data) > 2:
                pipeline.start(*data)
    else:
        for data in eval(f):
            pipeline.start(
                data['email'],
                data['max_posts'],
                data['max_likes']
            )
    print('>>> your config has been sent to the worker and will be done soon.')


if __name__ == '__main__':
    runner()
