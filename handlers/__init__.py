from . import main_handl, by_vk, by_email

labelers = [main_handl.config.labeler, by_vk.config.labeler, by_email.config.labeler]

__all__ = ['labelers']
