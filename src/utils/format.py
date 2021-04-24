def format_output (value):
    if value is None: 
        return -1

    output = str(round(value)).replace(".", "")

    if len(output) == 1:
        output = output + "000"
    elif len(output) == 2:
        output = output + "00"

    return int(output)