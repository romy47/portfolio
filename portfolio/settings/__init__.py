from .settings import *
if IS_DEV == True:
   from .dev import *
else:
   from .prod import *
