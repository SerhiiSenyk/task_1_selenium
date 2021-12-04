def singleton(cls):

    class SingleCls(cls):

        inst = None
        inited = False

        def __new__(cls, *args, **kwards):
            if cls.inst is None:
                cls.inst = object.__new__(cls, *args, **kwards)
            return cls.inst

        def __init__(self, *args, **kwards):
            if not self.inited:
                self.inited = True
                super(SingleCls, self).__init__(*args, **kwards)

        @classmethod
        def instance(cls):
            return cls.inst if cls.inst else cls()

    return SingleCls