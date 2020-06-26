def pickValidationFile():
    srcFilePath = pickFile(); filename, file_extension = splitext(srcFilePath)
    if not isfile(filename + '.sign'): raise Exception('Signature not exist')
    if file_extension == '.sign': raise Exception('You picked signature. Nonsense.')
    return open(srcFilePath, 'rb'), open(filename + '.sign', 'rb')
