from . import greet_handler, start

labelers = [greet_handler.config.labeler, start.config.labeler]

__all__ = ['labelers']
