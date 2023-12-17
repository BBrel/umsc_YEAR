from . import main_handl, vk_handl, email_handl

labelers = [main_handl.config.labeler, vk_handl.config.labeler, email_handl.config.labeler]

__all__ = ['labelers']
