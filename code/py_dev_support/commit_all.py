#!/usr/bin/env python3

import click
import subprocess

@click.command()
def run(version):
    bash_script = f"""
    #!/bin/bash
    git add .
    git commit -m "auto commit message"
    git push
    """
    subprocess.run(bash_script, shell=True)