import os
from shutil import move

import click

EXTENSIONS = [
    '.cr2',
    '.raf',
    '.jpg',
    '.jpeg'
]


@click.command()
@click.option('--src', help='Source directory')
@click.option('--dst', help='Destination directory')
def run(src, dst):
    date_dirs = os.listdir(src)

    for date_dir in date_dirs:
        src_photos_dir = os.path.join(src, date_dir)
        dst_photos_dir = os.path.join(dst, date_dir)

        click.echo(f'# Inspecting {src_photos_dir}')

        try:
            src_photos = os.listdir(src_photos_dir)
        except NotADirectoryError:
            click.echo(f'> Skipped {src_photos_dir}')
            continue

        try:
            dst_photos = os.listdir(dst_photos_dir)
        except NotADirectoryError:
            click.echo(f'> Skipped {dst_photos_dir}')
            continue

        for photo in src_photos:
            if photo not in dst_photos:
                continue

            # Only bigger src photos got copied over
            src_photo = os.path.join(src_photos_dir, photo)
            dst_photo = os.path.join(dst_photos_dir, photo)

            if os.path.getsize(src_photo) <= os.path.getsize(dst_photo):
                continue

            click.echo(f'Moving {src_photo}')
            move(src_photo, dst_photo)


if __name__ == '__main__':
    run()
