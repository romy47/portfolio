from .settings import * # noqa

if IS_DEV is True: # noqa
    from .dev import * # noqa
else:
    from .prod import * # noqa
