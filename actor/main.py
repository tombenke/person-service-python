#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The main entry-point of the application.
"""
from common.app import application_entrypoint
from actor.config import config
from actor.app.app import Application


def main():
    """The main entry point of the application"""
    application_entrypoint(Application, config)


if __name__ == "__main__":
    main()
