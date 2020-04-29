
class Column:
    def __inint__(self, name, jdbcType, length, precision, scale, comment, nullable = False, primary = False):
        self.name = name
        self.type = jdbcType
        self.length = length
        self.precision = precision
        self.scale = scale
        self.comment = comment
        self.nullable = nullable
        self.primary = primary