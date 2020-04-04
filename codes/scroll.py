import textwrap

def scroll(original, width=80, margins=5,top=1, bottom=1, padding=0, replacements=[]):
    temp = []
    for x in range(top):
        temp.append(' ')
    for line in original.split('\\n'):
        if line == '':
            temp.append(' ')
        else:
            temp.append(line)
    for x in range(bottom):
        temp.append(' ')
    message = []
    for line in temp:
        if line != ' ':
            for item in textwrap.wrap(line,(width - (margins * 2))):
                message.append(item)
        else:
            message.append(' ')
    reps = int(.9 + ((len(message)-4)/8))
    new_length = 5 + reps * 8
    border_top = int((new_length - len(message))/2)
    border_bottom = new_length - len(message) - border_top
    reassemble = []
    for x in range(border_top):
        reassemble.append(' ')
    for line in message:
        reassemble.append(line)
    for x in range(border_bottom):
        reassemble.append(' ')
    shape = []
    iwidth = width - (margins * 2)
    m = ' ' * margins
    shape.append('  ' + '_' * width + '__')
    shape.append(' /' + m + reassemble[0].ljust(iwidth) + m + '/ \\ ')
    shape.append('|' + m + reassemble[1].ljust(iwidth) + m + '| \\/ ')
    shape.append('|' + m + reassemble[2].ljust(iwidth) + m + '| ')
    shape.append(' \\' + m + reassemble[3].ljust(iwidth) + m + '\\ ')
    count = 0
    for loop in range(reps):
        shape.append('  \\' + m + reassemble[4 + count * 8].ljust(iwidth) + m + '\\ ')
        shape.append('   |' + m + reassemble[5 + count * 8].ljust(iwidth) + m + '| ')
        shape.append('   |' + m + reassemble[6 + count * 8].ljust(iwidth) + m + '| ')
        shape.append('  /' + m + reassemble[7 + count * 8].ljust(iwidth) + m + '/ ')
        shape.append(' /' + m + reassemble[8 + count * 8].ljust(iwidth) + m + '/ ')
        shape.append('|' + m + reassemble[9 + count * 8].ljust(iwidth) + m + '| ')
        shape.append('|' + m + reassemble[10 + count * 8].ljust(iwidth) + m + '| ')
        shape.append(' \\' + m + reassemble[11 + count * 8].ljust(iwidth) + m + '\\ ')
        count = count + 1
    shape.append(' _\\' + '_' * (margins + iwidth + margins) + ' \\ ')
    shape.append('/ ' + ' ' * (margins + iwidth + margins) + '/\\ | ')
    shape.append('\\' + '_' * (margins + iwidth + margins + 1) + '\\_/ ')
    final = ''
    for line in shape:
        data = line
        for item in replacements:
            data = data.replace(item[0],item[1])
        final = final + ' ' * padding + data + '|/'
    return final
        
    