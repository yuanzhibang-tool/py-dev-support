#!/usr/bin/env python3

import click
import subprocess

@click.command()
@click.option('--version', help='version name',required=True)
def run(version):
    bash_script = f"""
    #!/bin/bash
    git add .
    git commit -m "auto version update"
    git push
    git tag -a v{version} -m "auto tag v{version}"
    git push origin v{version}
    """
    subprocess.run(bash_script, shell=True)