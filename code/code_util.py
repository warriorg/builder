def underline_to_camel(underline_format):
     '''
         下划线命名格式驼峰命名格式
     '''
     camel_format = ''
     if isinstance(underline_format, str):
         for _s_ in underline_format.split('_'):
             camel_format += _s_.capitalize()
     return camel_format


def underline_to_java_bean(underline_format: str):
    '''
    符合java bean的命名
    '''
    camel_format = ''
    for _s_ in underline_format.split('_'):
       camel_format += _s_.capitalize()
       
    
    if len(camel_format) > 1 and camel_format[1].islower():
       camel_format = camel_format[:1].lower() + camel_format[1:] 

    return camel_format
