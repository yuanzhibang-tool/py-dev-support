#!/usr/bin/env python3

import click
import toml

@click.command()
@click.option('--toml_path', help='toml path',required=True)
@click.option('--section', help='action,support:major,minor,patch',required=True)
def run(toml_path,section):
    with open(toml_path, 'r') as f:
        toml_data = toml.load(f)
        current_version = toml_data['project']['version']
    # Assuming the current version is in the format "x.y.z"
    major, minor, patch = current_version.split('.')
    if section == 'major':
        major = int(major) + 1
        minor = 0
        patch = 0
    elif section == 'minor':
        minor = int(minor) + 1
        patch = 0
    elif section == 'patch':
        patch = int(patch) + 1
    new_version = f"{major}.{minor}.{patch}"
    toml_data['project']['version'] = new_version
    with open(toml_path, 'w') as f:
        toml.dump(toml_data, f)
    print(new_version)